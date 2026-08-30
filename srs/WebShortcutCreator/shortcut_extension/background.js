// background.js

const HOST_NAME = 'com.shortcut.creator';
const DOWNLOAD_URL = 'https://github.com/Borisovith/WebShortcutCreator/releases/download/v1.4/setup.exe';

// Локализация для уведомлений
const NOTIFICATION_I18N = {
  en: {
    title: "Web Shortcut Creator",
    message: "The companion host is not installed. Please download and run the installer.",
    button: "Download installer"
  },
  de: {
    title: "Web Shortcut Creator",
    message: "Der Begleit-Host ist nicht installiert. Bitte laden Sie das Installationsprogramm herunter und führen Sie es aus.",
    button: "Installationsprogramm herunterladen"
  },
  fr: {
    title: "Web Shortcut Creator",
    message: "L'hôte compagnon n'est pas installé. Veuillez télécharger et exécuter l'installateur.",
    button: "Télécharger l'installateur"
  },
  it: {
    title: "Web Shortcut Creator",
    message: "L'host companion non è installato. Scarica ed esegui l'installer.",
    button: "Scarica l'installer"
  },
  es: {
    title: "Web Shortcut Creator",
    message: "El host compañero no está instalado. Descargue y ejecute el instalador.",
    button: "Descargar instalador"
  },
  nl: {
    title: "Web Shortcut Creator",
    message: "De companion-host is niet geïnstalleerd. Download en voer de installer uit.",
    button: "Installer downloaden"
  },
  sv: {
    title: "Web Shortcut Creator",
    message: "Värdprogrammet är inte installerat. Ladda ner och kör installatören.",
    button: "Ladda ner installatör"
  },
  da: {
    title: "Web Shortcut Creator",
    message: "Værtsprogrammet er ikke installeret. Download og kør installatøren.",
    button: "Download installatør"
  },
  no: {
    title: "Web Shortcut Creator",
    message: "Vertsprogrammet er ikke installert. Last ned og kjør installasjonsprogrammet.",
    button: "Last ned installasjonsprogram"
  },
  pt: {
    title: "Web Shortcut Creator",
    message: "O host complementar não está instalado. Baixe e execute o instalador.",
    button: "Baixar instalador"
  },
  pl: {
    title: "Web Shortcut Creator",
    message: "Host towarzyszący nie jest zainstalowany. Pobierz i uruchom instalator.",
    button: "Pobierz instalator"
  },
  uk: {
    title: "Web Shortcut Creator",
    message: "Хост-компаньйон не встановлено. Завантажте та запустіть встановлювач.",
    button: "Завантажити встановлювач"
  },
  ru: {
    title: "Web Shortcut Creator",
    message: "Хост-компаньон не установлен. Скачайте и запустите установщик.",
    button: "Скачать установщик"
  },
  zh: {
    title: "Web Shortcut Creator",
    message: "配套主机未安装。请下载并运行安装程序。",
    button: "下载安装程序"
  },
  ja: {
    title: "Web Shortcut Creator",
    message: "コンパニオンホストがインストールされていません。インストーラをダウンロードして実行してください。",
    button: "インストーラをダウンロード"
  },
  ko: {
    title: "Web Shortcut Creator",
    message: "컴패니언 호스트가 설치되지 않았습니다. 설치 프로그램을 다운로드하여 실행하십시오.",
    button: "설치 프로그램 다운로드"
  }
};

// Получение активного языка (с учётом сохранённого в storage)
async function getActiveLang() {
  const result = await chrome.storage.local.get(['appLang']);
  const savedLang = result.appLang || 'auto';
  if (savedLang !== 'auto') return savedLang;
  // Если auto – берём системный
  const sysLang = chrome.i18n.getUILanguage().split('-')[0].toLowerCase();
  return NOTIFICATION_I18N[sysLang] ? sysLang : 'en';
}

// Функция для показа уведомления с локализацией
async function showHostMissingNotification() {
  const lang = await getActiveLang();
  const t = NOTIFICATION_I18N[lang] || NOTIFICATION_I18N['en'];
  chrome.notifications.create({
    type: "basic",
    iconUrl: "WebShortcutCreator.png",
    title: t.title,
    message: t.message,
    buttons: [{ title: t.button }],
    requireInteraction: true
  });
}

// Проверка хоста при клике (как было)
chrome.action.onClicked.addListener(async (tab) => {
  if (!tab.id || !tab.url) return;
  if (tab.url.startsWith("chrome://") || tab.url.startsWith("edge://") || tab.url.startsWith("about:")) return;

  const settings = await chrome.storage.local.get(['saveMode', 'defaultPath']);
  const saveMode = settings.saveMode || 'ask';
  const defaultPath = settings.defaultPath || '';

  let base64Icon = "";

  try {
    const results = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: async () => {
        const getBase64FromUrl = async (url) => {
          return new Promise((resolve) => {
            const img = new Image();
            img.crossOrigin = "anonymous";
            img.onload = () => {
              try {
                const canvas = document.createElement("canvas");
                canvas.width = 64;
                canvas.height = 64;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0, 64, 64);
                resolve(canvas.toDataURL("image/png"));
              } catch (e) {
                resolve("");
              }
            };
            img.onerror = () => resolve("");
            img.src = url;
          });
        };

        const iconEl = document.querySelector('link[rel*="icon"]');
        let iconUrl = iconEl ? iconEl.href : "";
        if (!iconUrl) {
          iconUrl = window.location.origin + "/favicon.ico";
        }

        return await getBase64FromUrl(iconUrl);
      }
    });

    base64Icon = results[0]?.result || "";
  } catch (e) {
    console.warn("Error getting icon:", e);
  }

  chrome.runtime.sendNativeMessage(HOST_NAME, {
    action: "create_shortcut",
    url: tab.url,
    title: tab.title || "Shortcut",
    base64Icon: base64Icon,
    saveMode: saveMode,
    defaultPath: defaultPath
  }, (response) => {
    if (chrome.runtime.lastError) {
      const err = chrome.runtime.lastError.message;
      console.error("Native Error:", err);
      if (err.includes("native host") || err.includes("not found") || err.includes("com.shortcut.creator")) {
        showHostMissingNotification();
      }
    }
  });
});

// Обработка нажатия на кнопку уведомления
chrome.notifications.onButtonClicked.addListener((notificationId, buttonIndex) => {
  if (buttonIndex === 0) {
    chrome.tabs.create({ url: DOWNLOAD_URL });
  }
});

// Обработка запроса ping из options.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'pingHost') {
    chrome.runtime.sendNativeMessage(HOST_NAME, { action: 'ping' }, (response) => {
      if (chrome.runtime.lastError) {
        sendResponse({ alive: false, error: chrome.runtime.lastError.message });
      } else {
        sendResponse({ alive: true });
      }
    });
    return true;
  }
});