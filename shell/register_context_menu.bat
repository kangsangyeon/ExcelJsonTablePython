@echo off
set "MenuName=Export Excel Files to json"
set "RegParentKey=HKEY_CLASSES_ROOT\Directory\Background\shell\%MenuName%"
set "RegKey=%RegParentKey%\command"
set "MenuCommand=ExcelJsonTablePython --folder=\"%%V\" --silent --action=export"

:: 컨텍스트 메뉴 추가
:: 메뉴 이름 등록
echo Adding context menu item...
reg add "%RegParentKey%" /ve /t REG_SZ /d "%MenuName%" /f

:: 명령어 등록
reg add "%RegKey%" /ve /t REG_SZ /d "%MenuCommand%" /f

:: 완료 메시지 출력
echo Context menu item added successfully.
pause