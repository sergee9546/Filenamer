# Under the MIT License
# Copyright (c) 2021 Sergey Ivanov

from pathlib import Path
import os
import ezdxf
from ezdxf.math import Vec3
from ezdxf import path, zoom
from ezdxf.tools import fonts
from ezdxf.addons import text2path

# Настройки шрифта
Shrift = 'Arial'
SizeOfFont = 20.0

# Находим все dxf файлы, подлежащие обработке
PathFile = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.upper().endswith(".DXF"):
            PathFile.append(os.path.join(root, file))

fonts.load()

# Записываем в слой Name каждого файла его название.

for Path in PathFile:
    doc = ezdxf.readfile(Path)
    fonts.load()

# Проверка на наличие слоя с именем Name, если его нет, то будет создан
    if 'Name' in doc.layers:
        pass
    else:
        doc.layers.new('Name')

    msp = doc.modelspace()
    attr = {"layer": "Name", "color": 1}

# Задание шрифта

    ff = fonts.FontFace(family=Shrift)
    align = "LEFT"

# Выделяем из пути название файла
    s = str(Path.split('\\')[-1].upper().replace('.DXF', ''))


# Размеры детали
#    X_width = doc.header['$EXTMAX'][0]-doc.header['$EXTMIN'][0]
#    Y_Height = doc.header['$EXTMAX'][1]-doc.header['$EXTMIN'][1]

#  Координаты левого верхнего угла детали
    X = doc.header['$EXTMIN'][0]
    Y = doc.header['$EXTMAX'][1]

# Векторизация шрифта через полилинии. Параметр size определяет размер
    Z = text2path.make_path_from_str(
        s,
        ff,
        size=SizeOfFont,
        align=align
        )

# Z-Path Object
    N = path.render_polylines2d(msp, Z, dxfattribs=attr)
# N - entity Query Object

#  Создаем новый блок c именем "Nazvanie"
#  Если такой блок уже есть, файл дальше не обрабатывается.
#  Объект Z создается в точке с координатами (0,0,0),
#  поэтому базовая точка блока также нулевая
    if 'Nazvanie' not in doc.blocks:
        BLOCK = doc.blocks.new(name='Nazvanie', base_point=(0, 0))
    else:
        continue


#  При перемещении в блок объекты удаляются с чертежа.
#  Поэтому готовый блок надо сразу куда то вставить.

    for entity in N:
        msp.move_to_layout(entity, BLOCK)

    msp.add_blockref(
        BLOCK.name,
        insert=(X, Y+50),
        dxfattribs={
            "rotation": 0,   # Можно повернуть на угол или
            "xscale": 1.0,   # отмасштабировать
            "yscale": 1.0,
            },
            )

    zoom.extents(msp)
    doc.saveas(Path)
