# Script para o Blender para carros convertidos para o NFS World 
# que renomeia o nome das MESH, e cria um arquivo xxx_blender.txt equivalente ao arquivo .txt do CTK
# já com as PARTS organizadas e tambem MARKERS e MATERIALS atribuidos, se estiver com o nome dentro do padrão

# PARTS = qualquer MESH que inicie com "KIT/STYLE/BASE"
# MATERIALS = materials devem ter o nome no padrão "SHADER+_TEXTURE" para texturas dedicadas e "SHADER+TEXTURE" para texturas genericas
# MARKERS = qualquer MESH que começe com _ no nome

import bpy, os

def printf(data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=(data), type="OUTPUT")

# function values = (Marker_Name, Marker_Type, attachPart, RotA, RotB, RotC)
def marker_ln(mkrName, mkrType, attachPart, x, y, z):
    fs.write("MARKER %s %s %s %s %s %s %s\n" % (gamePrefix, mkrName, mkrType, attachPart,x,y,z) )

###################
# Script Variables
substr_zero = ".0"
gamePrefix = 'W'
###################

parts = []; materials = []; mkrArr = [] # Parts, Materials and Markers list

for obj in bpy.context.scene.objects:
    if obj.name.find(substr_zero) != -1:
        obj.name = obj.name[:-4]
        print(obj.name)

for mat in bpy.data.materials:
    if mat.name.find(substr_zero) != -1:
        mat.name = mat.name[:-4]
        print(mat.name)

for obj in bpy.data.objects:
    if obj.type == "EMPTY":
        if obj.name.startswith("+"):
            obj.name = obj.name.upper()
    elif obj.type != "EMPTY":
        view_check = obj.visible_get()
        if view_check == True:
            if obj.name.__contains__('#'):
                mixedName = obj.name.split('#')
                mixedName = mixedName[1]
                obj.data.name = mixedName
                print(mixedName)
                parts.append(mixedName)
            else:
                print(obj.name)
                obj.data.name = obj.name
                parts.append(obj.name)
            
 
for mat in bpy.data.materials: materials.append(mat.name)

parts.sort(); materials.sort() # Parts and Materials short by name

with open('G:\CarrosNFS\Blender Scripts\obj-mesh-rename_markers.txt', 'r+') as mkrList_file:
    mkrList = mkrList_file.read().splitlines()
    
for _x in mkrList:
    mkrArr.append(_x.split())

printf("####################################################")

with open(os.path.splitext(bpy.data.filepath)[0] + "_blender.txt", "w") as fs: # open CarName_blender.txt file
    for parts_x in parts:
        for _x in mkrArr:
            if parts_x.startswith(_x[0]):
                marker_ln(parts_x, _x[1], _x[2], _x[3], _x[4], _x[5])
                
        if parts_x.startswith("KIT") or parts_x.startswith("BASE") or parts_x.startswith("STYLE"): # KIT/BASE/STYLE parts
                fs.write("PART\tW\t" + parts_x + "\t\t" + parts_x + "\n")
            
    for mat_x in materials:
        if mat_x.__contains__('+') and mat_x.__contains__('+_'): # Materials with unique texture (CAR_BADGING, CAR_KIT00_HEADLIGHT_ON...)
            tmp_mat = mat_x.split('+')
            fs.write("MATERIAL\tW\t" + mat_x + "\t" + tmp_mat[0] + "\t%" + tmp_mat[1] + "\n")
            printf("Shader: %s / Texture: %s" % (tmp_mat[0],tmp_mat[1]) )

        elif mat_x.__contains__('+'): # Materials with generic textures (EXHAUST, BLACK, WINDOW_FRONT...)
            tmp_mat = mat_x.split('+')
            fs.write("MATERIAL\tW\t" + mat_x + "\t" + tmp_mat[0] + "\t" + tmp_mat[1] + "\n")
            printf("Shader: " + tmp_mat[0] + " / Texture: " + tmp_mat[1])

        else: # Materials with no std name
            fs.write("MATERIAL\tW\t" + mat_x + "\n")
