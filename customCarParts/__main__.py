import os, json

def templateGen(outName, jsonDumpVar, v1):
    with open(outName, "w") as newFile:
        r = jsonDumpVar.replace("CARNAME", v1)
        print("Writing: " + outName)
        newFile.write(r)

templateFiles = [
    ("_templates\\vanilla.json", ".\\vanilla\\"),
    ("_templates\\expanded.json", ".\\expanded\\"),
    ("_templates\\reduced_1.json", ".\\reduced_1\\"),
    ("_templates\\reduced_2.json", ".\\reduced_2\\"),
    ("_templates\\preset_skins.json", ".\\PresetSkins\\"),
]

car = input("Car name: ").upper()

for templateFile, outDir in templateFiles:
        with open(templateFile) as f:
                jsonVar = json.load(f)

        outFile = outDir + car + ".json"
        jsonStr = json.dumps(jsonVar, indent=2)

        templateGen(outFile, jsonStr, car)