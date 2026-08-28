[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$SourceDir  = $PSScriptRoot
$InstallDir = "$env:LOCALAPPDATA\WebShortcutCreator"
$HostDir    = "$InstallDir\shortcut_host"
$ExtDir     = "$InstallDir\shortcut_extension"

Write-Host "1. Copying components to $InstallDir..." -ForegroundColor Green
New-Item -ItemType Directory -Force -Path $HostDir | Out-Null

if (Test-Path "$SourceDir\shortcut_host") {
    Copy-Item -Path "$SourceDir\shortcut_host\*" -Destination $HostDir -Recurse -Force
} else {
    Copy-Item -Path "$SourceDir\*" -Destination $HostDir -Recurse -Force
}

$HasExtensionFolder = Test-Path "$SourceDir\shortcut_extension"
if ($HasExtensionFolder) {
    New-Item -ItemType Directory -Force -Path $ExtDir | Out-Null
    Copy-Item -Path "$SourceDir\shortcut_extension\*" -Destination $ExtDir -Recurse -Force
}

$CrxFile = Join-Path $SourceDir "shortcut_extension.crx"

# ------------------------------------------------------------------
# Функция поиска ID по папкам Extensions (все профили)
# ------------------------------------------------------------------
function Find-ExtensionIdInFolders {
    $UserDataDir = "$env:LOCALAPPDATA\Google\Chrome\User Data"
    if (-not (Test-Path $UserDataDir)) { return $null }

    $profileDirs = Get-ChildItem -Path $UserDataDir -Directory | Where-Object { Test-Path (Join-Path $_.FullName "Extensions") }
    foreach ($profile in $profileDirs) {
        $extPath = Join-Path $profile.FullName "Extensions"
        $folders = Get-ChildItem -Path $extPath -Directory -ErrorAction SilentlyContinue
        foreach ($folder in $folders) {
            $id = $folder.Name
            if ($id -match '^[a-p]{32}$') {
                $manifest = Get-ChildItem -Path $folder.FullName -Filter "manifest.json" -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1
                if ($manifest) {
                    try {
                        $json = Get-Content $manifest.FullName -Raw -Encoding UTF8 | ConvertFrom-Json -ErrorAction Stop
                        if ($json.name -eq "Web Shortcut Creator" -or $json.name -eq "Desktop Shortcut Creator") {
                            return $id
                        }
                    } catch {}
                }
            }
        }
    }
    return $null
}

# ------------------------------------------------------------------
# Функция ожидания установки расширения (цикл опроса)
# ------------------------------------------------------------------
function Wait-ForExtensionInstallation {
    param(
        [string]$CrxPath,
        [string]$ExtFolderPath,
        [int]$MaxAttempts = 120  # 120 * 2 сек = 4 минуты
    )

    Write-Host "`n========================================================" -ForegroundColor Yellow
    Write-Host "  INSTALL EXTENSION" -ForegroundColor Yellow
    Write-Host "========================================================" -ForegroundColor Yellow
    Write-Host "Please install the extension using one of the following methods:" -ForegroundColor White
    if (Test-Path $CrxPath) {
        Write-Host "1. Drag and drop the file onto chrome://extensions/ (Developer mode ON):" -ForegroundColor Cyan
        Write-Host "   $CrxPath" -ForegroundColor Green
    }
    Write-Host "2. Or click 'Load unpacked' and select the folder:" -ForegroundColor Cyan
    Write-Host "   $ExtFolderPath" -ForegroundColor Green
    Write-Host "========================================================" -ForegroundColor Yellow
    Write-Host "Waiting for extension to be installed..." -ForegroundColor Cyan
    Write-Host "Press Ctrl+C to cancel." -ForegroundColor DarkGray

    $attempt = 0
    while ($attempt -lt $MaxAttempts) {
        $id = Find-ExtensionIdInFolders
        if ($id) {
            Write-Host "`nExtension detected! ID: $id" -ForegroundColor Green
            return $id
        }
        $attempt++
        Write-Host "." -NoNewline -ForegroundColor DarkGray
        Start-Sleep -Seconds 2
    }
    Write-Host "`nTimeout: Extension not installed within expected time." -ForegroundColor Red
    return $null
}

# ------------------------------------------------------------------
# Основной блок получения ID
# ------------------------------------------------------------------
Write-Host "`n2. Checking if extension is already installed..." -ForegroundColor Cyan
$detectedId = $null
try {
    $detectedId = Find-ExtensionIdInFolders
} catch {
    Write-Host "Error while searching for extension: $_" -ForegroundColor Red
}

if (-not $detectedId) {
    Write-Host "Extension not found in Chrome." -ForegroundColor Yellow

    if (Test-Path $CrxFile -or $HasExtensionFolder) {
        $detectedId = Wait-ForExtensionInstallation -CrxPath $CrxFile -ExtFolderPath $ExtDir
    } else {
        Write-Host "No .crx file and no extension folder found. Please provide ID manually." -ForegroundColor Red
    }
}

if (-not $detectedId) {
    Write-Host "`n========================================================" -ForegroundColor Yellow
    Write-Host "  EXTENSION NOT FOUND" -ForegroundColor Red
    Write-Host "========================================================" -ForegroundColor Yellow
    Write-Host "Could not detect the extension automatically." -ForegroundColor White
    Write-Host "Please enter the Extension ID manually." -ForegroundColor White
    Write-Host "You can copy it from chrome://extensions/ (under the extension name)." -ForegroundColor Cyan
    Write-Host "========================================================" -ForegroundColor Yellow

    do {
        $userInput = Read-Host "`nEnter the 32-character ID (letters a-p only)"
        if ($userInput -match '^[a-p]{32}$') {
            $detectedId = $userInput
            Write-Host "Manually entered: $detectedId" -ForegroundColor Green
        } else {
            Write-Host "Invalid ID. Must be 32 lowercase letters a-p." -ForegroundColor Red
        }
    } while (-not $detectedId)
}

# ------------------------------------------------------------------
# Регистрация Native Host (в HKCU)
# ------------------------------------------------------------------
Write-Host "`n3. Creating com.shortcut.creator.json..." -ForegroundColor Green
$ExePath = if (Test-Path "$HostDir\make_shortcut.exe") { "$HostDir\make_shortcut.exe" } else { "$HostDir\run.bat" }
$JsonPath = "$HostDir\com.shortcut.creator.json"

$HostConfig = [PSCustomObject]@{
    name            = "com.shortcut.creator"
    description     = "Desktop Shortcut Creator Native Host"
    path            = $ExePath
    type            = "stdio"
    allowed_origins = @("chrome-extension://$detectedId/")
}

try {
    $HostConfig | ConvertTo-Json -Depth 10 | Set-Content -Path $JsonPath -Encoding UTF8
} catch {
    Write-Host "Failed to create JSON: $_" -ForegroundColor Red
    exit 1
}

Write-Host "4. Registering Native Host in Windows Registry (HKCU)..." -ForegroundColor Green
$RegPath = "HKCU:\Software\Google\Chrome\NativeMessagingHosts\com.shortcut.creator"
try {
    New-Item -Path $RegPath -Force | Out-Null
    Set-ItemProperty -Path $RegPath -Name "(default)" -Value $JsonPath
} catch {
    Write-Host "Failed to write registry: $_" -ForegroundColor Red
    exit 1
}

# ------------------------------------------------------------------
# Добавление в политику для постоянного включения (требует админа)
# ------------------------------------------------------------------
function Add-ExtensionToPolicy {
    param($ExtensionId)

    $PolicyPath = "HKLM:\SOFTWARE\Policies\Google\Chrome\ExtensionInstallAllowlist"
    if (-not (Test-Path $PolicyPath)) {
        New-Item -Path $PolicyPath -Force | Out-Null
    }

    $existing = Get-ItemProperty -Path $PolicyPath -ErrorAction SilentlyContinue
    $alreadyExists = $false
    if ($existing) {
        foreach ($prop in $existing.PSObject.Properties) {
            if ($prop.Name -match '^\d+$' -and $prop.Value -eq $ExtensionId) {
                $alreadyExists = $true
                break
            }
        }
    }
    if ($alreadyExists) {
        Write-Host "Extension ID already in policy allowlist." -ForegroundColor Yellow
        return
    }

    $numbers = @()
    if ($existing) {
        $numbers = $existing.PSObject.Properties | Where-Object { $_.Name -match '^\d+$' } | ForEach-Object { [int]$_.Name }
    }
    $next = if ($numbers) { ($numbers | Measure-Object -Maximum).Maximum + 1 } else { 1 }

    Set-ItemProperty -Path $PolicyPath -Name "$next" -Value $ExtensionId -Type String
    Write-Host "Added extension to policy allowlist (key $next)." -ForegroundColor Green
}

$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if ($isAdmin) {
    Write-Host "`n5. Adding extension to Chrome policy (running as Admin)..." -ForegroundColor Green
    try {
        Add-ExtensionToPolicy -ExtensionId $detectedId
    } catch {
        Write-Host "Failed to add policy: $_" -ForegroundColor Red
    }
} else {
    Write-Host "`n========================================================" -ForegroundColor Yellow
    Write-Host "To make the extension permanently enabled, it must be added" -ForegroundColor White
    Write-Host "to Chrome policy (requires Administrator privileges)." -ForegroundColor White
    Write-Host "========================================================" -ForegroundColor Yellow
    Write-Host "Do you want to restart the script with Admin rights to add the policy?" -ForegroundColor Cyan
    Write-Host "  [Y] Yes (recommended)  [N] Skip (extension may remain disabled)" -ForegroundColor Cyan
    $choice = Read-Host "Your choice (Y/N)"
    if ($choice -eq 'Y' -or $choice -eq 'y') {
        $scriptPath = $MyInvocation.MyCommand.Path
        $arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" -AdminMode -ExtensionId $detectedId"
        try {
            Start-Process powershell -Verb RunAs -ArgumentList $arguments
            Write-Host "Restarting with Admin rights... Please approve UAC." -ForegroundColor Yellow
            exit 0
        } catch {
            Write-Host "Failed to restart with admin rights: $_" -ForegroundColor Red
        }
    } else {
        Write-Host "Skipping policy addition. You may need to enable extension manually." -ForegroundColor Yellow
    }
}

# ------------------------------------------------------------------
# Финальное сообщение
# ------------------------------------------------------------------
Write-Host "`n========================================================" -ForegroundColor Yellow
Write-Host "          INSTALLATION SUCCESSFULLY COMPLETED           " -ForegroundColor Yellow
Write-Host "========================================================" -ForegroundColor Yellow
Write-Host "Host binary installed to: $InstallDir" -ForegroundColor White
Write-Host "Active Extension ID set to: $detectedId" -ForegroundColor Green
if ($isAdmin) {
    Write-Host "Policy added: YES" -ForegroundColor Green
} else {
    Write-Host "Policy added: SKIPPED" -ForegroundColor Yellow
}
Write-Host "========================================================" -ForegroundColor Yellow
Write-Host ""
Start-Sleep -Seconds 5
exit 0

# ------------------------------------------------------------------
# Обработка аргументов для AdminMode (второй запуск)
# ------------------------------------------------------------------
if ($MyInvocation.BoundParameters.ContainsKey('AdminMode') -and $MyInvocation.BoundParameters.ContainsKey('ExtensionId')) {
    $detectedId = $MyInvocation.BoundParameters['ExtensionId']
    Write-Host "`nRunning in Admin mode, adding extension to policy..." -ForegroundColor Green
    Add-ExtensionToPolicy -ExtensionId $detectedId
    Write-Host "Policy added successfully. You can close this window." -ForegroundColor Green
    Start-Sleep -Seconds 3
    exit 0
}