@echo off
set "MenuName=Export Excel Files to json"
set "RegParentKey=HKEY_CLASSES_ROOT\Directory\Background\shell\%MenuName%"
set "RegKey=%RegParentKey%\command"
set "MenuCommand=ExcelJsonTablePython --folder=\"%%V\" --silent --action=export"

:: ���ؽ�Ʈ �޴� �߰�
:: �޴� �̸� ���
echo Adding context menu item...
reg add "%RegParentKey%" /ve /t REG_SZ /d "%MenuName%" /f

:: ��ɾ� ���
reg add "%RegKey%" /ve /t REG_SZ /d "%MenuCommand%" /f

:: �Ϸ� �޽��� ���
echo Context menu item added successfully.
pause