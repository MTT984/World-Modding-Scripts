import os

def binhash(string):
    val = 0xFFFFFFFF
    for c in string:
        val = val * 33 + ord(c)
    return val & 0xFFFFFFFF

def nfsmsReplace(fileNm):
    return fileNm.replace('!car!', car).\
        replace('!style!', style).\
        replace('!vltNode!', vltNode).\
        replace('!partHash!', partHash).\
        replace('!baseCar!', baseCar).\
        replace('!partName!', partName).\
        replace('!shortdesc!', shortdesc).\
        replace('!iconHood!', iconHood).\
        replace('!iconBk!', iconBk).\
        replace('!partTitle!', lang)

def xmlReplace(fileNml):
    return fileNml.replace('!partName!', partName).\
        replace('!partHash!', partHash).\
        replace('!style!', style).\
        replace('!iconHood!', iconHood).\
        replace('!iconBk!', iconBk).\
        replace('!priority!', str(100-styleN)).\
        replace('!partTitle!', lang)

txtData = "visualparts.txt"
iconBk = ""
iconHood = ""

tmpltHood = ['\n# HOOD - !car! !style!\n\
copy_node visualpart 0x11a0c2aa !vltNode!\ncopy_node virtualitem 0x11a0c2aa !vltNode!\n\n\
update_field visualpart !vltNode! visualPartHash !partHash!\n\
update_field visualpart !vltNode! baseCarHashes[0] !baseCar!\n\n\
update_field virtualitem !vltNode! hash !partHash!\n\
update_field virtualitem !vltNode! itemName !partName!\n\
update_field virtualitem !vltNode! shortdescription !shortdesc!\n\
update_field virtualitem !vltNode! title !partTitle!\n\
update_field virtualitem !vltNode! icon !iconHood!\n\
##################################################################################',
'<ProductTrans><BundleItems i:nil="true"/><CategoryId i:nil="true"/><Currency>CASH</Currency><Description>!partName!</Description>\
<Hash>!partHash!</Hash><Icon>!iconHood!</Icon><Level>0</Level><LongDescription/><Price>0</Price><Priority>!priority!</Priority><ProductId>SRV-HOOD!partHash!</ProductId>\
<ProductTitle>!partTitle!</ProductTitle><ProductType>VISUALPART</ProductType><SecondaryIcon/><UseCount>1</UseCount><VisualStyle/><WebIcon/><WebLocation/></ProductTrans>\n']

tmpltSpoiler = ['\n# SPOILER - !car! !style!\n\
copy_node visualpart 0x11a0c2aa !vltNode!\ncopy_node virtualitem 0x450147aa !vltNode!\n\n\
update_field visualpart !vltNode! visualPartHash !partHash!\n\
update_field visualpart !vltNode! baseCarHashes[0] !baseCar!\n\n\
update_field virtualitem !vltNode! hash !partHash!\n\
update_field virtualitem !vltNode! itemName !partName!\n\
update_field virtualitem !vltNode! shortdescription !shortdesc!\n\
update_field virtualitem !vltNode! icon PART_SPOILER_CUST\n\
##################################################################################',
'<ProductTrans><BundleItems i:nil="true"/><CategoryId i:nil="true"/><Currency>CASH</Currency><Description>!partName!</Description><Hash>!partHash!</Hash><Icon>PART_SPOILER_CUST</Icon>\
<Level>0</Level><LongDescription/><Price>0</Price><Priority>!priority!</Priority><ProductId>SRV-SPOILER!partHash!</ProductId>\<ProductTitle>!partTitle!</ProductTitle>\
<ProductType>VISUALPART</ProductType><SecondaryIcon/><UseCount>1</UseCount><VisualStyle/><WebIcon/><WebLocation/></ProductTrans>\n']

