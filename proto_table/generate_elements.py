"""Génère les tables Lua des prototypes à partir de elements.xlsx.

Usage :
    python generate_elements.py [elements.xlsx] [dossier_de_sortie]

Une feuille = une table Lua :
    resources    -> resources_data.lua    (roches, minerais, fluides naturels)
    elements     -> elements_data.lua     (les 118 éléments)
    alloys       -> alloys_data.lua       (alliages et leurs proportions)
    materials    -> materials_data.lua    (formes : lingot, plaque, poudre...)
    components   -> components_data.lua   (composants fabriqués)
    composition  -> composition_data.lua  (roche -> éléments, en % massique)
et groups_data.lua (groupes + sous-groupes du menu de craft).

Règles :
- name       : obligatoire, normalisé (minuscules, espaces -> "_"), unique
               sur l'ensemble des feuilles (les noms vanilla gardent leur tiret)
- level      : basic / advanced / experimental (vide = avertissement)
- kind       : resources, ore / rock / fluid / gas (fluid et gas -> type fluid)
- extraction : resources, fluid et gas seulement : deposit (défaut) / air
- vanilla    : resources, yes si la ressource existe déjà dans le jeu de base
- origin     : elements, natural / artificial
- type       : elements, item (défaut) / fluid
- stack_size : items seulement (100 par défaut)
- associated_with : resources, noms séparés par ";" (gisements mixtes)
- ing_i / qty_i   : alliages, jusqu'à 4 ingrédients
- base       : materials, doit exister dans elements ou alloys
- l'ordre des lignes dans le tableur devient le champ `order` en jeu
"""
import sys
from collections import defaultdict
from pathlib import Path

from openpyxl import load_workbook

LEVELS = ["basic", "advanced", "experimental"]
DEFAULT_STACK = 100
MAX_ALLOY_PARTS = 4

ENUMS = {
    "kind": {"ore", "rock", "fluid", "gas"},
    "extraction": {"deposit", "air"},
    "vanilla": {"yes", "no"},
    "origin": {"natural", "artificial"},
    "type": {"item", "fluid"},
}

SHEETS = {
    "resources": {
        "form": "ore", "file": "resources_data.lua", "kind": "items",
        "columns": ["name", "kind", "level", "extraction", "vanilla",
                    "stack_size", "associated_with", "name_en", "name_fr"],
    },
    "elements": {
        "form": "material", "file": "elements_data.lua", "kind": "items",
        "columns": ["name", "symbol", "atomic", "origin", "type", "level",
                    "stack_size", "name_en", "name_fr"],
    },
    "alloys": {
        "form": "material", "file": "alloys_data.lua", "kind": "items",
        "columns": ["name", "level", "stack_size"]
                   + [f"{p}_{i}" for i in range(1, MAX_ALLOY_PARTS + 1)
                      for p in ("ing", "qty")]
                   + ["name_en", "name_fr"],
    },
    "materials": {
        "form": "material", "file": "materials_data.lua", "kind": "items",
        "columns": ["name", "base", "level", "stack_size", "name_en", "name_fr"],
    },
    "components": {
        "form": "component", "file": "components_data.lua", "kind": "items",
        "columns": ["name", "level", "stack_size", "name_en", "name_fr"],
    },
    "composition": {
        "file": "composition_data.lua", "kind": "composition",
        "columns": ["resource", "element", "percent"],
    },
}
FORMS = ["ore", "material", "component"]

EMIT_ORDER = ["name", "form", "level", "subgroup", "order", "type", "kind",
              "extraction", "vanilla", "origin", "symbol", "atomic", "base",
              "associated_with", "ingredients", "stack_size", "name_en", "name_fr"]
TEXT_COLS = ("symbol", "name_en", "name_fr")


# --------------------------------------------------------------------------
# utilitaires
# --------------------------------------------------------------------------
def lua_str(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def lua_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, str):
        return lua_str(v)
    if isinstance(v, list):
        return "{ " + ", ".join(lua_value(x) for x in v) + " }"
    if isinstance(v, dict):
        return "{ " + ", ".join(f"{k} = {lua_value(x)}" for k, x in v.items()) + " }"
    raise TypeError(f"type non géré : {type(v)}")


def clean(value):
    """Cellule vide -> None, texte -> texte sans espaces autour."""
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        return value or None
    return value


def norm(value) -> str:
    return str(value).strip().lower().replace(" ", "_")


def to_number(value, label, where, errors, integer=False):
    if value is None:
        return None
    try:
        number = float(str(value).replace(",", ".")) if isinstance(value, str) else float(value)
        if integer and number != int(number):
            raise ValueError
        return int(number) if number == int(number) else number
    except (TypeError, ValueError):
        kind = "un entier" if integer else "un nombre"
        errors.append(f"{where} : '{label}' doit être {kind} (reçu : {value!r})")
        return None


