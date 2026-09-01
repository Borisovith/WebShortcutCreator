import sys
import json
import struct
import os
import base64
import io
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import ctypes
import winreg

# ---------- Мультиязычные сообщения (16 языков) ----------
MESSAGES = {
    'en': {
        'select_folder': 'Select folder',
        'select_folder_default': 'Select default folder',
        'select_folder_save': 'Select folder to save shortcut',
        'folder_unavailable': 'Folder unavailable',
        'folder_unavailable_msg': 'The selected folder is not available or write-protected:\n{path}\n\nPlease choose another folder.',
        'choose_available_folder': 'Choose available folder',
        'shortcut_saved': 'Shortcut saved to:',
        'error': 'Error'
    },
    'de': {
        'select_folder': 'Ordner auswählen',
        'select_folder_default': 'Standardordner auswählen',
        'select_folder_save': 'Ordner zum Speichern der Verknüpfung auswählen',
        'folder_unavailable': 'Ordner nicht verfügbar',
        'folder_unavailable_msg': 'Der ausgewählte Ordner ist nicht verfügbar oder schreibgeschützt:\n{path}\n\nBitte wählen Sie einen anderen Ordner.',
        'choose_available_folder': 'Verfügbaren Ordner auswählen',
        'shortcut_saved': 'Verknüpfung gespeichert unter:',
        'error': 'Fehler'
    },
    'fr': {
        'select_folder': 'Sélectionner un dossier',
        'select_folder_default': 'Sélectionner le dossier par défaut',
        'select_folder_save': 'Sélectionner le dossier pour enregistrer le raccourci',
        'folder_unavailable': 'Dossier indisponible',
        'folder_unavailable_msg': 'Le dossier sélectionné n\'est pas disponible ou est en lecture seule:\n{path}\n\nVeuillez choisir un autre dossier.',
        'choose_available_folder': 'Choisir un dossier disponible',
        'shortcut_saved': 'Raccourci enregistré dans :',
        'error': 'Erreur'
    },
    'it': {
        'select_folder': 'Seleziona cartella',
        'select_folder_default': 'Seleziona cartella predefinita',
        'select_folder_save': 'Seleziona cartella per salvare il collegamento',
        'folder_unavailable': 'Cartella non disponibile',
        'folder_unavailable_msg': 'La cartella selezionata non è disponibile o è protetta da scrittura:\n{path}\n\nScegli un\'altra cartella.',
        'choose_available_folder': 'Scegli cartella disponibile',
        'shortcut_saved': 'Collegamento salvato in:',
        'error': 'Errore'
    },
    'es': {
        'select_folder': 'Seleccionar carpeta',
        'select_folder_default': 'Seleccionar carpeta predeterminada',
        'select_folder_save': 'Seleccionar carpeta para guardar el acceso directo',
        'folder_unavailable': 'Carpeta no disponible',
        'folder_unavailable_msg': 'La carpeta seleccionada no está disponible o está protegida contra escritura:\n{path}\n\nElija otra carpeta.',
        'choose_available_folder': 'Elegir carpeta disponible',
        'shortcut_saved': 'Acceso directo guardado en:',
        'error': 'Error'
    },
    'nl': {
        'select_folder': 'Map selecteren',
        'select_folder_default': 'Standaardmap selecteren',
        'select_folder_save': 'Map selecteren om snelkoppeling op te slaan',
        'folder_unavailable': 'Map niet beschikbaar',
        'folder_unavailable_msg': 'De geselecteerde map is niet beschikbaar of is schrijfbeveiligd:\n{path}\n\nKies een andere map.',
        'choose_available_folder': 'Kies beschikbare map',
        'shortcut_saved': 'Snelkoppeling opgeslagen in:',
        'error': 'Fout'
    },
    'sv': {
        'select_folder': 'Välj mapp',
        'select_folder_default': 'Välj standardmapp',
        'select_folder_save': 'Välj mapp för att spara genvägen',
        'folder_unavailable': 'Mappen är inte tillgänglig',
        'folder_unavailable_msg': 'Den valda mappen är inte tillgänglig eller är skrivskyddad:\n{path}\n\nVälj en annan mapp.',
        'choose_available_folder': 'Välj tillgänglig mapp',
        'shortcut_saved': 'Genväg sparad i:',
        'error': 'Fel'
    },
    'da': {
        'select_folder': 'Vælg mappe',
        'select_folder_default': 'Vælg standardmappe',
        'select_folder_save': 'Vælg mappe til at gemme genvej',
        'folder_unavailable': 'Mappe ikke tilgængelig',
        'folder_unavailable_msg': 'Den valgte mappe er ikke tilgængelig eller er skrivebeskyttet:\n{path}\n\nVælg en anden mappe.',
        'choose_available_folder': 'Vælg tilgængelig mappe',
        'shortcut_saved': 'Genvej gemt i:',
        'error': 'Fejl'
    },
    'no': {
        'select_folder': 'Velg mappe',
        'select_folder_default': 'Velg standardmappe',
        'select_folder_save': 'Velg mappe for å lagre snarvei',
        'folder_unavailable': 'Mappe utilgjengelig',
        'folder_unavailable_msg': 'Den valgte mappen er ikke tilgjengelig eller er skrivebeskyttet:\n{path}\n\nVelg en annen mappe.',
        'choose_available_folder': 'Velg tilgjengelig mappe',
        'shortcut_saved': 'Snarvei lagret i:',
        'error': 'Feil'
    },
    'pt': {
        'select_folder': 'Selecionar pasta',
        'select_folder_default': 'Selecionar pasta padrão',
        'select_folder_save': 'Selecionar pasta para salvar o atalho',
        'folder_unavailable': 'Pasta indisponível',
        'folder_unavailable_msg': 'A pasta selecionada não está disponível ou é somente leitura:\n{path}\n\nEscolha outra pasta.',
        'choose_available_folder': 'Escolher pasta disponível',
        'shortcut_saved': 'Atalho salvo em:',
        'error': 'Erro'
    },
    'pl': {
        'select_folder': 'Wybierz folder',
        'select_folder_default': 'Wybierz domyślny folder',
        'select_folder_save': 'Wybierz folder do zapisania skrótu',
        'folder_unavailable': 'Folder niedostępny',
        'folder_unavailable_msg': 'Wybrany folder jest niedostępny lub chroniony przed zapisem:\n{path}\n\nWybierz inny folder.',
        'choose_available_folder': 'Wybierz dostępny folder',
        'shortcut_saved': 'Skrót zapisany w:',
        'error': 'Błąd'
    },
    'uk': {
        'select_folder': 'Виберіть папку',
        'select_folder_default': 'Виберіть папку за замовчуванням',
        'select_folder_save': 'Виберіть папку для збереження ярлика',
        'folder_unavailable': 'Папка недоступна',
        'folder_unavailable_msg': 'Вибрана папка недоступна або захищена від запису:\n{path}\n\nБудь ласка, виберіть іншу папку.',
        'choose_available_folder': 'Виберіть доступну папку',
        'shortcut_saved': 'Ярлик збережено в:',
        'error': 'Помилка'
    },
    'ru': {
        'select_folder': 'Выберите папку',
        'select_folder_default': 'Выберите папку по умолчанию',
        'select_folder_save': 'Выберите папку для сохранения ярлыка',
        'folder_unavailable': 'Папка недоступна',
        'folder_unavailable_msg': 'Выбранная папка недоступна или защищена от записи:\n{path}\n\nПожалуйста, выберите другую папку.',
        'choose_available_folder': 'Выберите доступную папку',
        'shortcut_saved': 'Ярлык сохранён в:',
        'error': 'Ошибка'
    },
    'zh': {
        'select_folder': '选择文件夹',
        'select_folder_default': '选择默认文件夹',
        'select_folder_save': '选择保存快捷方式的文件夹',
        'folder_unavailable': '文件夹不可用',
        'folder_unavailable_msg': '所选文件夹不可用或受写保护：\n{path}\n\n请选择另一个文件夹。',
        'choose_available_folder': '选择可用文件夹',
        'shortcut_saved': '快捷方式已保存到：',
        'error': '错误'
    },
    'ja': {
        'select_folder': 'フォルダを選択',
        'select_folder_default': 'デフォルトのフォルダを選択',
        'select_folder_save': 'ショートカットを保存するフォルダを選択',
        'folder_unavailable': 'フォルダが利用できません',
        'folder_unavailable_msg': '選択したフォルダは利用できないか、書き込み禁止です：\n{path}\n\n別のフォルダを選択してください。',
        'choose_available_folder': '利用可能なフォルダを選択',
        'shortcut_saved': 'ショートカットを保存しました：',
        'error': 'エラー'
    },
    'ko': {
        'select_folder': '폴더 선택',
        'select_folder_default': '기본 폴더 선택',
        'select_folder_save': '바로 가기를 저장할 폴더 선택',
        'folder_unavailable': '폴더를 사용할 수 없음',
        'folder_unavailable_msg': '선택한 폴더를 사용할 수 없거나 쓰기 방지되어 있습니다:\n{path}\n\n다른 폴더를 선택하십시오.',
        'choose_available_folder': '사용 가능한 폴더 선택',
        'shortcut_saved': '바로 가기가 저장되었습니다:',
        'error': '오류'
    }
}

