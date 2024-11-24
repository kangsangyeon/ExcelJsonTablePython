import subprocess

# Step 1: pip freeze를 통해 현재 설치된 패키지 목록 저장
installed_packages_file = "installed_packages.txt"
requirements_file = "../requirements.txt"

# 현재 설치된 패키지 목록 저장
with open(installed_packages_file, "w") as f:
    subprocess.run(["pip", "freeze"], stdout=f, text=True)

try:
    # Step 2: installed_packages.txt와 requirements.txt 읽기
    with open(installed_packages_file, 'r', encoding='utf-8') as f1, open(requirements_file, 'r',
                                                                          encoding='utf-8') as f2:
        installed_lines = f1.readlines()
        required_lines = f2.readlines()

    # 설치된 패키지 및 버전 정보를 딕셔너리로 변환
    installed_packages = {line.split('==')[0]: line.split('==')[1].strip() for line in installed_lines if '==' in line}
    required_packages = {line.split('==')[0]: line.split('==')[1].strip() for line in required_lines if '==' in line}

    # Step 3: 사라진 패키지 삭제
    for package in list(installed_packages.keys()):
        if package not in required_packages:
            print(f"Removing package: {package}")
            subprocess.run(["pip", "uninstall", "-y", package])

    # Step 4: 새로 추가된 패키지 설치 및 버전 변경
    for package, required_version in required_packages.items():
        if package in installed_packages:
            installed_version = installed_packages[package]
            # 버전이 다른 경우 업데이트
            if installed_version != required_version:
                print(f"Upgrading package: {package} from {installed_version} to {required_version}")
                subprocess.run(["pip", "install", f"{package}=={required_version}"])
        else:
            # 새 패키지 설치
            print(f"Installing new package: {package}=={required_version}")
            subprocess.run(["pip", "install", f"{package}=={required_version}"])

except FileNotFoundError as e:
    print(f"Error: {e}. Make sure both '{installed_packages_file}' and '{requirements_file}' exist.")
