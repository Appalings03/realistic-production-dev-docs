--[[

Setting Types Explained:

• startup: Applied before the game loads prototypes. Requires restarting Factorio if changed. Access it via settings.startup["my-mod-enable-feature"].value.
• runtime-global: Applies to the whole save and can be changed during gameplay by any player (or admin in multiplayer). Access it via settings.global["my-mod-enable-feature"].value in control.lua.
• runtime-per-user: Varies per player in multiplayer games. Access it via settings.player["my-mod-enable-feature"].value in control.lua


2. Read the setting value in your code

Depending on which setting_type you chose, read the .value property in the appropriate lifecycle file:
• In data.lua (for startup settings):lua

    local feature_enabled = settings.startup["my-mod-enable-feature"].value
    if feature_enabled then
    -- Modify prototypes or recipes here
    end

Utilisez le code avec précaution.
• In control.lua (for runtime-global or runtime-per-user settings):lua

    script.on_event(defines.events.on_tick, function(event)
    local is_enabled = settings.global["my-mod-enable-feature"].value
    if is_enabled then
        -- Run runtime logic
    end
    end)

]]


local order = {
    type = "string-setting",
    name = "RM-stp-order",
    order = "cgp-c-b",
    setting_type = "startup",
    default_value = "aw",
    allowed_values = {"aw", "dw"},
}

local bool = {
    type = "bool-setting",
    name = "my-mod-enable-feature",
    setting_type = "startup", -- Choose: "startup", "runtime-global", or "runtime-per-user"
    default_value = true,
    per_user = false,
    localised_name = "Enable My Feature",
    localised_description = "Turns the custom feature on or off."
}


data:extend({
    order,
    bool,
})