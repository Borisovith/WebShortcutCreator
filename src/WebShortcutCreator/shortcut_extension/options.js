const i18n = {
  en: {
    title: "Save Mode Settings",
    ask: "Ask for folder every time when saving",
    default: "Save to default folder",
    placeholder: "Default: Desktop",
    browse: "Browse...",
    saved: "Settings saved",
    updated: "Default path updated",
    bmc: "Buy me a coffee"
  },
  de: {
    title: "Einstellungen für den Speichermodus",
    ask: "Jedes Mal nach dem Ordner fragen",
    default: "Im Standardordner speichern",
    placeholder: "Standard: Desktop",
    browse: "Durchsuchen...",
    saved: "Einstellungen gespeichert",
    updated: "Standardpfad aktualisiert",
    bmc: "Spendier mir einen Kaffee"
  },
  fr: {
    title: "Paramètres du mode d'enregistrement",
    ask: "Demander le dossier à chaque enregistrement",
    default: "Enregistrer dans le dossier par défaut",
    placeholder: "Par défaut : Bureau",
    browse: "Parcourir...",
    saved: "Paramètres enregistrés",
    updated: "Dossier par défaut mis à jour",
    bmc: "Offrez-moi un café"
  },
  it: {
    title: "Impostazioni modalità di salvataggio",
    ask: "Chiedi ogni volta la cartella di destinazione",
    default: "Salva nella cartella predefinita",
    placeholder: "Predefinito: Desktop",
    browse: "Sfoglia...",
    saved: "Impostazioni salvate",
    updated: "Percorso predefinito aggiornato",
    bmc: "Offrimi un caffè"
  },
  es: {
    title: "Configuración del modo de guardado",
    ask: "Preguntar la carpeta cada vez",
    default: "Guardar en la carpeta predeterminada",
    placeholder: "Predeterminado: Escritorio",
    browse: "Examinar...",
    saved: "Configuración guardada",
    updated: "Ruta predeterminada actualizada",
    bmc: "Invítame un café"
  },
  nl: {
    title: "Instellingen voor opslagmodus",
    ask: "Elke keer vragen om opslagmap",
    default: "Opslaan in standaardmap",
    placeholder: "Standaard: Bureaublad",
    browse: "Bladeren...",
    saved: "Instellingen opgeslagen",
    updated: "Standaardpad bijgewerkt",
    bmc: "Koop een kop koffie voor mij"
  },
  sv: {
    title: "Inställningar för sparläge",
    ask: "Fråga efter mapp varje gång du sparar",
    default: "Spara i standardmappen",
    placeholder: "Standard: Skrivbord",
    browse: "Bläddra...",
    saved: "Inställningar sparade",
    updated: "Standardsökväg uppdaterad",
    bmc: "Bjud mig på en kaffe"
  },
  da: {
    title: "Indstillinger for gemmetilstand",
    ask: "Spørg om mappe hver gang der gemmes",
    default: "Gem i standardmappe",
    placeholder: "Standard: Skrivebord",
    browse: "Gennemse...",
    saved: "Indstillinger gemt",
    updated: "Standardsti opdateret",
    bmc: "Køb mig en kop kaffe"
  },
  no: {
    title: "Innstillinger for lagringsmodus",
    ask: "Spør om mappe hver gang du lagrer",
    default: "Lagre i standardmappe",
    placeholder: "Standard: Skrivebord",
    browse: "Bla gjennom...",
    saved: "Innstillinger lagret",
    updated: "Standardsti oppdatert",
    bmc: "Kjøp meg en kaffe"
  },
  pt: {
    title: "Configurações do modo de salvamento",
    ask: "Perguntar a pasta sempre que salvar",
    default: "Salvar na pasta padrão",
    placeholder: "Padrão: Área de Trabalho",
    browse: "Procurar...",
    saved: "Configurações salvas",
    updated: "Caminho padrão atualizado",
    bmc: "Pague-me um café"
  },
  pl: {
    title: "Ustawienia trybu zapisywania",
    ask: "Pytaj o folder za każdym razem",
    default: "Zapisuj w folderze domyślnym",
    placeholder: "Domyślnie: Pulpit",
    browse: "Przeglądaj...",
    saved: "Ustawienia zapisane",
    updated: "Ścieżka domyślna zaktualizowana",
    bmc: "Postaw mi kawę"
  },
  uk: {
    title: "Налаштування режиму збереження",
    ask: "Запитувати папку щоразу при збереженні",
    default: "Зберігати у папку за замовчуванням",
    placeholder: "За замовчуванням: Робочий стіл",
    browse: "Огляд...",
    saved: "Налаштування збережено",
    updated: "Шлях за замовчуванням оновлено",
    bmc: "Купити мені каву"
  },
  ru: {
    title: "Режим сохранения ярлыков",
    ask: "Спрашивать папку каждый раз при сохранении",
    default: "Сохранять в папку по умолчанию",
    placeholder: "По умолчанию: Рабочий стол",
    browse: "Обзор...",
    saved: "Настройки сохранены",
    updated: "Папка по умолчанию обновлена",
    bmc: "Угостить кофе"
  },
  zh: {
    title: "保存模式设置",
    ask: "每次保存时询问目标文件夹",
    default: "保存到默认文件夹",
    placeholder: "默认：桌面",
    browse: "浏览...",
    saved: "设置已保存",
    updated: "默认路径已更新",
    bmc: "请我喝杯咖啡"
  },
  ja: {
    title: "保存モードの設定",
    ask: "保存時に毎回フォルダを確認する",
    default: "デフォルトフォルダに保存する",
    placeholder: "デフォルト：デスクトップ",
    browse: "参照...",
    saved: "設定を保存しました",
    updated: "デフォルトパスを更新しました",
    bmc: "コーヒーを奢る"
  },
  ko: {
    title: "저장 모드 설정",
    ask: "저장할 때마다 폴더 위치 묻기",
    default: "기본 폴더에 저장",
    placeholder: "기본값: 바탕 화면",
    browse: "찾아보기...",
    saved: "설정이 저장되었습니다",
    updated: "기본 경로가 업데이트되었습니다",
    bmc: "커피 한 잔 사주기"
  }
};

