import subprocess
import sys

def install_requirements(requirements_file="requirements.txt"):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("All dependencies have been successfully installed!")
    except Exception as e:
        print(f"An error occurred while installing dependencies: {e}")

if __name__ == "__main__":
    install_requirements()