tmplBodykit = ['\n# BODYKIT - !car! !style!\n\
copy_node visualpart 0x1fb0a35e !vltNode!\ncopy_node virtualitem 0x1ff8d934 !vltNode!\n\n\
update_field visualpart !vltNode! visualPartHash !partHash!\n\
update_field visualpart !vltNode! baseCarHashes[0] !baseCar!\n\n\
update_field virtualitem !vltNode! hash !partHash!\n\
update_field virtualitem !vltNode! itemName !partName!\n\
update_field virtualitem !vltNode! shortdescription !shortdesc!\n\
update_field virtualitem !vltNode! title !partTitle!\n\
update_field virtualitem !vltNode! icon !iconBk!\n\
update_field virtualitem !vltNode! type visualpart\n\
update_field virtualitem !vltNode! subType vpart_bodykit\n\
##################################################################################',
'<ProductTrans><BundleItems i:nil="true"/><CategoryId i:nil="true"/><Currency>CASH</Currency><Description>!partName!</Description><Hash>!partHash!</Hash><Icon>!iconBk!</Icon><Level>1</Level>\
<LongDescription/><Price>0</Price><Priority>!priority!</Priority><ProductId>SRV-BODY!partHash!</ProductId><ProductTitle>!partTitle!</ProductTitle><ProductType>VISUALPART</ProductType><SecondaryIcon/>\
<UseCount>1</UseCount><VisualStyle/><WebIcon/><WebLocation/></ProductTrans>\n']

with open(txtData, "r+") as hashFile:
    hashFileDmp = hashFile.read().splitlines()
    hashFile.close()

for _x in hashFileDmp:
    lineData = _x.split(" / ")

    partName = lineData[0].upper()
    partNameSpl = partName.split("_")
    car = partNameSpl[0]; style = partNameSpl[1]; partType = partNameSpl[2]
    
    try: lang = lineData[3]
    except: lang = partName
    
    if lang.startswith("-"):
        try: lang = lineData[4]
        except: lang = partName

    if lang == partName:
        lang = 'GM_CATALOG_00009999'
    else:
        lang = '"' + lang + '"'

    print(lang)

    partHash = lineData[2]
    vltNode = lineData[1].lower()
    baseCar = str(binhash(car))
    shortdesc = "CAR_MDL_" + car
    
    fileName_nfsms = [car + "_visualparts.nfsms", car + "_visualparts_bodykit.nfsms"]
    fileName_xml = [car + "_visualparts_catalogHood.xml", car + "_visualparts_catalogSpoiler.xml", car + "_visualparts_catalogBodykit.xml"]
            
    if partType == 'HOOD':
        try: partNameSpl[3]; iconHood = 'PART_HOOD_CF' 
        except: iconHood = 'PART_HOOD'
        styleN = style.split('STYLE'); styleN = int(styleN[1])

        with open(fileName_nfsms[0], "a+") as nfsmsOutFile:
            nfsmsOutFile.write(nfsmsReplace(tmpltHood[0]))

        with open(fileName_xml[0], "a+") as xmlOutFile:
            xmlOutFile.write(xmlReplace(tmpltHood[1]))

    elif partType == 'SPOILER':
        styleN = style.split('STYLE'); styleN = int(styleN[1])

        with open(fileName_nfsms[0], "a+") as nfsmsOutFile:
            nfsmsOutFile.write(nfsmsReplace(tmpltSpoiler[0]))

        with open(fileName_xml[1], "a+") as xmlOutFile:
            xmlOutFile.write(xmlReplace(tmpltSpoiler[1]))

    elif partType == 'INTEGRATED':
        if style.__contains__('KITW'):
            iconBk = 'VP_BST3_WOH'
            styleN = style.split('KITW'); styleN = int(styleN[1])
        else:
            iconBk = 'VP_BST1_WOH'
            styleN = style.split('KIT'); styleN = int(styleN[1])

        with open(fileName_nfsms[1], "a+") as nfsmsOutFile2:
            nfsmsOutFile2.write(nfsmsReplace(tmplBodykit[0]))

        with open(fileName_xml[2], "a+") as xmlOutFile2:
            xmlOutFile2.write(xmlReplace(tmplBodykit[1]))
