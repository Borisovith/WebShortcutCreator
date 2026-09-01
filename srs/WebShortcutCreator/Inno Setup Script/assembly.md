Установите Inno Setup 6.7+
https://github.com/jrsoftware/issrc

Добавте в Inno Setup недостающие языковые пакеты из папки  Languages,
путь по умолчанию C:\Program Files (x86)\Inno Setup 6\Languages



Убедитесь, что в папке со скриптом лежат:
setup.iss (сам скрипт)
make_shortcut.exe
WebShortcutCreator.ico
WebShortcutCreator.bmp (164X314)
WebShortcutCreatorSmall.bmp (55X55)
Откройте setup.iss в Inno Setup и нажмите Compile (F9).
Готовый Setup.exe появится в той же папке.