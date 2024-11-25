@echo off

:: 현재 배치 파일이 위치한 디렉터리 경로 가져오기
set "CurrentDir=%~dp0"
:: 끝에 백슬래시가 있기 때문에 이를 제거
if "%CurrentDir:~-1%"=="\" set "CurrentDir=%CurrentDir:~0,-1%"

:: 레지스트리에서 사용자 PATH 값 가져오기
for /f "tokens=2*" %%A in ('reg query "HKEY_CURRENT_USER\Environment" /v Path 2^>nul') do set "UserPath=%%B"

:: UserPath가 비어 있는지 확인 (reg query 실패 시 대비)
if not defined UserPath (
    echo Failed to retrieve the user PATH.
    goto :eof
)

:: 현재 디렉터리가 PATH에 이미 포함되어 있는지 확인
echo %UserPath% | find /i "%CurrentDir%" >nul
if not errorlevel 1 (
    :: 이미 PATH에 포함된 경우 메시지를 출력하고 종료
    echo The directory "%CurrentDir%" is already in the PATH.
    goto :eof
)

:: 새로운 Path 문자열을 결정함.
:: 세미콜론이 중복으로 삽입되지 않도록 현재 UserPath의 마지막 문자가 세미콜론인지 확인하고 세미콜론을 넣을지 결정.
if "%UserPath:~-1%"==";" (
    set "NewPath=%UserPath%%CurrentDir%;"
) else (
    set "NewPath=%UserPath%;%CurrentDir%;"
)

:: PATH에 현재 디렉터리 추가 (사용자 환경 변수)
reg add "HKEY_CURRENT_USER\Environment" /v Path /t REG_EXPAND_SZ /f /d "%NewPath%"

:: 변경 사항 알림
echo Successfully added "%CurrentDir%" to the user PATH.