call "%~dp0..\.venv\Scripts\activate" 
pyinstaller ../src/main.py --onefile --noconsole --distpath "../build/dist" --workpath "../build/build" --specpath ".." --name "ExcelJsonTablePython"