def read_rows(ws, columns, sheet):
    header = [clean(c.value) for c in ws[1]]
    missing = [c for c in columns if c not in header]
    if missing:
        sys.exit(f"Feuille '{sheet}' : colonnes manquantes : {', '.join(missing)}")
    index = {name: header.index(name) for name in columns}

    for number, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        record = {c: clean(row[index[c]]) for c in columns}
        if all(v is None for v in record.values()):
            continue  # ligne vide
        yield number, record


# --------------------------------------------------------------------------
# lecture et validation
# --------------------------------------------------------------------------
def build_items(sheet, cfg, ws, seen, rank, errors, warnings):
    entries, no_level = [], []
    letters = "abcdefghij"

    for number, r in read_rows(ws, cfg["columns"], sheet):
        where = f"{sheet} ligne {number}"
        cols = cfg["columns"]

        if not r["name"]:
            errors.append(f"{where} : 'name' est vide")
            continue
        name = norm(r["name"])
        if name in seen:
            errors.append(f"{where} : doublon de '{name}' (déjà {seen[name]})")
            continue
        seen[name] = where

        entry = {"name": name, "form": cfg["form"]}
        bad = False

        # niveau
        level = norm(r["level"]) if r["level"] else None
        if level is None:
            no_level.append(number)
        elif level not in LEVELS:
            errors.append(f"{where} : level '{r['level']}' invalide ({' / '.join(LEVELS)})")
            bad = True
        else:
            entry["level"] = level
            entry["subgroup"] = f"{level}-{cfg['form']}"

        # colonnes à valeurs fixes
        values = {}
        for col in ENUMS:
            if col in cols and r[col] is not None:
                value = norm(r[col])
                if value not in ENUMS[col]:
                    errors.append(f"{where} : {col} '{r[col]}' invalide "
                                  f"({' / '.join(sorted(ENUMS[col]))})")
                    bad = True
                values[col] = value
        if bad:
            continue

        # type Factorio
        if "type" in cols:
            ftype = values.get("type", "item")
        elif "kind" in cols:
            if "kind" not in values:
                errors.append(f"{where} : 'kind' est vide")
                continue
            ftype = "fluid" if values["kind"] in ("fluid", "gas") else "item"
        else:
            ftype = "item"
        entry["type"] = ftype

        if "kind" in values:
            entry["kind"] = values["kind"]
            if values["kind"] in ("fluid", "gas"):
                entry["extraction"] = values.get("extraction", "deposit")
            elif "extraction" in values:
                errors.append(f"{where} : 'extraction' ne s'applique qu'aux fluid et gas")
                continue
        if "origin" in values:
            entry["origin"] = values["origin"]
        if values.get("vanilla") == "yes":
            entry["vanilla"] = True

        for col in TEXT_COLS:
            if col in cols and r[col] is not None:
                entry[col] = str(r[col])
        if "atomic" in cols:
            atomic = to_number(r["atomic"], "atomic", where, errors, integer=True)
            if atomic is not None:
                entry["atomic"] = atomic

        if "base" in cols and r["base"] is not None:
            entry["base"] = norm(r["base"])
        if "associated_with" in cols and r["associated_with"] is not None:
            entry["associated_with"] = [norm(x) for x in str(r["associated_with"]).split(";")
                                        if x.strip()]

        # alliages
        if "ing_1" in cols:
            parts = []
            for i in range(1, MAX_ALLOY_PARTS + 1):
                ing, qty = r[f"ing_{i}"], r[f"qty_{i}"]
                if ing is None and qty is None:
                    continue
                if ing is None:
                    errors.append(f"{where} : qty_{i} sans ing_{i}")
                    continue
                part = {"name": norm(ing)}
                amount = to_number(qty, f"qty_{i}", where, errors)
                if amount is None and qty is None:
                    warnings.append(f"{where} : ing_{i} '{ing}' sans quantité")
                elif amount is not None:
                    part["amount"] = amount
                parts.append(part)
            if parts:
                entry["ingredients"] = parts

        # pile
        if "stack_size" in cols and ftype == "item":
            stack = to_number(r["stack_size"], "stack_size", where, errors, integer=True)
            entry["stack_size"] = stack if stack is not None else DEFAULT_STACK

        entry["order"] = f"{letters[rank]}-{len(entries) + 1:04d}"
        entry["_row"] = number
        entries.append(entry)

    if no_level:
        warnings.append(f"{sheet} : {len(no_level)} ligne(s) sans level "
                        f"(première : ligne {no_level[0]})")
    return entries


