import logging
import sys
from datetime import datetime
from tkinter import messagebox

import const


def config_logging_stdout(name: str) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        encoding="UTF-8",
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    return logging.getLogger(name=name)


def config_logging_file(name: str, path: str) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        filename=path,
        encoding="UTF-8",
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    return logging.getLogger(name=name)


def get_formatted_date():
    return datetime.now().strftime(const.date_format)


# Alert 창 표시 함수
def show_alert(message, tk=None):
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨김
    messagebox.showerror("오류", message)
    root.destroy()
