import sys
import os
import subprocess
from pathlib import Path

PACKAGES = [
    "hyprland",
    "hyprpaper",
    "wofi",
    "cava",
    "fastfetch",
    "hyprpaper",
    "htop",
    "kitty",
    "nvim",
    "btop",
    "waybar",
    "git",
    "yazi"
]

FONTS = [
    "ttf-jetbrains-mono-nerd"
]

VERSIONS = [
    "Winter",
    "Ambient"
]

AUR_PACKAGES = [
    "ttf-jetbrains-mono-nerd"
]

def fix_mirrors():
    #Updating mirrors
    print("Updating mirrors...")
    
    subprocess.run("sudo pacman -Syu --noconfirm", shell=True)
    
    print("Mirrors updated")

def is_aur(pkg: str) -> bool:
    return pkg in AUR_PACKAGES

def install_aur():
    print("Start installing yay...")
    print("Installing Dependencies...")
    cmd = "sudo pacman -S --needed git base-devel go"
    subprocess.run(cmd, shell=True)

    print("Cloning official repo...")
    cmd = "git clone https://aur.archlinux.org/yay.git /tmp/yay"
    subprocess.run(cmd, shell=True)

    print("Building yay...")
    cmd = "cd /tmp/yay && makepkg -si --noconfirm"
    subprocess.run(cmd, shell=True)

    subprocess.run("rm -rf /tmp/yay", shell=True)
    print("yay was Successfully installed ✔")

def install_pkg():

    #installing packages
    fix_mirrors()
    print("Installing Packages...")
    for pkg in PACKAGES:
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

def install_configs():
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
    set_wallpaper(ver_path)
    subprocess.run(f"cp -r * {dotconf} ", shell=True)

def set_wallpaper(ver_path: str):
    print("Starting setting wallpapers...")
    temp = Path(ver_path)
    wallpaper_path = temp / "wallpaper.png"
    subprocess.run("mkdir -p ~/wallpapers", shell=True)
    subprocess.run(f"mv {wallpaper_path} ~/wallpapers ", shell=True)

    wallpaper_path = Path.home() / "wallpapers" / "wallpaper.png"
    config_path = Path.home() / ".config" / "hypr" / "hyprpaper.conf"
    config_text = f"""preload = {wallpaper_path}
    wallpaper = ,{wallpaper_path}
    """
    config_path.write_text(config_text)
    print("Wallpapers was Successfully Installed! ")

def main():
    # installing AUR
    result = subprocess.run("which yay",
                            shell=True,
                            capture_output=True,
                            text=True)
    if not result.returncode == 0:
        install_aur()
    # installing packages
    install_pkg()

    #installing configs
    install_configs()


if __name__ == "__main__":
    main()
