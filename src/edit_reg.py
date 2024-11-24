import winreg


def toggle_context_menu_item(menu_name, exe_path):
    try:
        # 레지스트리 경로 정의
        key_path = r"Directory\Background\shell\{}".format(menu_name)

        # 레지스트리 키가 존재하는지 확인
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_READ):
            return True

    except FileNotFoundError:
        # 키가 존재하지 않으면 추가
        add_context_menu_item(menu_name, exe_path)
        print(f"컨텍스트 메뉴 항목 '{menu_name}'이(가) 추가되었습니다.")

    except Exception as e:
        print(f"컨텍스트 메뉴 항목 처리 중 오류 발생: {e}")

    finally:
        return False


def add_context_menu_item(menu_name, exe_path):
    """
    Windows 컨텍스트 메뉴에 항목을 추가하는 함수.

    :param menu_name: 컨텍스트 메뉴에 표시될 이름 (예: "Run Excel Script")
    :param exe_path: 실행 파일의 전체 경로 (예: "C:\\path\\to\\script_name.exe")
    """
    try:
        # 'HKEY_CLASSES_ROOT\Directory\Background\shell\<menu_name>' 키 생성
        key_path = r"Directory\Background\shell\{}".format(menu_name)
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path) as key:
            winreg.SetValue(key, '', winreg.REG_SZ, menu_name)  # 메뉴 이름 설정

        # 'command' 하위 키 생성 및 실행 명령 설정
        command_key_path = key_path + r"\command"
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_key_path) as command_key:
            command_value = f'"{exe_path}" "%V" --silent --action=export'  # "%V"는 현재 폴더 경로를 전달
            winreg.SetValue(command_key, '', winreg.REG_SZ, command_value)

    except PermissionError as e:
        print(f"레지스트리 수정 권한 부족: {e}")
    except Exception as e:
        print(f"컨텍스트 메뉴 항목 추가 중 오류 발생: {e}")


def remove_context_menu_item(menu_name):
    """
    Windows 컨텍스트 메뉴에서 항목을 제거하는 함수.

    :param menu_name: 제거할 메뉴 이름 (예: "Run Excel Script")
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"Directory\Background\shell", 0,
                            winreg.KEY_ALL_ACCESS) as parent_key:
            winreg.DeleteKey(parent_key, menu_name)

    except FileNotFoundError:
        print(f"컨텍스트 메뉴 항목 '{menu_name}'이(가) 존재하지 않습니다.")
    except PermissionError as e:
        print(f"레지스트리 수정 권한 부족: {e}")
    except Exception as e:
        print(f"컨텍스트 메뉴 항목 제거 중 오류 발생: {e}")
