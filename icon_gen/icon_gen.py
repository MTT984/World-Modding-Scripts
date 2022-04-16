"""
Script para geração automatica de thumbnails(icones) de vinyl para o NFS World

- Requisitos: Python3, modulo Pillow(PIL) e imagemagick instalado e adicionado ao PATH do Windows
- Uso: Ao iniciar o script, ele ira pedir o local da pasta onde esta localizado os vinyls,
basta colar/escrever o local correto (evitar usar pastas com espaço no nome, trocar por - ou _)

- O Padrão da pasta/arquivos do vinyl deve ser:
    - Pasta com nome do vinyl (ex: ADDON_PETRONAS, ADDON_AMG)
    - Dentro da pasta deve ter os layers do vinyl em PNG (ex: petronas_0.png, petronas_1.png/amg_0.png...)
    - O NOME DOS PNGs DEVE CONTER "_0.png, _1.png, _2.png ou _3.png" NO FINAL DO NOME. De acordo com o numero de layers que o vinyl tiver
    - Vinyl com 1 layer deve ter um arquivo "xxxx_0.png", 2 layers = arquivos [xxxx_0.png, xxxxx_1.png]

- exemplo de um padrão VALIDO:
    - Pasta: ADDON_PETRONAS / ADDON_AMG / ADDON_REDBULL_LOGO
    - Arquivos: petronas_0.png / PETRONAS_0.png / vinyl_0.png / petronas_vinyl_0.png / petronas_1.png / aaaaa_0.png / 123456_1.png

- exemplo de um padrão INVALIDO:
    - Pasta: vinyl petronas / petronas / addon-petronas / addon amg
    - Arquivos: petronas-1.png, petronas-2.png / petronas 0.png, petronas 1.png / petronas0.png, petronas2.png / amg_01.png / vinyl_00.png
"""

import os
from PIL import Image

def colorReplace(PNGname, newColor, iconFile):
    png = Image.open(path + "\\" + PNGname)
    wx, hx = png.size

    for x in range(wx):
        for y in range(hx):
            px = png.load()
            current_color = (px[x, y])
            if current_color != (0, 0, 0, 0):
                png.putpixel((x,y), newColor)

    png.save(path + "\\" + iconFile)
    print('Saving: ' + iconFile)

path = input("PNGs folder: ")
vinyl_name = path.split("\\"); vinyl_name = vinyl_name[-1]
print(vinyl_name)
path_files = os.listdir(path)

png_qtd = 0; png_files = []
blue_shades = [(4, 66, 79, 255), (50, 102, 116, 255), (89, 140, 154, 255), (128, 180, 195, 255)]

for x in path_files:
    if x.__contains__('_0.png'): png_files.append(x); png_qtd += 1
    elif x.__contains__('_1.png'): png_files.append(x); png_qtd += 1
    elif x.__contains__('_2.png'): png_files.append(x); png_qtd += 1
    elif x.__contains__('_3.png'): png_files.append(x); png_qtd += 1

if png_qtd == 1:
    colorReplace(png_files[0], blue_shades[0], 'icon_a.png')

    # INDEX [0]=.dds file / [1]=icon_a.png
    newDirFiles = [path + '\\' + vinyl_name + '.dds', path + '\\icon_a.png']

    ddsMergeCMD = "magick -background none " + newDirFiles[1] + " -layers flatten -resize 128x128 -define dds:compression:DXT5 " + newDirFiles[0]
    os.system(ddsMergeCMD)
    os.system('del ' + path + '\\icon_*')

elif png_qtd == 2:
    colorReplace(png_files[0], blue_shades[0], 'icon_a.png')
    colorReplace(png_files[1], blue_shades[3], 'icon_b.png')

    # INDEX [0]=.dds file / [1]=icon_a.png / [2]=icon_b.png
    newDirFiles = [path + '\\' + vinyl_name + '.dds', path + '\\icon_a.png', path + '\\icon_b.png']

    ddsMergeCMD = "magick -background none " + newDirFiles[1] + " " + newDirFiles[2] + " -layers flatten -resize 128x128 -define dds:compression:DXT5 " + newDirFiles[0]
    os.system(ddsMergeCMD)
    os.system('del ' + path + '\\icon_*')

elif png_qtd == 3:
    colorReplace(png_files[0], blue_shades[0], 'icon_a.png')
    colorReplace(png_files[1], blue_shades[1], 'icon_b.png')
    colorReplace(png_files[2], blue_shades[2], 'icon_c.png')

    # INDEX [0]=.dds file / [1]=icon_a.png / [2]=icon_b.png / [3]=icon_c.png
    newDirFiles = [path + '\\' + vinyl_name + '.dds', path + '\\icon_a.png', path + '\\icon_b.png', path + '\\icon_c.png']

    ddsMergeCMD = "magick -background none " + newDirFiles[1] + " " + newDirFiles[2] + " " + newDirFiles[3] + " -layers flatten -resize 128x128 -define dds:compression:DXT5 " + newDirFiles[0]
    os.system(ddsMergeCMD)
    os.system('del ' + path + '\\icon_*')

elif png_qtd == 4:
    colorReplace(png_files[0], blue_shades[0], 'icon_a.png')
    colorReplace(png_files[1], blue_shades[1], 'icon_b.png')
    colorReplace(png_files[2], blue_shades[2], 'icon_c.png')
    colorReplace(png_files[3], blue_shades[3], 'icon_d.png')
    
    # INDEX [0]=.dds file / [1]=icon_a.png / [2]=icon_b.png / [3]=icon_c.png / [4]=icon_d.png
    newDirFiles = [path + '\\' + vinyl_name + '.dds', path + '\\icon_a.png', path + '\\icon_b.png', path + '\\icon_c.png', path + '\\icon_d.png']

    ddsMergeCMD = "magick -background none " + newDirFiles[1] + " " + newDirFiles[2] + " " + newDirFiles[3] + " " + newDirFiles[4] + " -layers flatten -resize 128x128 -define dds:compression:DXT5 " + newDirFiles[0]
    os.system(ddsMergeCMD)
    os.system('del ' + path + '\\icon_*')