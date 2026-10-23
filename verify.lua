-- Usage: lua verify.lua [chemin vers le dossier realistic_production_ore]
-- Simule data:extend pour les definitions de prototypes et verifie leurs references.

local source = debug.getinfo(1, "S").source
local script_path = source:sub(1, 1) == "@" and source:sub(2) or source
local script_dir = script_path:match("^(.*)[/\\]") or "."
local mod_dir = (arg and arg[1]) or (script_dir .. "\\..\\realistic_production_ore")
local prototype_dir = mod_dir .. "\\prototypes"

local issues = {}
local registered_count = 0
local data = { raw = {} }

local function add_issue(source_file, prototype_name, message)
    issues[#issues + 1] = {
        source = source_file,
        prototype = prototype_name or "<fichier>",
        message = message,
    }
end

function data:extend(prototypes)
    if type(prototypes) ~= "table" then
        error("data:extend attend une table de prototypes")
    end

    for index, prototype in ipairs(prototypes) do
        if type(prototype) ~= "table" then
            error("prototype #" .. index .. " n'est pas une table")
        end
        if type(prototype.type) ~= "string" or prototype.type == "" then
            error("prototype #" .. index .. " n'a pas de type valide")
        end
        if type(prototype.name) ~= "string" or prototype.name == "" then
            error("prototype #" .. index .. " n'a pas de nom valide")
        end

        self.raw[prototype.type] = self.raw[prototype.type] or {}
        if self.raw[prototype.type][prototype.name] then
            error("doublon " .. prototype.type .. "/" .. prototype.name)
        end
        self.raw[prototype.type][prototype.name] = prototype
        registered_count = registered_count + 1
    end
end

local function load_file(relative_path)
    local full_path = prototype_dir .. "\\" .. relative_path
    local ok, result = pcall(dofile, full_path)
    if not ok then
        add_issue(relative_path, nil, "impossible de charger le fichier : " .. tostring(result))
        return nil
    end
    if type(result) ~= "table" then
        add_issue(relative_path, nil, "le fichier doit retourner une table")
        return nil
    end
    return result
end