LCID_MAP = {
    1033: 'en', 1031: 'de', 1036: 'fr', 1040: 'it', 3082: 'es',
    1043: 'nl', 1053: 'sv', 1030: 'da', 1044: 'no', 2070: 'pt',
    1045: 'pl', 1058: 'uk', 1049: 'ru', 2052: 'zh', 1041: 'ja', 1042: 'ko'
}

def get_system_lang():
    try:
        lcid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
        return LCID_MAP.get(lcid, 'en')
    except:
        return 'en'

def get_message(key, lang=None):
    if lang is None:
        lang = get_system_lang()
    return MESSAGES.get(lang, MESSAGES['en']).get(key, key)

# ---------- Определение системной темы (светлая/тёмная) ----------
def is_dark_theme():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        winreg.CloseKey(key)
        return value == 0
    except:
        # Если не удалось прочитать, считаем, что тема светлая
        return False

# ---------- Кастомное всплывающее окно (Tkinter Toast) ----------
def show_toast_notification(folder_path):
    """Показывает плавно всплывающее стильное окно в правом нижнем углу."""
    try:
        lang = get_system_lang()
        msg_template = get_message('shortcut_saved', lang)
        full_msg = f"{msg_template} {folder_path}"

        # Определяем цвета под системную тему
        if is_dark_theme():
            bg = '#202020'
            fg_title = '#ffffff'
            fg_text = '#cccccc'
            border_color = '#3a3a3a'
        else:
            bg = '#f0f0f0'
            fg_title = '#000000'
            fg_text = '#333333'
            border_color = '#c0c0c0'

        toast = tk.Tk()
        toast.overrideredirect(True)
        toast.attributes('-topmost', True)

        width = 360
        height = 70
        screen_w = toast.winfo_screenwidth()
        screen_h = toast.winfo_screenheight()
        x = screen_w - width - 20
        y = screen_h - height - 60

        toast.geometry(f"{width}x{height}+{x}+{y}")
        toast.configure(bg=bg)

        main_frame = tk.Frame(toast, bg=bg, highlightbackground=border_color, highlightthickness=1)
        main_frame.pack(fill='both', expand=True)

        lbl_title = tk.Label(
            main_frame,
            text="Web Shortcut Creator",
            font=("Segoe UI", 9, "bold"),
            fg=fg_title,
            bg=bg,
            anchor='w'
        )
        lbl_title.pack(fill='x', padx=12, pady=(8, 2))

        lbl_msg = tk.Label(
            main_frame,
            text=full_msg,
            font=("Segoe UI", 8),
            fg=fg_text,
            bg=bg,
            anchor='w',
            justify='left'
        )
        lbl_msg.pack(fill='x', padx=12, pady=(0, 8))

        def fade_out():
            alpha = toast.attributes('-alpha')
            if alpha > 0.05:
                toast.attributes('-alpha', alpha - 0.05)
                toast.after(30, fade_out)
            else:
                toast.destroy()

        toast.attributes('-alpha', 0.95)
        toast.after(3000, fade_out)
        toast.mainloop()

    except Exception:
        pass

