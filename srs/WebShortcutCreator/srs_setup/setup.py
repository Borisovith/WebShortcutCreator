import os
import sys
import shutil
import json
import winreg
import ctypes
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

# --- CONFIGURATION ---
EXTENSION_ID = "npahemdaconbjbbgojmmegikfnnkgjbc"  # ваш магазинный ID
INSTALL_DIR = os.path.join(os.environ['LOCALAPPDATA'], 'WebShortcutCreator')
HOST_DIR = os.path.join(INSTALL_DIR, 'shortcut_host')
HOST_EXE = 'make_shortcut.exe'
HOST_BAT = 'run.bat'
JSON_FILENAME = 'com.shortcut.creator.json'
CHROME_STORE_URL = "https://chrome.google.com/webstore/detail/" + EXTENSION_ID

# Список браузеров и их путей в реестре (HKCU)
BROWSER_REG_PATHS = {
    "Google Chrome": r"Software\Google\Chrome\NativeMessagingHosts\com.shortcut.creator",
    "Microsoft Edge": r"Software\Microsoft\Edge\NativeMessagingHosts\com.shortcut.creator",
    "Opera": r"Software\Opera Software\NativeMessagingHosts\com.shortcut.creator",
    "Brave": r"Software\BraveSoftware\Brave\NativeMessagingHosts\com.shortcut.creator",
    "Vivaldi": r"Software\Vivaldi\NativeMessagingHosts\com.shortcut.creator",
}
# --------------------

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def run_as_admin():
    script = sys.executable
    params = ' '.join([f'"{arg}"' for arg in sys.argv])
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", script, params, None, 1)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to request admin rights: {e}")
        return False

def is_extension_installed(extension_id):
    user_data = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data')
    if not os.path.isdir(user_data):
        return False
    for profile in os.listdir(user_data):
        ext_path = os.path.join(user_data, profile, 'Extensions', extension_id)
        if os.path.isdir(ext_path):
            return True
    return False

def register_native_host_for_browser(json_path, reg_path):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, json_path)
        winreg.CloseKey(key)
        return True
    except Exception:
        return False

