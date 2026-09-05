# WebShortcutCreator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Chrome Web Store](https://img.shields.io/badge/Chrome_Web_Store-v1.4-blue)](https://chromewebstore.google.com/detail/npahemdaconbjbbgojmmegikfnnkgjbc?utm_source=item-share-cb)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078d7)](https://www.microsoft.com/windows)

**One‑click creation of web shortcuts with real favicon icons on Windows**  
This is a Chrome extension + native messaging host that lets you create desktop shortcuts for any website with its original favicon directly from your browser toolbar. Supports Chrome, Edge, Opera, Brave, Vivaldi, and other Chromium-based browsers.

---

## ✨ Features
- **One‑click creation** — click the extension icon on any page to generate a shortcut instantly.
- **Real favicon embedding** — extracts the website's original favicon and bakes it into the Windows `.url` shortcut.
- **Flexible saving modes** — prompt for a destination folder every time or save instantly to a default directory (e.g., Desktop).
- **Native messaging host** — background creation handled safely by a lightweight compiled local executable.
- **Multi-browser support** — companion installer configures Native Messaging for Chrome, Edge, Opera, Brave, and Vivaldi.
- **Clean Installer (Inno Setup)** — `setup.exe` handles Registry configuration for Chromium browsers and supports standard Windows installation and uninstallation via System Settings / Control Panel.

---

## 📦 Quick Start Guide (Two-step setup)

### Step 1: Install the Extension
1. Install **Web Shortcut Creator** directly from the [Chrome Web Store](https://chromewebstore.google.com/detail/npahemdaconbjbbgojmmegikfnnkgjbc?utm_source=item-share-cb).
2. **Pin the extension** to your toolbar: click the puzzle icon (extensions menu) and click the pin icon next to "Web Shortcut Creator".

> **Important:** Pinning ensures predictable right-click context menu behavior.

### Step 2: Install the Native Host
1. Download the latest release archive from [Releases](https://github.com/Borisovith/WebShortcutCreator/releases).
2. Extract the archive and run `setup.exe`.
3. Follow the Inno Setup wizard prompts — it will automatically register the native host in the Windows Registry for your Chromium browsers.

---

## ⚙️ Configuration
Right‑click the extension icon and select **Options** (or open it via the extension manager):
- **Ask every time** – displays a native folder selection dialog whenever you create a shortcut.
- **Save to default folder** – creates shortcuts immediately in your preferred directory (default is `Desktop`).

---

## 🖥️ System Requirements
- Windows 7 / 8 / 10 / 11
- Any Chromium-based browser (Google Chrome, Microsoft Edge, Brave, Opera, Vivaldi)
- No Python runtime required — host and setup tools are fully compiled executable binaries (`.exe`).

---

## 🔧 Troubleshooting
- **Shortcut not created?** → Make sure you have run `setup.exe` after installing the extension.
- **Check Registry entry** → Verify that the key `HKCU\Software\Google\Chrome\NativeMessagingHosts\com.shortcut.creator` exists in your Windows Registry.
- **Right‑click triggers an unintended download?** → Ensure the extension icon is pinned to your main browser toolbar.

---

## 📂 Repository Contents
- **Installer & Setup Source:** `setup.exe` (Inno Setup), setup scripts, `WebShortcutCreator.ico`
- **Native Host Executable & Source:** `make_shortcut.exe`, `make_shortcut.py`
- **Extension Source:** `manifest.json`, `background.js`, `options.html`, `options.js`, icon assets

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements
- Built with [Chrome Extensions Manifest V3](https://developer.chrome.com/docs/extensions/mv3/)
- Uses [Tkinter](https://docs.python.org/3/library/tkinter.html) for local folder selection dialogs.
- Setup wizard compiled with [Inno Setup](https://jrsoftware.org/isinfo.php).

---

*Happy shortcutting!* 🚀




[https://chromewebstore.google.com/detail/web-shortcut-creator/npahemdaconbjbbgojmmegikfnnkgjbc](https://chromewebstore.google.com/detail/web-shortcut-creator/npahemdaconbjbbgojmmegikfnnkgjbc)

