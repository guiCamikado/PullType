import subprocess
import sys

# Função para instalar pacotes via pip
def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar {package_name}: {e}")
        
# Lista de pacotes a serem instalados
packages = ["flask",
            "pyjwt",
            "bcrypt"]
for package in packages:
    install_package(package)