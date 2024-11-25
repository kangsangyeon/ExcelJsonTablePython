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
if errorlevel 1 (
    :: PATH에 디렉터리가 포함되지 않은 경우 메시지를 출력하고 종료
    echo The directory "%CurrentDir%" is not in the user PATH.
    goto :eof
)

:: 현재 디렉터리를 제거한 새로운 PATH 문자열 생성
set "NewPath="
for %%B in ("%UserPath:;=" "%") do (
    if /i not "%%~B"=="%CurrentDir%" (
        if defined NewPath (
            set "NewPath=%NewPath%;%%~B"
        ) else (
            set "NewPath=%%~B"
        )
    )
)

:: 사용자 PATH 업데이트
reg add "HKEY_CURRENT_USER\Environment" /v Path /t REG_EXPAND_SZ /f /d "%NewPath%"

:: 변경 사항 알림
echo Successfully removed "%CurrentDir%" from the user PATH.