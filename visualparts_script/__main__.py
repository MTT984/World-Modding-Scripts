import os, json, subprocess

def nfsmsReplace(fileNm):
    return fileNm.replace('!car!', car).\
        replace('!style!', style).\
        replace('!vltNode!', vltNode).\
        replace('!partHash!', partHash).\
        replace('!baseCar!', basecar).\
        replace('!partName!', partName).\
        replace('!shortdesc!', shortdesc).\
        replace('!iconHood!', icons['hood']).\
        replace('!iconBk!', icons['bodykit']).\
        replace('!partTitle!', lang)

def xmlReplace(fileNml):
    return fileNml.replace('!partName!', partName).\
        replace('!partHash!', partHash).\
        replace('!style!', style).\
        replace('!iconHood!', icons['hood']).\
        replace('!iconBk!', icons['bodykit']).\
        replace('!priority!', str(100-styleN)).\
        replace('!partTitle!', lang)

txtData = "visualparts.txt"
workDir = os.path.dirname(os.path.abspath(__file__))
icons = {"hood":"", "spoiler":"", "bodykit":""}
templates = {}

with open('_nfsms_template.json', 'r') as F1: 
    templates['nfsms'] = json.load(F1)
    for _x in templates['nfsms']:
        templates['nfsms'][_x] = "".join(templates['nfsms'][_x])

with open('_xml_template.json', 'r') as F2: templates['xml'] = json.load(F2)
with open('visualparts.txt', 'r') as F3: partsList = F3.read().splitlines()

for _x in partsList:
    _xspl = _x.upper().split("_")   # 0=car, 1=style, 2=type
    car = _xspl[0]
    style = _xspl[1]
    partType = _xspl[2]
    partName = _x.upper()
    lang = 'GM_CATALOG_00009999'
    shortdesc = "CAR_MDL_" + car

    qh_exe = os.path.join(workDir, f"quickhashercli.exe bin-int:{_x} commerce:{_x.lower()} bin-int:{car}")
    qh_run = subprocess.run(qh_exe, stdout=subprocess.PIPE)
    qh_out = qh_run.stdout.decode("utf-8").split(" ")

    partHash = qh_out[0]
    vltNode = qh_out[1]
    basecar = qh_out[2]
    
    outFiles = {}
    outFiles['nfsms'] = os.path.join(workDir, car + "_visualparts.nfsms")
    outFiles['nfsms_bodykit'] = os.path.join(workDir, car + "_visualparts_bodykit.nfsms")
    outFiles['xml_hood'] = os.path.join(workDir, car + "_visualparts_catalogHood.xml")
    outFiles['xml_spoiler'] = os.path.join(workDir, car + "_visualparts_catalogSpoiler.xml")
    outFiles['xml_bodykit'] = os.path.join(workDir, car + "_visualparts_catalogBodykit.xml")

    if partType == 'HOOD':
        try: _xspl[3]; icons['hood'] = 'PART_HOOD_CF' 
        except: icons['hood'] = 'PART_HOOD'

        styleN = style.split('STYLE'); styleN = int(styleN[1])

        with open(outFiles['nfsms'], "a+") as outF1: outF1.write(nfsmsReplace(templates['nfsms']['hood']))
        with open(outFiles['xml_hood'], "a+") as outF2: outF2.write(xmlReplace(templates['xml']['hood']))

    elif partType == 'SPOILER':
        styleN = style.split('STYLE'); styleN = int(styleN[1])

        with open(outFiles['nfsms'], "a+") as outF1: outF1.write(nfsmsReplace(templates['nfsms']['spoiler']))
        with open(outFiles['xml_spoiler'], "a+") as outF2: outF2.write(xmlReplace(templates['xml']['spoiler']))

    elif partType == 'INTEGRATED':
        if style.__contains__('KITW'):
            icons['bodykit'] = 'VP_BST3_WOH'
            styleN = style.split('KITW'); styleN = int(styleN[1])
        else:
            icons['bodykit'] = 'VP_BST1_WOH'
            styleN = style.split('KIT'); styleN = int(styleN[1])

        with open(outFiles['nfsms_bodykit'], "a+") as outF1: outF1.write(nfsmsReplace(templates['nfsms']['bodykit']))
        with open(outFiles['xml_bodykit'], "a+") as outF2: outF2.write(xmlReplace(templates['xml']['bodykit']))