class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Shortcut Creator - Installer")
        self.root.geometry("500x520")
        self.root.resizable(False, False)

        try:
            icon_path = resource_path("WebShortcutCreator.ico")
            self.root.iconbitmap(icon_path)
        except:
            pass

        ttk.Label(root, text="Web Shortcut Creator", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(root, text="Installer", font=("Arial", 10)).pack()

        self.status_var = tk.StringVar()
        self.status_var.set("Initializing...")
        ttk.Label(root, textvariable=self.status_var, wraplength=450, justify="center").pack(pady=10)

        self.progress = ttk.Progressbar(root, mode='indeterminate', length=400)
        self.progress.pack(pady=5)

        self.log_text = tk.Text(root, height=12, width=70, state='disabled', wrap='word', font=("Consolas", 8))
        self.log_text.pack(pady=5, padx=10)

        self.finish_btn = ttk.Button(root, text="Finish", command=self.finish, state='disabled')
        self.finish_btn.pack(pady=10)

        self.progress.start(10)
        threading.Thread(target=self.run_install, daemon=True).start()

    def log(self, msg):
        self.log_text.config(state='normal')
        self.log_text.insert('end', msg + '\n')
        self.log_text.see('end')
        self.log_text.config(state='disabled')
        self.root.update()

    def finish(self):
        self.root.destroy()

    def show_extension_not_found(self, url):
        """Показывает диалог с ссылкой, кнопкой открытия и копирования."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Extension not installed")
        dialog.geometry("420x220")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()

        ttk.Label(dialog, text="The extension is not installed in Chrome.", font=("Arial", 10)).pack(pady=5)
        ttk.Label(dialog, text="You can install it from the Chrome Web Store:", font=("Arial", 9)).pack(pady=2)

        # Ссылка (кликабельная)
        link = ttk.Label(dialog, text=url, foreground="blue", cursor="hand2", wraplength=380)
        link.pack(pady=5)
        link.bind("<Button-1>", lambda e: webbrowser.open(url))

        # Кнопки
        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(pady=15)

        def open_browser():
            webbrowser.open(url)
            dialog.destroy()

        def copy_link():
            self.root.clipboard_clear()
            self.root.clipboard_append(url)
            self.root.update()
            dialog.destroy()

        ttk.Button(btn_frame, text="Open in Browser", command=open_browser).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Copy Link", command=copy_link).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Continue", command=dialog.destroy).pack(side=tk.LEFT, padx=5)

        self.root.wait_window(dialog)

    def run_install(self):
        try:
            self.status_var.set("Checking extension...")
            self.log("Checking if extension is installed in Chrome...")
            if is_extension_installed(EXTENSION_ID):
                self.log("✓ Extension is already installed.")
            else:
                self.log("✗ Extension not found.")
                self.log("You can install it later from the Chrome Web Store:")
                self.log(f"  {CHROME_STORE_URL}")
                # Показываем диалог с ссылкой и кнопками
                self.show_extension_not_found(CHROME_STORE_URL)

            self.status_var.set("Checking admin rights...")
            self.log("Checking admin rights...")
            if not is_admin():
                self.log("Requesting administrator privileges...")
                self.root.update()
                if run_as_admin():
                    self.root.quit()
                    return
                else:
                    messagebox.showwarning("Warning", "Could not obtain admin rights.\nWill continue without adding Chrome policy.")
            else:
                self.log("✓ Running with admin rights.")

            self.status_var.set("Copying host files...")
            self.log("Copying host files...")
            src_dir = resource_path('shortcut_host')
            if not os.path.exists(src_dir):
                raise Exception("Embedded host folder not found.")
            os.makedirs(HOST_DIR, exist_ok=True)
            for item in os.listdir(src_dir):
                s = os.path.join(src_dir, item)
                d = os.path.join(HOST_DIR, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            self.log("✓ Host files copied.")

            self.status_var.set("Creating configuration...")
            self.log("Creating com.shortcut.creator.json...")
            exe_path = os.path.join(HOST_DIR, HOST_EXE)
            if not os.path.exists(exe_path):
                exe_path = os.path.join(HOST_DIR, HOST_BAT)
                if not os.path.exists(exe_path):
                    raise Exception("Neither make_shortcut.exe nor run.bat found.")
            json_path = os.path.join(HOST_DIR, JSON_FILENAME)
            config = {
                "name": "com.shortcut.creator",
                "description": "Desktop Shortcut Creator Native Host",
                "path": exe_path,
                "type": "stdio",
                "allowed_origins": [f"chrome-extension://{EXTENSION_ID}/"]
            }
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
            self.log("✓ JSON created.")

            self.status_var.set("Registering in Windows Registry...")
            self.log("Registering native host for all supported browsers...")
            registered_count = 0
            for browser_name, reg_path in BROWSER_REG_PATHS.items():
                if register_native_host_for_browser(json_path, reg_path):
                    self.log(f"  ✓ {browser_name}")
                    registered_count += 1
                else:
                    self.log(f"  ✗ {browser_name} (failed)")
            self.log(f"Registered for {registered_count} browser(s).")

            if is_admin():
                self.status_var.set("Adding to Chrome policy...")
                self.log("Adding extension to Chrome policy (admin)...")
                policy_path = r"SOFTWARE\Policies\Google\Chrome\ExtensionInstallAllowlist"
                try:
                    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, policy_path)
                    idx = 1
                    while True:
                        try:
                            winreg.QueryValueEx(key, str(idx))
                            idx += 1
                        except FileNotFoundError:
                            break
                    winreg.SetValueEx(key, str(idx), 0, winreg.REG_SZ, EXTENSION_ID)
                    winreg.CloseKey(key)
                    self.log(f"✓ Added to policy (key {idx}).")
                except Exception as e:
                    self.log(f"✗ Failed to add policy: {e}")
            else:
                self.log("Skipped policy (no admin rights).")

            self.status_var.set("Installation completed successfully!")
            self.log("=" * 60)
            self.log(f"Extension ID: {EXTENSION_ID}")
            self.log(f"Installed to: {INSTALL_DIR}")
            self.log("=" * 60)
            self.finish_btn.config(state='normal')
            self.progress.stop()
            self.progress['mode'] = 'determinate'
            self.progress['value'] = 100

        except Exception as e:
            self.log(f"ERROR: {e}")
            messagebox.showerror("Installation Failed", str(e))
            self.progress.stop()
            self.finish_btn.config(state='normal', text="Close")
            self.finish_btn.config(command=self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()