local function register(prototype, source_file, display_name)
    local problems = {}

    if type(prototype) ~= "table" then
        add_issue(source_file, display_name, "la definition n'est pas une table")
        return false
    end
    if type(prototype.name) ~= "string" or prototype.name == "" then
        problems[#problems + 1] = "nom manquant ou invalide"
    end
    if type(prototype.type) ~= "string" or prototype.type == "" then
        problems[#problems + 1] = "type manquant ou invalide"
    elseif prototype.type ~= "item" and prototype.type ~= "fluid" then
        problems[#problems + 1] = "type non gere : " .. prototype.type
    end
    if prototype.type == "item" and
        (type(prototype.stack_size) ~= "number" or prototype.stack_size < 1 or prototype.stack_size % 1 ~= 0) then
        problems[#problems + 1] = "stack_size doit etre un entier positif pour un item"
    end
    if type(prototype.subgroup) ~= "string" or prototype.subgroup == "" then
        problems[#problems + 1] = "subgroup manquant ou invalide"
    end

    if #problems > 0 then
        for _, message in ipairs(problems) do
            add_issue(source_file, display_name, message)
        end
        return false
    end

    local ok, message = pcall(function()
        data:extend({ prototype })
    end)
    if not ok then
        add_issue(source_file, prototype.type .. "/" .. prototype.name, tostring(message))
        return false
    end
    return true
end

local function register_group(group, prototype_type, source_file, display_name)
    if type(group) ~= "table" or type(group.name) ~= "string" or group.name == "" then
        add_issue(source_file, display_name, "nom de groupe manquant ou invalide")
        return
    end
    local prototype = {
        type = prototype_type,
        name = group.name,
        order = group.order,
        group = group.group,
    }
    local ok, message = pcall(function()
        data:extend({ prototype })
    end)
    if not ok then
        add_issue(source_file, prototype_type .. "/" .. group.name, tostring(message))
    end
end

local groups = load_file("groups\\groups_data.lua")
local known_groups = {}
local known_subgroups = {}
if groups then
    if type(groups.groups) ~= "table" or type(groups.subgroups) ~= "table" then
        add_issue("groups\\groups_data.lua", nil, "les tables groups et subgroups sont requises")
    else
        for _, group in ipairs(groups.groups) do
            if type(group) == "table" and type(group.name) == "string" then
                known_groups[group.name] = true
            end
            register_group(group, "item-group", "groups\\groups_data.lua", "item-group")
        end
        for _, subgroup in ipairs(groups.subgroups) do
            if type(subgroup) == "table" and type(subgroup.name) == "string" then
                known_subgroups[subgroup.name] = subgroup.group
                if type(subgroup.group) ~= "string" or not known_groups[subgroup.group] then
                    add_issue("groups\\groups_data.lua", subgroup.name, "groupe parent inconnu : " .. tostring(subgroup.group))
                end
            end
            register_group(subgroup, "item-subgroup", "groups\\groups_data.lua", "item-subgroup")
        end
    end
end

local records = {}
local record_files = {
    { path = "resources\\resources_data.lua", type = "resources" },
    { path = "resources\\elements_data.lua", type = "elements" },
    { path = "materials\\alloys_data.lua", type = "alloys" },
    { path = "materials\\materials_data.lua", type = "materials" },
    { path = "components\\components_data.lua", type = "components" },
}

for _, file in ipairs(record_files) do
    local definitions = load_file(file.path)
    if definitions then
        for index, definition in ipairs(definitions) do
            local display_name = type(definition) == "table" and definition.name or ("entree #" .. index)
            records[#records + 1] = {
                definition = definition,
                source = file.path,
                category = file.type,
                display_name = display_name,
            }
            register(definition, file.path, display_name)
        end
    end
end

local known_names = {}
for _, record in ipairs(records) do
    local definition = record.definition
    if type(definition) == "table" and type(definition.name) == "string" then
        known_names[definition.name] = true
        if definition.subgroup and not known_subgroups[definition.subgroup] then
            add_issue(record.source, definition.name, "sous-groupe inconnu : " .. tostring(definition.subgroup))
        end
        if definition.associated_with then
            if type(definition.associated_with) ~= "table" then
                add_issue(record.source, definition.name, "associated_with doit etre une table")
            else
                for _, associated_name in ipairs(definition.associated_with) do
                    -- Les associations ne concernent que les ressources, verifiees plus bas.
                    if type(associated_name) ~= "string" then
                        add_issue(record.source, definition.name, "associated_with contient un nom invalide")
                    end
                end
            end
        end
        if record.category == "alloys" and definition.ingredients then
            if type(definition.ingredients) ~= "table" then
                add_issue(record.source, definition.name, "ingredients doit etre une table")
            else
                for _, ingredient in ipairs(definition.ingredients) do
                    if type(ingredient) ~= "table" or type(ingredient.name) ~= "string" then
                        add_issue(record.source, definition.name, "ingredient avec nom manquant ou invalide")
                    elseif type(ingredient.amount) ~= "number" or ingredient.amount <= 0 then
                        add_issue(record.source, definition.name, "quantite invalide pour l'ingredient " .. ingredient.name)
                    end
                end
            end
        end
    end
end

local known_resources = {}
for _, record in ipairs(records) do
    if record.category == "resources" and type(record.definition) == "table" and type(record.definition.name) == "string" then
        known_resources[record.definition.name] = true
    end
end

for _, record in ipairs(records) do
    local definition = record.definition
    if type(definition) == "table" and type(definition.name) == "string" then
        if type(definition.associated_with) == "table" then
            for _, associated_name in ipairs(definition.associated_with) do
                if type(associated_name) == "string" and not known_resources[associated_name] then
                    add_issue(record.source, definition.name, "ressource associee inconnue : " .. associated_name)
                end
            end
        end
        if record.category == "alloys" and type(definition.ingredients) == "table" then
            for _, ingredient in ipairs(definition.ingredients) do
                if type(ingredient) == "table" and type(ingredient.name) == "string" and not known_names[ingredient.name] then
                    add_issue(record.source, definition.name, "ingredient inconnu : " .. ingredient.name)
                end
            end
        end
    end
end

local composition = load_file("resources\\composition_data.lua")
if composition then
    for index, entry in ipairs(composition) do
        local display_name = type(entry) == "table" and entry.resource or ("entree #" .. index)
        if type(entry) ~= "table" then
            add_issue("resources\\composition_data.lua", display_name, "la composition n'est pas une table")
        else
            if type(entry.resource) ~= "string" or not known_resources[entry.resource] then
                add_issue("resources\\composition_data.lua", display_name, "ressource inconnue ou manquante")
            end
            if type(entry.element) ~= "string" or not known_names[entry.element] then
                add_issue("resources\\composition_data.lua", display_name, "element inconnu ou manquant : " .. tostring(entry.element))
            end
            if type(entry.percent) ~= "number" or entry.percent <= 0 then
                add_issue("resources\\composition_data.lua", display_name, "pourcentage invalide")
            end
        end
    end
end

print("Rapport de simulation du chargement des prototypes")
print("Dossier analyse : " .. prototype_dir)
print("Prototypes enregistres : " .. registered_count)
print("Problemes trouves : " .. #issues)

if #issues > 0 then
    for index, issue in ipairs(issues) do
        print(string.format(
            "%d. [%s] %s : %s",
            index,
            issue.source,
            tostring(issue.prototype),
            issue.message
        ))
    end
    os.exit(1)
end

print("Aucun probleme detecte.")
