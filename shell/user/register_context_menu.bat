@echo off
set "MenuName=Export Excel Files to json"
set "RegParentKey=HKEY_CLASSES_ROOT\Directory\Background\shell\%MenuName%"
set "RegKey=%RegParentKey%\command"

:: ���� ��ġ ������ ��ġ�� ���͸� ��� ��������. (���� �齽���ð� �ֱ� ������ �̸� ����)
set "CurrentDir=%~dp0"
if "%CurrentDir:~-1%"=="\" set "CurrentDir=%CurrentDir:~0,-1%"

set "MenuCommand=\"%CurrentDir%\ExcelJsonTablePython.exe\" --folder=\"%%V\" --silent --action=export"

:: ���ؽ�Ʈ �޴� �߰�
echo Adding context menu item...

:: �޴� �̸� ���
reg add "%RegParentKey%" /ve /t REG_SZ /d "%MenuName%" /f

:: ��ɾ� ���
reg add "%RegKey%" /ve /t REG_SZ /d "%MenuCommand%" /f

:: �Ϸ� �޽��� ���
echo Context menu item added successfully.
pause