# ---------- Остальные функции (без изменений) ----------
def read_message():
    raw_length = sys.stdin.buffer.read(4)
    if not raw_length:
        return None
    message_length = struct.unpack('@I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

def send_message(message):
    encoded = json.dumps(message).encode('utf-8')
    sys.stdout.buffer.write(struct.pack('@I', len(encoded)))
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()

def select_folder_dialog(title_key, lang=None):
    if lang is None:
        lang = get_system_lang()
    title = get_message(title_key, lang)
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_selected = filedialog.askdirectory(title=title)
    root.destroy()
    return folder_selected

def show_warning_message(title_key, msg_key, path=None, lang=None):
    if lang is None:
        lang = get_system_lang()
    title = get_message(title_key, lang)
    msg = get_message(msg_key, lang)
    if path is not None:
        msg = msg.format(path=path)
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showwarning(title, msg)
    root.destroy()

def is_path_writable(path):
    if not path or not os.path.isdir(path):
        return False
    try:
        test_file = os.path.join(path, f".test_{hashlib.md5(path.encode()).hexdigest()[:8]}")
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        return True
    except Exception:
        return False

def create_fallback_icon(letter):
    img = Image.new('RGBA', (64, 64), color=(66, 133, 244, 255))
    draw = ImageDraw.Draw(img)
    char = (letter or "W").upper()[0]
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), char, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((64 - w) / 2, (64 - h) / 2 - 4), char, fill="white", font=font)
    return img

