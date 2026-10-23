-- file: verify_prototypes.lua
-- Usage: lua verify_prototypes.lua

local lfs = require("lfs") -- LuaFileSystem for directory scanning

-- Directory where your prototype files are
local PROTOTYPE_DIR = "C:/Users/marti/OneDrive/Documents/Scripts/Factorio Modding/realistic_production/realistic_production_ore/prototypes"

-- Table to collect all prototypes
local all_prototypes = {}
local name_set = {}

-- Helper to validate a single prototype
local function validate_prototype(p)
    local errors = {}

    if type(p) ~= "table" then
        table.insert(errors, "Prototype is not a table")
        return errors
    end
    if type(p.name) ~= "string" then
        table.insert(errors, "Missing or invalid 'name'")
    elseif name_set[p.name] then
        table.insert(errors, "Duplicate name: " .. p.name)
    else
        name_set[p.name] = true
    end
    if type(p.type) ~= "string" then
        table.insert(errors, "Missing or invalid 'type'")
    end
    return errors
end

-- Load all .lua files in the directory
for file in lfs.dir(PROTOTYPE_DIR) do
    if file:match("%.lua$") then
        local path = PROTOTYPE_DIR .. "/" .. file
        local ok, result = pcall(dofile, path)
        if not ok then
            print("Error loading " .. file .. ": " .. result)
        else
            -- Expect result to be a table of prototypes
            if type(result) == "table" then
                for _, proto in ipairs(result) do
                    table.insert(all_prototypes, proto)
                end
            end
        end
    end
end

-- Validate all prototypes
local error_count = 0
for _, proto in ipairs(all_prototypes) do
    local errs = validate_prototype(proto)
    if #errs > 0 then
        error_count = error_count + 1
        print("Errors in prototype '" .. (proto.name or "<unknown>") .. "':")
        for _, e in ipairs(errs) do
            print("  - " .. e)
        end
    end
end

if error_count == 0 then
    print("All prototypes look good!")
else
    print("Found " .. error_count .. " prototype(s) with errors.")
end
