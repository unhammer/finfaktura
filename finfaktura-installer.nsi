;Finfaktura installer
;By havard@gulldahl.no
;
; Based on
;  "Start Menu Folder Selection Example Script"
;  Written by Joost Verburg
; And other examples
; Uses ZipDLL (GPL): http://nsis.sourceforge.net/ZipDLL 


;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;--------------------------------
;General

  ;Name and file
  Name "Fryktelig Fin Faktura"
  OutFile "dist\finfaktura-netinstaller.exe"

  ;Default installation folder
  InstallDir "$PROGRAMFILES\Fryktelig Fin Faktura"
  
  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\Fryktelig Fin Faktura" ""

  ;Request application privileges for Windows Vista
  RequestExecutionLevel user

  SetCompressor /SOLID /FINAL zlib

;--------------------------------
;Variables

  Var StartMenuFolder

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE "LICENSE" ;; lisens-fil
  ;!insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  
  ;Start Menu Folder Page Configuration
  !define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU" 
  !define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\Fryktelig Fin Faktura" 
  !define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"
  
  !insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
  
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  !insertmacro MUI_UNPAGE_FINISH

;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;ZipDLL

  !include "zipdll.nsh"

;--------------------------------
;Installer Sections

Section "Installere Fryktelig Fin Faktura" SecInstall

  SetOutPath "$INSTDIR"

  Call SetupInstDir ;; download the program if not upgrading
  
  ;ADD YOUR OWN FILES HERE...
  File "dist\library.zip"
  
  ;Store installation folder
  WriteRegStr HKCU "Software\Fryktelig Fin Faktura" "Install_Dir" $INSTDIR
  
  ;Create uninstaller
  ;;WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Example2" "DisplayName" "NSIS Example2"
  ;;WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Example2" "UninstallString" '"$INSTDIR\uninstall.exe"'
  ;;WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Example2" "NoModify" 1
  ;;WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Example2" "NoRepair" 1
  WriteUninstaller "$INSTDIR\finfaktura-uninstall.exe"
  
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
    
    ;Create shortcuts
    CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk" "$INSTDIR\finfaktura-uninstall.exe"
    CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Fryktelig Fin Faktura.lnk" "$INSTDIR\faktura.exe"
  
  !insertmacro MUI_STARTMENU_WRITE_END

SectionEnd

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SecInstall ${LANG_ENGLISH} "Installere Fryktelig Fin Faktura"

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecInstall} $(DESC_SecInstall)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
 
;--------------------------------
;Uninstaller Section

Section "Uninstall"

  ; Remove registry keys
  ;;DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Fryktelig Fin Faktura"

  ; Remove files and uninstaller
  Delete "$INSTDIR\_elementtree.pyd"
  Delete "$INSTDIR\_imaging.pyd"
  Delete "$INSTDIR\_hashlib.pyd"
  Delete "$INSTDIR\_rl_accel.pyd"
  Delete "$INSTDIR\_socket.pyd"
  Delete "$INSTDIR\_sqlite3.pyd"
  Delete "$INSTDIR\_ssl.pyd"
  Delete "$INSTDIR\bz2.pyd"
  Delete "$INSTDIR\faktura.exe"
  Delete "$INSTDIR\library.zip"
  Delete "$INSTDIR\mingwm10.dll"
  Delete "$INSTDIR\MSVCR71.dll"
  Delete "$INSTDIR\PyQt4.QtCore.pyd"
  Delete "$INSTDIR\PyQt4.QtGui.pyd"
  Delete "$INSTDIR\pyexpat.pyd"
  Delete "$INSTDIR\python25.dll"
  Delete "$INSTDIR\QtCore4.dll"
  Delete "$INSTDIR\QtGui4.dll"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\sgmlop.pyd"
  Delete "$INSTDIR\sip.pyd"
  Delete "$INSTDIR\sqlite3.dll"
  Delete "$INSTDIR\unicodedata.pyd"
  Delete "$INSTDIR\w9xpopen.exe"
  Delete "$INSTDIR\finfaktura-uninstall.exe"
  RMDir "$INSTDIR"

  !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuFolder
    
  Delete "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk"
  Delete "$SMPROGRAMS\$StartMenuFolder\Fryktelig Fin Faktura.lnk"
  RMDir "$SMPROGRAMS\$StartMenuFolder"
  
  DeleteRegKey /ifempty HKCU "Software\Fryktelig Fin Faktura"

SectionEnd

;--------------------------------
;Functions

Function SetupInstDir

  ;Check for previous installation

  IfFileExists $INSTDIR\python25.dll Good
    ; Nothing there, get the whole shebang
    Call DownloadFullProgram
  Good:
    ; Python runtime exists, assuming the install is good
    
FunctionEnd

Function DownloadFullProgram

  Call ConnectInternet ;Make an internet connection (if no connection available)

  StrCpy $2 "$TEMP\finfaktura-win32-base-2_0_x.zip"
  StrCpy $3 "http://finfaktura.googlecode.com/files/finfaktura-win32-base-2_0_x.zip"
  ;;StrCpy $3 "http://kode.lurtgjort.no/finfaktura-win32-base-2_0_x.zip"
  NSISdl::download $3 $2
  Pop $0
  StrCmp $0 success success
    SetDetailsView show
    DetailPrint "download failed: $0"
    Abort
  success:
    !insertmacro ZIPDLL_EXTRACT $2 $INSTDIR "<ALL>"
    Pop $0
    StrCmp $0 success end
    SetDetailsView show
    DetailPrint "unzip failed: $0"
    Abort
    Delete $2
  end:
  

FunctionEnd

Function ConnectInternet

  Push $R0

    ClearErrors
    Dialer::AttemptConnect
    IfErrors noie3

    Pop $R0
    StrCmp $R0 "online" connected
      MessageBox MB_OK|MB_ICONSTOP "Cannot connect to the internet."
      Quit

    noie3:

    ; IE3 not installed
    MessageBox MB_OK|MB_ICONINFORMATION "Please connect to the internet now."

    connected:

  Pop $R0

FunctionEnd