def main():
    try:
        data = read_message()
        if not data:
            send_message({"status": "error", "message": "No data"})
            return

        action = data.get('action', 'create_shortcut')
        lang = get_system_lang()

        if action == "ping":
            send_message({"status": "ok", "message": "pong"})
            return

        if action == "select_folder":
            selected_path = select_folder_dialog('select_folder_default', lang)
            send_message({"status": "ok", "selected_path": selected_path})
            return

        url = data.get('url')
        title = data.get('title', 'Shortcut')
        base64_icon = data.get('base64Icon')
        save_mode = data.get('saveMode', 'ask')
        default_path = data.get('defaultPath', '').strip()

        target_dir = ""
        if save_mode == 'ask':
            target_dir = select_folder_dialog('select_folder_save', lang)
            if not target_dir:
                send_message({"status": "cancelled"})
                return
        else:
            real_desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
            candidate_path = default_path if default_path else real_desktop
            if is_path_writable(candidate_path):
                target_dir = candidate_path
            else:
                show_warning_message('folder_unavailable', 'folder_unavailable_msg', candidate_path, lang)
                target_dir = select_folder_dialog('choose_available_folder', lang)
                if not target_dir:
                    send_message({"status": "cancelled"})
                    return

        safe_title = "".join([c for c in title if c not in r'\/:*?"<>|']).strip() or "Shortcut"
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()

        appdata_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'WebShortcutsIcons')
        os.makedirs(appdata_dir, exist_ok=True)

        icon_path = os.path.join(appdata_dir, f"{url_hash}.ico")
        shortcut_path = os.path.join(target_dir, f"{safe_title}.url")

        img = None
        if base64_icon and ',' in base64_icon:
            try:
                base64_data = base64_icon.split(',', 1)[1]
                img_bytes = base64.b64decode(base64_data)
                img = Image.open(io.BytesIO(img_bytes))
            except Exception:
                img = None

        if not img:
            img = create_fallback_icon(safe_title)

        img = img.convert("RGBA")
        img.save(icon_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

        with open(shortcut_path, 'w', encoding='utf-8-sig') as f:
            f.write("[InternetShortcut]\n")
            f.write(f"URL={url}\n")
            f.write(f"IconFile={icon_path}\n")
            f.write("IconIndex=0\n")

        send_message({"status": "ok", "icon_path": icon_path})

        # Показываем уведомление (кастомное окно Tkinter)
        show_toast_notification(target_dir)

    except Exception as e:
        send_message({"status": "error", "message": str(e)})

if __name__ == '__main__':
    main()