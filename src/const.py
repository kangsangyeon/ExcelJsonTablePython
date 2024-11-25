import os
from pathlib import Path

app_name = "ExcelJsonTablePython"
app_package = f"com.sanyoni.{app_name}"
app_cache_dir = os.path.expandvars(f"%LOCALAPPDATA%/Low/{app_package}")
app_title = "Excel Json Table | All Excel Files in Folder Convert to json"

reg_key_name = f"Directory\\Background\\shell\\{app_name}"
reg_command_name = "Export Excel Files to json"

log_file_path_format = f"{app_cache_dir}/{{}}.log"
date_format = "%Y-%m-%d-[%H-%M-%S]"

# 폴더 생성 시도
Path(app_cache_dir).mkdir(parents=True, exist_ok=True)
