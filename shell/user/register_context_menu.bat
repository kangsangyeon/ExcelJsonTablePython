@echo off
set "MenuName=Export Excel Files to json"
set "RegParentKey=HKEY_CLASSES_ROOT\Directory\Background\shell\%MenuName%"
set "RegKey=%RegParentKey%\command"

:: 현재 배치 파일이 위치한 디렉터리 경로 가져오기. (끝에 백슬래시가 있기 때문에 이를 제거)
set "CurrentDir=%~dp0"
if "%CurrentDir:~-1%"=="\" set "CurrentDir=%CurrentDir:~0,-1%"

set "MenuCommand=\"%CurrentDir%\ExcelJsonTablePython.exe\" --folder=\"%%V\" --silent --action=export"

:: 컨텍스트 메뉴 추가
echo Adding context menu item...

:: 메뉴 이름 등록
reg add "%RegParentKey%" /ve /t REG_SZ /d "%MenuName%" /f

:: 명령어 등록
reg add "%RegKey%" /ve /t REG_SZ /d "%MenuCommand%" /f

:: 완료 메시지 출력
echo Context menu item added successfully.
pause