import subprocess
import platform

def install_on_windows(application_name):
    try:
        subprocess.run(["choco", "--version"], check=True)
    except FileNotFoundError:
        print("Chocolatey is not installed. Please install Chocolatey and try again.")
        return

    try:
        subprocess.run(["choco", "install", application_name, "-y"], check=True)
        print(f"Successfully installed {application_name} using Chocolatey.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {application_name} using Chocolatey: {e}")

def install_on_linux(application_name):
    package_managers = {
        "apt": "sudo apt-get",
        "yum": "sudo yum",
        "dnf": "sudo dnf",
        "zypper": "sudo zypper",
    }

    chosen_package_manager = None

    # Check which package manager is available
    for package_manager, command in package_managers.items():
        try:
            subprocess.run([package_manager, "--version"], check=True)
            chosen_package_manager = package_manager
            break
        except FileNotFoundError:
            continue

    if chosen_package_manager:
        try:
            subprocess.run([chosen_package_manager, "install", application_name, "-y"], check=True)
            print(f"Successfully installed {application_name} using {chosen_package_manager}.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {application_name} using {chosen_package_manager}: {e}")
    else:
        print("No compatible package manager found for your Linux distribution.")

def install_on_macos(application_name):
    try:
        subprocess.run(["brew", "--version"], check=True)
    except FileNotFoundError:
        print("Homebrew is not installed. Please install Homebrew and try again.")
        return

    try:
        subprocess.run(["brew", "install", application_name], check=True)
        print(f"Successfully installed {application_name} using Homebrew.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {application_name} using Homebrew: {e}")

def install_application(application_name):
    os_name = platform.system()

    if os_name == "Windows":
        install_on_windows(application_name)
    elif os_name == "Linux":
        install_on_linux(application_name)
    elif os_name == "Darwin":
        install_on_macos(application_name)
    else:
        print(f"The application cannot be installed on {os_name}.")

if __name__ == "__main__":
    application_name = input("Enter the application name to install: ")
    install_application(application_name)
