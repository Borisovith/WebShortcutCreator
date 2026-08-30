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

def select_folder_dialog(title_text="Выберите папку"):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_selected = filedialog.askdirectory(title=title_text)
    root.destroy()
    return folder_selected

def show_warning_message(title, message):
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showwarning(title, message)
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

        # --- Обработка ping ---
        if action == "ping":
            send_message({"status": "ok", "message": "pong"})
            return

        if action == "select_folder":
            selected_path = select_folder_dialog("Выберите папку по умолчанию")
            send_message({"status": "ok", "selected_path": selected_path})
            return

        url = data.get('url')
        title = data.get('title', 'Shortcut')
        base64_icon = data.get('base64Icon')
        save_mode = data.get('saveMode', 'ask')
        default_path = data.get('defaultPath', '').strip()

        target_dir = ""
        if save_mode == 'ask':
            target_dir = select_folder_dialog("Выберите папку для сохранения ярлыка")
            if not target_dir:
                send_message({"status": "cancelled"})
                return
        else:
            real_desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
            candidate_path = default_path if default_path else real_desktop
            if is_path_writable(candidate_path):
                target_dir = candidate_path
            else:
                show_warning_message("Папка недоступна", 
                    f"Выбранная папка недоступна или защищена от записи:\n{candidate_path}\n\nПожалуйста, выберите другую папку для сохранения.")
                target_dir = select_folder_dialog("Выберите доступную папку для сохранения")
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
    except Exception as e:
        send_message({"status": "error", "message": str(e)})

if __name__ == '__main__':
    main()