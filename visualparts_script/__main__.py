import os, json, subprocess

def nfsmsReplace(newFile):
    return newFile.replace('!car!', car).\
        replace('!style!', style).\
        replace('!vltNode!', vltNode).\
        replace('!partHash!', partHash).\
        replace('!baseCar!', basecar).\
        replace('!partName!', partName).\
        replace('!shortdesc!', shortdesc).\
        replace('!icon!', icon).\
        replace('!partTitle!', lang)

def xmlReplace(newFile):
    return newFile.replace('!partName!', partName).\
        replace('!partHash!', partHash).\
        replace('!style!', style).\
        replace('!icon!', icon).\
        replace('!priority!', str(100-styleN)).\
        replace('!partTitle!', lang)

def logInfo():
    print(f"CAR: {car} - PART: {partName}")

txtData = "visualparts.txt"
workDir = os.path.dirname(os.path.abspath(__file__))
savedDir = os.path.join(workDir, 'saved')
if not os.path.exists(savedDir): os.makedirs(savedDir)
templates = {}

with open('_nfsms_template.json', 'r') as F1: 
    templates['nfsms'] = json.load(F1)
    for _x in templates['nfsms']:
        templates['nfsms'][_x] = "".join(templates['nfsms'][_x])

with open('_xml_template.json', 'r') as F2: templates['xml'] = json.load(F2)
with open('visualparts.txt', 'r') as F3: partsList = F3.read().splitlines()

for _x in partsList:
    _x = _x.upper()
    icon = ""

    pos = len(_x)
    for sub in ["_KIT", "_BASE", "_STYLE"]:
        sub_pos = _x.find(sub)
        if sub_pos >= 0 and sub_pos < pos:
            pos = sub_pos

    _xspl = [_x[:pos], (_x[pos:])[1:]]
    car = _xspl[0]

    _xspl = _xspl[1].split("_")
    style = _xspl[0]
    partType = _xspl[1]
    try: partType2 = _xspl[2]
    except: partType2 = None
    partName = _x.upper()
    lang = style
    shortdesc = "CAR_MDL_" + car

    qh_exe = os.path.join(workDir, f"quickhashercli.exe bin-int:{_x} commerce:{_x} bin-int:{car}")
    qh_run = subprocess.run(qh_exe, stdout=subprocess.PIPE)
    qh_out = qh_run.stdout.decode("utf-8").split(" ")

    partHash = qh_out[0]
    vltNode = qh_out[1]
    basecar = qh_out[2]
    
    outFiles = {}
    outFiles['nfsms'] = os.path.join(savedDir, car + "_visualparts.nfsms")
    outFiles['nfsms_bodykit'] = os.path.join(savedDir, car + "_visualparts_bodykit.nfsms")
    outFiles['nfsms_wheel'] = os.path.join(savedDir, car + "_visualparts_wheel.nfsms")
    outFiles['xml_hood'] = os.path.join(savedDir, car + "_visualparts_catalogHood.xml")
    outFiles['xml_spoiler'] = os.path.join(savedDir, car + "_visualparts_catalogSpoiler.xml")
    outFiles['xml_bodykit'] = os.path.join(savedDir, car + "_visualparts_catalogBodykit.xml")
    outFiles['xml_wheel'] = os.path.join(savedDir, car + "_visualparts_catalogWheel.xml")

    if partType == 'HOOD':
        if partType2 == 'CF': icon = 'PART_HOOD_CF'
        else: icon = 'PART_HOOD'

        styleN = style.split('STYLE'); styleN = int(styleN[1])

        with open(outFiles['nfsms'], "a+") as outF1: outF1.write(nfsmsReplace(templates['nfsms']['hood']))
        with open(outFiles['xml_hood'], "a+") as outF2: outF2.write(xmlReplace(templates['xml']['hood']))

    elif partType == 'SPOILER':
        icon = "PART_SPOILER_CUST"
        styleN = style.split('STYLE'); styleN = int(styleN[1])

        with open(outFiles['nfsms'], "a+") as outF1: outF1.write(nfsmsReplace(templates['nfsms']['spoiler']))
        with open(outFiles['xml_spoiler'], "a+") as outF2: outF2.write(xmlReplace(templates['xml']['spoiler']))

    elif partType == 'INTEGRATED':
        if style.__contains__('KITW'):
            icon = 'VP_BST3_WOH'
            styleN = style.split('KITW'); styleN = int(styleN[1])
        else:
            icon = 'VP_BST1_WOH'
            styleN = style.split('KIT'); styleN = int(styleN[1])

        with open(outFiles['nfsms_bodykit'], "a+") as outF1: outF1.write(nfsmsReplace(templates['nfsms']['bodykit']))
        with open(outFiles['xml_bodykit'], "a+") as outF2: outF2.write(xmlReplace(templates['xml']['bodykit']))
    
    elif partType == 'FRONT' and partType2 == 'TIRE':
        icon = 'PART_RI_CUST'
        styleN = style.split('STYLE'); styleN = int(styleN[1])

        with open(outFiles['nfsms_wheel'], "a+") as outF1: outF1.write(nfsmsReplace(templates['nfsms']['wheel']))
        with open(outFiles['xml_wheel'], "a+") as outF2: outF2.write(xmlReplace(templates['xml']['wheel']))
    
    logInfo()