document.addEventListener('DOMContentLoaded', async () => {
  const radioAsk = document.querySelector('input[value="ask"]');
  const radioDefault = document.querySelector('input[value="default"]');
  const defaultPathInput = document.getElementById('defaultPath');
  const browseBtn = document.getElementById('browseBtn');
  const status = document.getElementById('status');
  const langSelect = document.getElementById('langSelect');

  const settings = await chrome.storage.local.get(['saveMode', 'defaultPath', 'appLang']);
  const saveMode = settings.saveMode || 'ask';
  const appLang = settings.appLang || 'auto';

  langSelect.value = appLang;

  if (saveMode === 'ask') {
    radioAsk.checked = true;
  } else {
    radioDefault.checked = true;
  }

  defaultPathInput.value = settings.defaultPath || '';

  // Определение и применение локализации
  function getActiveLang() {
    const selected = langSelect.value;
    if (selected !== 'auto') return selected;
    
    // Получение языка браузера/системы
    const sysLang = chrome.i18n.getUILanguage().split('-')[0].toLowerCase();
    return i18n[sysLang] ? sysLang : 'en';
  }

  function applyTranslation() {
    const lang = getActiveLang();
    const t = i18n[lang] || i18n['en'];

    document.getElementById('titleText').innerText = t.title;
    document.getElementById('lblAsk').innerText = t.ask;
    document.getElementById('lblDefault').innerText = t.default;
    document.getElementById('btnBrowseText').innerText = t.browse;
    document.getElementById('bmcText').innerText = t.bmc;
    defaultPathInput.placeholder = t.placeholder;
  }

  applyTranslation();

  // Смена языка
  langSelect.addEventListener('change', (e) => {
    const selectedLang = e.target.value;
    chrome.storage.local.set({ appLang: selectedLang });
    applyTranslation();
    const t = i18n[getActiveLang()];
    showStatus(t.saved);
  });

  // Переключение режимов сохранения
  document.querySelectorAll('input[name="saveMode"]').forEach((radio) => {
    radio.addEventListener('change', (e) => {
      chrome.storage.local.set({ saveMode: e.target.value });
      const t = i18n[getActiveLang()];
      showStatus(t.saved);
    });
  });

  // Выбор папки по умолчанию
  browseBtn.addEventListener('click', () => {
    chrome.runtime.sendNativeMessage('com.shortcut.creator', { action: "select_folder" }, (response) => {
      if (response && response.selected_path) {
        defaultPathInput.value = response.selected_path;
        radioDefault.checked = true;
        chrome.storage.local.set({
          saveMode: 'default',
          defaultPath: response.selected_path
        });
        const t = i18n[getActiveLang()];
        showStatus(t.updated);
      }
    });
  });

  function showStatus(text) {
    status.innerText = text;
    setTimeout(() => status.innerText = "", 2000);
  }
});