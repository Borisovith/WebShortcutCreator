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
    console.warn("Ошибка извлечения иконки:", e);
  }

  // Отправляем команду Python-скрипту
  chrome.runtime.sendNativeMessage('com.shortcut.creator', {
    action: "create_shortcut",
    url: tab.url,
    title: tab.title || "Shortcut",
    base64Icon: base64Icon,
    saveMode: saveMode,
    defaultPath: defaultPath
  }, (response) => {
    if (chrome.runtime.lastError) {
      console.error("Native Error:", chrome.runtime.lastError.message);
    }
  });
});