def build_composition(sheet, cfg, ws, errors):
    entries, pairs = [], {}
    for number, r in read_rows(ws, cfg["columns"], sheet):
        where = f"{sheet} ligne {number}"
        if not r["resource"] or not r["element"]:
            errors.append(f"{where} : 'resource' et 'element' sont obligatoires")
            continue
        percent = to_number(r["percent"], "percent", where, errors)
        if percent is None:
            if r["percent"] is None:
                errors.append(f"{where} : 'percent' est vide")
            continue
        if not 0 < percent <= 100:
            errors.append(f"{where} : percent {percent} hors de ]0 ; 100]")
            continue
        key = (norm(r["resource"]), norm(r["element"]))
        if key in pairs:
            errors.append(f"{where} : doublon {key[0]} / {key[1]} (déjà ligne {pairs[key]})")
            continue
        pairs[key] = number
        entries.append({"resource": key[0], "element": key[1],
                        "percent": percent, "_row": number})
    return entries


def check_references(tables, errors):
    def names(*sheets):
        return {e["name"] for s in sheets for e in tables[s]}

    resources, elements = names("resources"), names("elements")
    compounds = names("elements", "alloys")

    for e in tables["resources"]:
        for other in e.get("associated_with", []):
            if other not in resources:
                errors.append(f"resources ligne {e['_row']} : associated_with "
                              f"'{other}' absent de resources")
    for e in tables["alloys"]:
        for part in e.get("ingredients", []):
            if part["name"] not in compounds or part["name"] == e["name"]:
                errors.append(f"alloys ligne {e['_row']} : ingrédient "
                              f"'{part['name']}' absent de elements / alloys")
    for e in tables["materials"]:
        if "base" in e and e["base"] not in compounds:
            errors.append(f"materials ligne {e['_row']} : base '{e['base']}' "
                          f"absente de elements / alloys")

    totals = defaultdict(float)
    for e in tables["composition"]:
        if e["resource"] not in resources:
            errors.append(f"composition ligne {e['_row']} : resource "
                          f"'{e['resource']}' absente de resources")
        if e["element"] not in elements:
            errors.append(f"composition ligne {e['_row']} : element "
                          f"'{e['element']}' absent de elements")
        totals[e["resource"]] += e["percent"]
    for resource, total in totals.items():
        if total > 100.5:
            errors.append(f"composition : '{resource}' totalise {total:.2f} % (> 100)")


def build(wb):
    errors, warnings, seen, tables = [], [], {}, {}
    rank_in_form = defaultdict(int)

    for sheet, cfg in SHEETS.items():
        if cfg["kind"] == "items":
            rank = rank_in_form[cfg["form"]]
            rank_in_form[cfg["form"]] += 1
            tables[sheet] = build_items(sheet, cfg, wb[sheet], seen, rank, errors, warnings)
        else:
            tables[sheet] = build_composition(sheet, cfg, wb[sheet], errors)

    check_references(tables, errors)
    return tables, errors, warnings


# --------------------------------------------------------------------------
# écriture Lua
# --------------------------------------------------------------------------
def to_lua(entries, sheet) -> str:
    lines = [f"-- FICHIER GÉNÉRÉ par generate_elements.py ({sheet}) : "
             "ne pas modifier à la main", "return {"]
    for e in entries:
        keys = [k for k in EMIT_ORDER if k in e] if "name" in e else \
               [k for k in ("resource", "element", "percent") if k in e]
        fields = ", ".join(f"{k} = {lua_value(e[k])}" for k in keys)
        lines.append("    { " + fields + " },")
    lines.append("}")
    return "\n".join(lines) + "\n"


def groups_lua() -> str:
    letters = "abcdefghij"
    lines = ["-- FICHIER GÉNÉRÉ par generate_elements.py (groupes) : "
             "ne pas modifier à la main", "return {", "    groups = {"]
    for i, level in enumerate(LEVELS):
        lines.append(f'        {{ name = "{level}-processing", order = "{letters[i]}" }},')
    lines += ["    },", "    subgroups = {"]
    for level in LEVELS:
        for j, form in enumerate(FORMS):
            lines.append(f'        {{ name = "{level}-{form}", group = "{level}-processing", '
                         f'order = "{letters[j]}" }},')
    lines += ["    },", "}"]
    return "\n".join(lines) + "\n"


def main():
    source = Path(sys.argv[1] if len(sys.argv) > 1 else "elements.xlsx")
    out_dir = Path(sys.argv[2] if len(sys.argv) > 2 else ".")

    wb = load_workbook(source, data_only=True)
    absent = [s for s in SHEETS if s not in wb.sheetnames]
    if absent:
        sys.exit(f"Feuilles manquantes dans {source.name} : {', '.join(absent)}")

    tables, errors, warnings = build(wb)
    if errors:
        print("Erreurs, aucun fichier écrit :")
        for message in errors:
            print("  -", message)
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    for sheet, cfg in SHEETS.items():
        (out_dir / cfg["file"]).write_text(to_lua(tables[sheet], sheet), encoding="utf-8")
        print(f"{len(tables[sheet]):4d} lignes -> {cfg['file']}")
    (out_dir / "groups_data.lua").write_text(groups_lua(), encoding="utf-8")
    print("   3 groupes, 9 sous-groupes -> groups_data.lua")

    for message in warnings:
        print("Attention :", message)


if __name__ == "__main__":
    main()
