# WebShortcutCreator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-blue)](https://chrome.google.com/webstore)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078d7)](https://www.microsoft.com/windows)

**One‑click creation of web shortcuts with real favicon icons on Windows**  
This is a Chrome extension + native messaging host that lets you create desktop shortcuts for any website with its original favicon, all from your browser toolbar.

---

## ✨ Features
- **One‑click** — just click the extension icon on any page and a shortcut is created.
- **Real favicon** — the icon is extracted from the website and embedded into the shortcut.
- **Flexible saving** — choose between asking for a folder each time or saving to a default folder (configurable).
- **Native host** — the shortcut is created by a small Python script (compiled to `.exe`) that runs locally.
- **No extra dependencies** — everything is packed into a single installer.

---

## 📦 Installation (two steps)

### Step 1: Install the Native Host
1. Download the latest release archive from [Releases](https://github.com/Borisovith/WebShortcutCreator/releases).
2. Extract the folder `WebShortcutCreator` anywhere on your PC.
3. Run `Setup.bat` **as Administrator** (right-click → "Run as administrator").
   - This will copy the host files to `%LocalAppData%\WebShortcutCreator` and register the host in the Windows registry.
   - The script may ask for admin rights to add the extension to Chrome policy (so it stays enabled).
4. Wait until the window closes automatically – do not close it manually.

### Step 2: Install the Chrome Extension
1. Open Chrome and go to `chrome://extensions/`.
2. Enable **Developer mode** (toggle in the top‑right corner).
3. Drag and drop the `shortcut_extension.crx` file (from the release archive) onto the extensions page.
4. Confirm installation by clicking **Add extension**.
5. **Pin the extension** to your toolbar: click the puzzle icon (extensions) and click the pin icon next to "Web Shortcut Creator".

> **Important:** Pinning prevents unintended downloads when right‑clicking the icon.

---

## ⚙️ Configuration
Right‑click the extension icon and choose **Options**. There you can set:
- **Ask every time** – a folder picker dialog will appear when you create a shortcut.
- **Save to default folder** – shortcuts are saved immediately to the folder you choose (default is `Desktop`).

---

## 🖥️ System Requirements
- Windows 7 / 8 / 10 / 11
- Google Chrome (any recent version, preferably latest)
- .NET Framework (usually pre‑installed on Windows)
- No Python required – the host is pre‑compiled.

---

## 🔧 Troubleshooting
- **Right‑click triggers a download?** → Make sure the extension is **pinned** to the toolbar (see installation step 2).
- **Shortcut not created?** → Check that the host is registered: look for `HKCU\Software\Google\Chrome\NativeMessagingHosts\com.shortcut.creator` in Registry.
- **Extension not staying enabled?** → Re‑run `Setup.bat` as Administrator to add the Chrome policy.

---

## 📝 Detailed Instructions (Russian)
For a detailed step‑by‑step guide in Russian, see [INSTALL_RU.md](INSTALL_RU.md).

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements
- Built with [Chrome Extensions Manifest V3](https://developer.chrome.com/docs/extensions/mv3/)
- Uses [Tkinter](https://docs.python.org/3/library/tkinter.html) for folder selection dialogs.

---

*Happy shortcutting!* 🚀
