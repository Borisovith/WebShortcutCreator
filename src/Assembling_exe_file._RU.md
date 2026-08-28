Скомпилировать Python-скрипт (make_shortcut.py) в один самостоятельный файл .exe (чтобы избавиться от необходимости ставить Python и Pillow на других ПК) можно с помощью библиотеки PyInstaller.

Ниже инструкция, как превратить ваш Native Host в один автономный исполняемый файл.

Шаг 1. Установка PyInstaller
Откройте PowerShell от имени администратора и установите PyInstaller:

pip install pyinstaller

Шаг 2. Сборка .exe файла
Откройте PowerShell  и запустите сборку в один файл без консольного окна:

cd C:\Tools\shortcut_host
pyinstaller --onefile --noconsole make_shortcut.py

--onefile — упаковывает сам интерпретатор Python, все зависимости (Pillow) и ваш код в один единственный файл make_shortcut.exe.
--noconsole — отключает всплывающее черное окно консоли при вызове из Chrome.

После завершения компиляции готовый файл появится в созданной папке C:\Tools\shortcut_host\dist\make_shortcut.exe.

Шаг 3. Перенос .exe и обновление манифеста
Скопируйте файл make_shortcut.exe из папки dist прямо в корень C:\Tools\shortcut_host\.Папки build, dist и файл make_shortcut.spec после этого можно удалить.

В файле com.shortcut.creator.json измените путь с .bat на ваш новый .exe:

{
  "name": "com.shortcut.creator",
  "description": "Desktop Shortcut Creator Native Host",
  "path": "C:\\Tools\\shortcut_host\\make_shortcut.exe",
  "type": "stdio",
  "allowed_origins": [
    "chrome-extension://EXTENSION_ID/"
  ]
}

Шаг 4. Корректировка register.reg
Запустите файл register.reg (или убедитесь, что в реестре путь указывает на обновленный com.shortcut.creator.json).

Теперь ваш Native Messaging Host работает полностью автономно — файл run.bat, установленный Python и библиотека Pillow на целевом ПК больше не нужны.