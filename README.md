A little script for adding a filename of an dxf file
to the modelspace of that file. It is usefull for lasercutting purposes for
marking  parts after cutting. 
Original ezdxf module by Manfred Moitzi support for
DXF versions: R12, R2000, R2004, R2007, R2010, R2013 and R2018
Other versions may be working unstable.
Always use that script only on copies of a original files and
check dimensions before cut parts on a laser machine.

Installation:

pip install ezdxf==0.17b0

How to use:
Prepare a folder with a copies of files to be processed.
Put a script 'Filenamer.py' in it. Run script. Enjoy results.



Утилита для проставления наименования детали на файл детали
в формате dxf для последующего нанесения на саму деталь гравировкой.
Имя детали берется из названия файла детали. Модуль ezdxf, который
для этой задачи используется поддерживает форматы dxf файлов в версиях
R12, R2000, R2004, R2007, R2010, R2013 и R2018. С остальными версиями
работа не гарантируется. Сами файлы могут быть при этом повреждены.
Так что работайте, пожалуйста, с копиями оригинальных файлов и контролируйте
размеры, прежде чем отправлять что либо на станок.

Требуется установить пакет ezdxf версии 0.17:

pip install ezdxf==0.17b0

Запуск:
Подготовьте папку с копиями файлов, подлежащих обработке.
Поместите в неё скрипт, запустите и наслаждайтесь.
После обработки необходимо будет отмасштабировать надпись в вашей
управляющей станком программе, присвоить ей режим обработки гравировкой
и поместить надпись на саму деталь.