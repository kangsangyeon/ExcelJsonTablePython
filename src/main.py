import argparse
import logging
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

import const
from edit_reg import toggle_context_menu_item
from exporter import export_excel_to_json_dir
from src import utils


# GUI 생성 함수
def create_gui():
    # 메인 창 생성
    root = tk.Tk()
    root.title(const.app_title)

    path_label = tk.Label(root, text="폴더 경로:")
    path_label.grid(row=0, column=0, padx=10, pady=10)

    path_entry = tk.Entry(root, width=50)
    path_entry.grid(row=0, column=1, padx=10, pady=10)

    def browse_directory():
        try:
            directory = filedialog.askdirectory()
            if directory:
                path_entry.delete(0, tk.END)
                path_entry.insert(0, directory)
        except Exception as e:
            logging.error(f"디렉토리 선택 중 오류 발생: {e}")
            utils.show_alert("디렉토리 선택 중 오류가 발생했습니다.")

    browse_button = tk.Button(root, text="찾아보기", command=browse_directory)
    browse_button.grid(row=0, column=2, padx=10, pady=10)

    # 출력 버튼 생성
    def process_files():
        directory = path_entry.get().strip()
        if not os.path.isdir(directory):
            messagebox.showerror("오류", "유효한 디렉토리를 입력하세요.")
            return

        try:
            export_excel_to_json_dir(directory)
        except Exception as e:
            logging.error(f"파일 처리 중 오류 발생: {e}")
            utils.show_alert("파일 처리 중 오류가 발생했습니다. 로그를 확인하세요.")

    output_button = tk.Button(root, text="출력", command=process_files)
    output_button.grid(row=1, column=1, pady=10)

    # 컨텍스트 메뉴 토글 버튼 생성
    def toggle_context_menu():
        try:
            exe_path = os.path.abspath(sys.argv[0])  # 현재 실행 중인 프로그램의 경로
            toggle_context_menu_item("Export Excel Files to json", exe_path)
        except Exception as e:
            logging.error(f"컨텍스트 메뉴 토글 중 오류 발생: {e}")
            utils.show_alert("컨텍스트 메뉴 등록/해제 중 오류가 발생했습니다.")

    context_menu_button = tk.Button(root, text="컨텍스트 메뉴 등록/해제", command=toggle_context_menu)
    context_menu_button.grid(row=2, column=1, pady=10)

    # 경로 입력란에는 기본적으로 현재 위치가 들어감.
    cwd = os.getcwd()
    path_entry.insert(0, cwd)

    root.mainloop()


if __name__ == "__main__":
    # 로깅 설정
    log_file_path = const.log_file_path_format.format(utils.get_formatted_date())
    utils.config_logging_file('main', log_file_path)

    # 명령줄 옵션 파싱
    parser = argparse.ArgumentParser(description=const.app_title)
    parser.add_argument("--silent", action="store_true", help="Silent 모드로 실행")
    parser.add_argument("--folder", type=str, help="처리할 폴더 경로")
    parser.add_argument("--action", type=str, help="실행할 동작 (예: export)")

    args = parser.parse_args()

    try:
        if args.action == "export":
            if os.path.isdir(args.folder):
                export_excel_to_json_dir(args.folder)
            else:
                raise ValueError(f"유효하지 않은 디렉토리입니다: {args.folder}")

        if not args.silent:
            create_gui()

    except Exception as e:
        logging.error(f"프로그램 실행 중 오류 발생: {e}")
        utils.show_alert("프로그램 실행 중 오류가 발생했습니다. 로그를 확인하세요.")
