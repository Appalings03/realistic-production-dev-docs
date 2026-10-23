-- FICHIER GÉNÉRÉ par generate_elements.py (groupes) : ne pas modifier à la main
return {
    groups = {
        { name = "basic-processing", order = "a" },
        { name = "advanced-processing", order = "b" },
        { name = "experimental-processing", order = "c" },
    },
    subgroups = {
        { name = "basic-ore", group = "basic-processing", order = "a" },
        { name = "basic-material", group = "basic-processing", order = "b" },
        { name = "basic-component", group = "basic-processing", order = "c" },
        { name = "advanced-ore", group = "advanced-processing", order = "a" },
        { name = "advanced-material", group = "advanced-processing", order = "b" },
        { name = "advanced-component", group = "advanced-processing", order = "c" },
        { name = "experimental-ore", group = "experimental-processing", order = "a" },
        { name = "experimental-material", group = "experimental-processing", order = "b" },
        { name = "experimental-component", group = "experimental-processing", order = "c" },
    },
}
