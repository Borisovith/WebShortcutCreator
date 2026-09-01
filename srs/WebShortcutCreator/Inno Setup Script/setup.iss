; Inno Setup Script for Web Shortcut Creator Native Host
; Full multilingual installer with all languages
; Supports Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox
; Checks if extension is installed in any browser and offers store link
; No Start Menu shortcut or AUMID – they are not needed for custom Tkinter notification

[Setup]
AppName=Web Shortcut Creator Host
AppVersion=1.5
AppPublisher=Borisovith
AppPublisherURL=https://github.com/Borisovith/WebShortcutCreator
AppSupportURL=https://github.com/Borisovith/WebShortcutCreator/issues
AppUpdatesURL=https://github.com/Borisovith/WebShortcutCreator/releases

DefaultDirName={localappdata}\WebShortcutCreator\shortcut_host
DisableDirPage=yes

UninstallFilesDir={localappdata}\WebShortcutCreator

SetupIconFile=WebShortcutCreator.ico
UninstallDisplayIcon={app}\WebShortcutCreator.ico
WizardImageFile=WebShortcutCreator.bmp
WizardSmallImageFile=WebShortcutCreatorSmall.bmp

PrivilegesRequired=lowest
Compression=lzma
SolidCompression=yes
OutputDir=.
OutputBaseFilename=Setup
ShowLanguageDialog=yes

[Languages]
Name: "en"; MessagesFile: "compiler:Default.isl"
Name: "de"; MessagesFile: "compiler:Languages\German.isl"
Name: "fr"; MessagesFile: "compiler:Languages\French.isl"
Name: "it"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "es"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "nl"; MessagesFile: "compiler:Languages\Dutch.isl"
Name: "sv"; MessagesFile: "compiler:Languages\Swedish.isl"
Name: "da"; MessagesFile: "compiler:Languages\Danish.isl"
Name: "no"; MessagesFile: "compiler:Languages\Norwegian.isl"
Name: "pt"; MessagesFile: "compiler:Languages\Portuguese.isl"
Name: "pl"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "uk"; MessagesFile: "compiler:Languages\Ukrainian.isl"
Name: "ru"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "zh"; MessagesFile: "compiler:Languages\ChineseSimplified.isl"
Name: "ja"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "ko"; MessagesFile: "compiler:Languages\Korean.isl"

