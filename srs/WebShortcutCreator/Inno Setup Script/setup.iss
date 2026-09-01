; Inno Setup Script for Web Shortcut Creator Native Host
; Full multilingual installer with all languages from the extension
; Supports Chrome, Edge, Opera, Brave, Vivaldi, Yandex
; Checks if extension is installed and offers to open store

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

[Files]
Source: "make_shortcut.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "WebShortcutCreator.ico"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
; Google Chrome
Root: HKCU; Subkey: "Software\Google\Chrome\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
; Microsoft Edge
Root: HKCU; Subkey: "Software\Microsoft\Edge\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
; Opera
Root: HKCU; Subkey: "Software\Opera Software\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
; Brave
Root: HKCU; Subkey: "Software\BraveSoftware\Brave\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
; Vivaldi
Root: HKCU; Subkey: "Software\Vivaldi\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey
; Yandex
Root: HKCU; Subkey: "Software\Yandex\YandexBrowser\NativeMessagingHosts\com.shortcut.creator"; ValueType: string; ValueName: ""; ValueData: "{app}\com.shortcut.creator.json"; Flags: uninsdeletekey

[Code]
const
  EXTENSION_ID = 'npahemdaconbjbbgojmmegikfnnkgjbc';
  STORE_URL = 'https://chrome.google.com/webstore/detail/' + EXTENSION_ID;

function IsExtensionInstalled: Boolean;
var
  UserDataPath: string;
  ProfilePath: string;
  ExtPath: string;
  FindRec: TFindRec;
begin
  Result := False;
  UserDataPath := ExpandConstant('{localappdata}\Google\Chrome\User Data');
  if not DirExists(UserDataPath) then
    Exit;

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

function InitializeSetup: Boolean;
var
  MsgText: string;
  ErrorCode: Integer;
begin
  Result := True;

  if not IsExtensionInstalled then
  begin
    MsgText := 'The Web Shortcut Creator extension is not installed in Chrome.' + #13#10 +
               'The host will work only after you install the extension.' + #13#10 +
               'Would you like to open the Chrome Web Store page to install it?' + #13#10 +
               '(You can also continue without installing the extension.)';
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