 Соберите setup.exe


Команда (из папки srs_setup, где лежат setup.py и WebShortcutCreator.ico):

cmd
pyinstaller --onefile --windowed --icon="WebShortcutCreator.ico" --add-data "..\shortcut_host;shortcut_host" setup.py
Пояснение:

--onefile – один EXE.

--windowed – без консоли (GUI).

--icon – иконка для EXE.

--add-data "..\shortcut_host;shortcut_host" – встроить папку shortcut_host (находящуюся на уровень выше) в EXE.

После сборки готовый setup.exe появится в папке dist.