import sys
import os
import subprocess
from pathlib import Path

PACKAGES = [
    "hyprland",
    "wofi",
    "cava",
    "fastfetch",
    "wpaperd",
    "htop",
    "kitty",
    "nvim",
    "btop",
    "waybar",
    "yazi",
    "zellij",
    "firefox",
    "wl-clipboard",
    "hyprshade"
]

FONTS = [
    "ttf-jetbrains-mono-nerd"
]

VERSIONS = [
    "Winter",
    "Ambient",
    "Summer"
]

AUR_PACKAGES = [
    "ttf-jetbrains-mono-nerd",
    "wpaperd",
    "hyprshade"
]

def update_mirrors():
    print("Updating mirrors...") 
    subprocess.run("sudo pacman -Syu --noconfirm", shell=True) 
    print("Mirrors updated")

def is_aur(pkg: str) -> bool:
    return pkg in AUR_PACKAGES

def install_aur():
    print("Start installing yay...")
    print("Installing Dependencies...")
    cmd = "sudo pacman -S --needed git base-devel go --noconfirm"
    subprocess.run(cmd, shell=True)

    print("Cloning official repo...")
    cmd = "git clone https://aur.archlinux.org/yay.git /tmp/yay"
    subprocess.run(cmd, shell=True)

    print("Building yay...")
    cmd = "cd /tmp/yay && makepkg -si --noconfirm"
    subprocess.run(cmd, shell=True)

    subprocess.run("rm -rf /tmp/yay", shell=True)
    print("yay was Successfully installed ✔")

def set_wallpapers(path: str):
    r = input("Do you want to set the default wallpaper for this theme?")
    if "n" in r.lower():
        return

    subprocess.run("mkdir -p ~/wallpapers")
    subprocess.run("cp wallpaper.png ~/wallpapers")

def install_pkg():
    #installing packages
    update_mirrors()

    print("Installing Packages...")
    for pkg in PACKAGES:
        if is_aur(pkg):
            result = subprocess.run(f"yay -S --noconfirm {pkg}", shell=True,
                                capture_output=True,
                                text=True)
        else:
            result = subprocess.run(f"sudo pacman -S --noconfirm {pkg}", shell=True,
                                capture_output=True,
                                text=True)

        if result.returncode == 0:
            print(f"{pkg} was Successfully installed!")
        else:
            print(f"Error was occurred:{pkg} is not installed")

    #installing Fonts
    print("Installing Fonts...")
    for font in FONTS:
        if is_aur(font):
            result = subprocess.run(f"yay -S --noconfirm {font}",
                                    shell=True,
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                print(f"{font} was Successfully installed!")

        else:
            result = subprocess.run(f"sudo pacman -S --noconfirm {font}",
                                    shell=True,
                                    capture_output=True,
                                    text=True)
            if result.returncode == 0:
                print(f"{font} was Successfully installed!")

def load_configs():
    user = os.getlogin()

    print("Which version of dotfiles do you want to install???") 
    for i, ver in enumerate(VERSIONS):
        print(f"{i + 1}):{ver}")

    conf = int(input("Enter Number: "))
    home = Path.home()
    dotconf = home / ".config"
    selected_ver = VERSIONS[conf - 1]
    ver_path = home / "my-dotfiles-hyprland" / selected_ver


    os.chdir(ver_path)
    subprocess.run("rm example.png", shell=True)
    set_wallpapers()
    subprocess.run("rm wallpaper.png", shell=True)
    subprocess.run(f"cp -r * {dotconf} ", shell=True)

    subprocess.run(f"sudo chown -R {user}:{user} {dotconf}", shell=True)
    print("Configs Was Successfully Installed!")

def install_zsh():
    subprocess.run("cd ~/")
    subprocess.run("sudo pacman -S --noconfirm zsh")
    subprocess.run("chsh -s $(which zsh)")
    omz_cmd ="""
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    """
    subprocess.run(omz_cmd)
    print("Now confirm installation of yours zsh with ohmyzsh menu!")

def main():
    # if the user attempted to run the script as root
    if os.getlogin == "root":
        print("""
        +--------------------------------------------------------------------+
        |                              ERROR                                 |
        +--------------------------------------------------------------------+
        |  This script should NOT be run as root. Running as root may break  |
        |  your user configuration, change file permissions incorrectly, or  |
        |  cause other issues.                                               |
        |                                                                    |
        |  Please run this script as a regular user (sudo will be used       |
        |  automatically when needed).                                       |
        +--------------------------------------------------------------------+
        """)
        exit(1)

    # warning for user
    r = input("""
    +--------------------------------------------------------------------+
    |                              WARNING                               |
    +--------------------------------------------------------------------+
    |  This version of the installation script does NOT support systems  |
    |  like NixOS or Garuda Linux. It only supports Arch Linux in this   |
    |  version.                                                          |
    |                                                                    |
    |  If your system is not supported by this version of the script,    |
    |  nothing will work — or worse, it may break your system.           |
    |                                                                    |
    |  So, Do you want to continue the installation?                     |
    +--------------------------------------------------------------------+
    """)
    continue if "y" in r.lower() else sys.exit(1)

    # installing AUR
    result = subprocess.run("which yay",
                            shell=True,
                            capture_output=True,
                            text=True)
    if not result.returncode == 0:
        install_aur()

    install_pkg()
    load_configs()
    r = input("Do you want to install zsh with ohmyzsh?")

    install_zsh() if "y" in r.lower()

if __name__ == "__main__":
    main()