[CustomMessages]
en.ExtensionNotInstalled=The Web Shortcut Creator extension is not installed in any supported browser (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
en.OpenStorePrompt=The host will work only after you install the extension.%n%nWould you like to open the Chrome Web Store page to install it?%n%n(You can also continue without installing the extension.)

de.ExtensionNotInstalled=Die Web Shortcut Creator-Erweiterung ist in keinem unterstützten Browser installiert (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
de.OpenStorePrompt=Der Host funktioniert erst, nachdem Sie die Erweiterung installiert haben.%n%nMöchten Sie die Chrome Web Store-Seite öffnen, um sie zu installieren?%n%n(Sie können auch fortfahren, ohne die Erweiterung zu installieren.)

fr.ExtensionNotInstalled=L'extension Web Shortcut Creator n'est installée dans aucun navigateur pris en charge (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
fr.OpenStorePrompt=L'hôte ne fonctionnera qu'après avoir installé l'extension.%n%nSouhaitez-vous ouvrir la page du Chrome Web Store pour l'installer ?%n%n(Vous pouvez également continuer sans installer l'extension.)

it.ExtensionNotInstalled=L'estensione Web Shortcut Creator non è installata in nessun browser supportato (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
it.OpenStorePrompt=L'host funzionerà solo dopo aver installato l'estensione.%n%nVuoi aprire la pagina del Chrome Web Store per installarla?%n%n(Puoi anche continuare senza installare l'estensione.)

es.ExtensionNotInstalled=La extensión Web Shortcut Creator no está instalada en ningún navegador compatible (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
es.OpenStorePrompt=El host solo funcionará después de instalar la extensión.%n%n¿Desea abrir la página de Chrome Web Store para instalarla?%n%n(También puede continuar sin instalar la extensión.)

nl.ExtensionNotInstalled=De Web Shortcut Creator-extensie is niet geïnstalleerd in een ondersteunde browser (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
nl.OpenStorePrompt=De host werkt pas nadat je de extensie hebt geïnstalleerd.%n%nWil je de Chrome Web Store-pagina openen om deze te installeren?%n%n(Je kunt ook doorgaan zonder de extensie te installeren.)

sv.ExtensionNotInstalled=Web Shortcut Creator-tillägget är inte installerat i någon webbläsare som stöds (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
sv.OpenStorePrompt=Värden fungerar först efter att du har installerat tillägget.%n%nVill du öppna Chrome Web Store-sidan för att installera det?%n%n(Du kan också fortsätta utan att installera tillägget.)

da.ExtensionNotInstalled=Web Shortcut Creator-udvidelsen er ikke installeret i en understøttet browser (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
da.OpenStorePrompt=Værten fungerer først, når du har installeret udvidelsen.%n%nVil du åbne Chrome Web Store-siden for at installere den?%n%n(Du kan også fortsætte uden at installere udvidelsen.)

no.ExtensionNotInstalled=Web Shortcut Creator-utvidelsen er ikke installert i en nettleser som støttes (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
no.OpenStorePrompt=Verden fungerer først etter at du har installert utvidelsen.%n%nVil du åpne Chrome Web Store-siden for å installere den?%n%n(Du kan også fortsette uten å installere utvidelsen.)

pt.ExtensionNotInstalled=A extensão Web Shortcut Creator não está instalada em nenhum navegador suportado (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
pt.OpenStorePrompt=O host só funcionará após instalar a extensão.%n%nDeseja abrir a página da Chrome Web Store para instalá-la?%n%n(Você também pode continuar sem instalar a extensão.)

pl.ExtensionNotInstalled=Rozszerzenie Web Shortcut Creator nie jest zainstalowane w żadnej obsługiwanej przeglądarce (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
pl.OpenStorePrompt=Host będzie działał dopiero po zainstalowaniu rozszerzenia.%n%nCzy chcesz otworzyć stronę Chrome Web Store, aby je zainstalować?%n%n(Możesz też kontynuować bez instalowania rozszerzenia.)

uk.ExtensionNotInstalled=Розширення Web Shortcut Creator не встановлено в жодному підтримуваному браузері (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
uk.OpenStorePrompt=Хост працюватиме лише після встановлення розширення.%n%nБажаєте відкрити сторінку Chrome Web Store, щоб встановити його?%n%n(Ви також можете продовжити без встановлення розширення.)

ru.ExtensionNotInstalled=Расширение Web Shortcut Creator не установлено ни в одном поддерживаемом браузере (Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox).
ru.OpenStorePrompt=Хост будет работать только после установки расширения.%n%nХотите открыть страницу Chrome Web Store, чтобы установить его?%n%n(Вы также можете продолжить без установки расширения.)

zh.ExtensionNotInstalled=Web Shortcut Creator 扩展程序未安装在受支持的浏览器中（Chrome、Edge、Opera、Brave、Vivaldi、Yandex、Firefox）。
zh.OpenStorePrompt=主机仅在安装扩展程序后才能工作。%n%n是否要打开 Chrome 网上应用店页面进行安装？%n%n（您也可以在不安装扩展程序的情况下继续。）

ja.ExtensionNotInstalled=Web Shortcut Creator 拡張機能はサポートされているブラウザ（Chrome、Edge、Opera、Brave、Vivaldi、Yandex、Firefox）にインストールされていません。
ja.OpenStorePrompt=ホストは拡張機能をインストールした後でのみ機能します。%n%nインストールするために Chrome ウェブストアのページを開きますか？%n%n（拡張機能をインストールせずに続行することもできます。）

ko.ExtensionNotInstalled=Web Shortcut Creator 확장 프로그램이 지원되는 브라우저(Chrome, Edge, Opera, Brave, Vivaldi, Yandex, Firefox)에 설치되어 있지 않습니다.
ko.OpenStorePrompt=호스트는 확장 프로그램을 설치한 후에만 작동합니다.%n%n설치를 위해 Chrome 웹 스토어 페이지를 열겠습니까?%n%n(확장 프로그램을 설치하지 않고 계속할 수도 있습니다.)

[Files]
Source: "make_shortcut.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "WebShortcutCreator.ico"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
; Register Native Messaging host for all browsers (HKCU)
Root: HKCU; Subkey: "Software\Google\Chrome\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Microsoft\Edge\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Opera Software\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\BraveSoftware\Brave\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Vivaldi\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Yandex\YandexBrowser\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey

[Code]
const
  EXTENSION_ID = 'npahemdaconbjbbgojmmegikfnnkgjbc';
  STORE_URL = 'https://chrome.google.com/webstore/detail/' + EXTENSION_ID;

function IsExtensionInstalledInChromiumBrowser(const UserDataPath: string): Boolean;
var
  ProfilePath: string;
  ExtPath: string;
  FindRec: TFindRec;
begin
  Result := False;
  if not DirExists(UserDataPath) then Exit;
  if FindFirst(UserDataPath + '\*', FindRec) then
  begin
    try
      repeat
        if (FindRec.Name <> '.') and (FindRec.Name <> '..') then
        begin
          if (FindRec.Attributes and FILE_ATTRIBUTE_DIRECTORY) <> 0 then
          begin
            ProfilePath := UserDataPath + '\' + FindRec.Name;
            ExtPath := ProfilePath + '\Extensions\' + EXTENSION_ID;
            if DirExists(ExtPath) then
            begin
              Result := True;
              Exit;
            end;
          end;
        end;
      until not FindNext(FindRec);
    finally
      FindClose(FindRec);
    end;
  end;
end;

function IsExtensionInstalledInFirefox: Boolean;
var
  FirefoxPath: string;
  ProfileDir: string;
  ExtPath: string;
  FindRec: TFindRec;
begin
  Result := False;
  FirefoxPath := ExpandConstant('{localappdata}\Mozilla\Firefox\Profiles');
  if not DirExists(FirefoxPath) then Exit;

  if FindFirst(FirefoxPath + '\*', FindRec) then
  begin
    try
      repeat
        if (FindRec.Name <> '.') and (FindRec.Name <> '..') then
        begin
          ProfileDir := FirefoxPath + '\' + FindRec.Name;
          if DirExists(ProfileDir) then
          begin
            ExtPath := ProfileDir + '\extensions\' + EXTENSION_ID;
            if DirExists(ExtPath) then
            begin
              Result := True;
              Exit;
            end;
          end;
        end;
      until not FindNext(FindRec);
    finally
      FindClose(FindRec);
    end;
  end;
end;

function IsExtensionInstalled: Boolean;
begin
  Result :=
    IsExtensionInstalledInChromiumBrowser(ExpandConstant('{localappdata}\Google\Chrome\User Data')) or
    IsExtensionInstalledInChromiumBrowser(ExpandConstant('{localappdata}\Microsoft\Edge\User Data')) or
    IsExtensionInstalledInChromiumBrowser(ExpandConstant('{localappdata}\Opera Software\Opera Stable')) or
    IsExtensionInstalledInChromiumBrowser(ExpandConstant('{localappdata}\BraveSoftware\Brave-Browser\User Data')) or
    IsExtensionInstalledInChromiumBrowser(ExpandConstant('{localappdata}\Vivaldi\User Data')) or
    IsExtensionInstalledInChromiumBrowser(ExpandConstant('{localappdata}\Yandex\YandexBrowser\User Data')) or
    IsExtensionInstalledInFirefox;
end;

function InitializeSetup: Boolean;
var
  MsgText: string;
  ErrorCode: Integer;
begin
  Result := True;

  if not IsExtensionInstalled then
  begin
    MsgText := CustomMessage('ExtensionNotInstalled') + #13#10 + #13#10 +
               CustomMessage('OpenStorePrompt');
    if MsgBox(MsgText, mbConfirmation, MB_YESNO) = IDYES then
    begin
      ShellExec('open', STORE_URL, '', '', SW_SHOWNORMAL, ewNoWait, ErrorCode);
    end;
  end;
end;

procedure CreateJsonFile();
var
  JsonContent: string;
  JsonPath: string;
  HostPath: string;
begin
  JsonPath := ExpandConstant('{app}\com.shortcut.creator.json');
  HostPath := ExpandConstant('{app}\make_shortcut.exe');
  StringChange(HostPath, '\', '\\');
  JsonContent := '{' + #13#10 +
                 '  "name": "com.shortcut.creator",' + #13#10 +
                 '  "description": "Desktop Shortcut Creator Native Host",' + #13#10 +
                 '  "path": "' + HostPath + '",' + #13#10 +
                 '  "type": "stdio",' + #13#10 +
                 '  "allowed_origins": [' + #13#10 +
                 '    "chrome-extension://' + EXTENSION_ID + '/"' + #13#10 +
                 '  ]' + #13#10 +
                 '}';
  SaveStringToFile(JsonPath, JsonContent, False);
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
    CreateJsonFile();
end;

[UninstallDelete]
Type: files; Name: "{app}\com.shortcut.creator.json"
Type: filesandordirs; Name: "{app}"