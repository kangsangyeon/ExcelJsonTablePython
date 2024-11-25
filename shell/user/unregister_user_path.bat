@echo off

:: ���� ��ġ ������ ��ġ�� ���͸� ��� ��������
set "CurrentDir=%~dp0"
:: ���� �齽���ð� �ֱ� ������ �̸� ����
if "%CurrentDir:~-1%"=="\" set "CurrentDir=%CurrentDir:~0,-1%"

:: ������Ʈ������ ����� PATH �� ��������
for /f "tokens=2*" %%A in ('reg query "HKEY_CURRENT_USER\Environment" /v Path 2^>nul') do set "UserPath=%%B"

:: UserPath�� ��� �ִ��� Ȯ�� (reg query ���� �� ���)
if not defined UserPath (
    echo Failed to retrieve the user PATH.
    goto :eof
)

:: ���� ���͸��� PATH�� �̹� ���ԵǾ� �ִ��� Ȯ��
echo %UserPath% | find /i "%CurrentDir%" >nul
if errorlevel 1 (
    :: PATH�� ���͸��� ���Ե��� ���� ��� �޽����� ����ϰ� ����
    echo The directory "%CurrentDir%" is not in the user PATH.
    goto :eof
)

:: ���� ���͸��� ������ ���ο� PATH ���ڿ� ����
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

:: ����� PATH ������Ʈ
reg add "HKEY_CURRENT_USER\Environment" /v Path /t REG_EXPAND_SZ /f /d "%NewPath%"

:: ���� ���� �˸�
echo Successfully removed "%CurrentDir%" from the user PATH.