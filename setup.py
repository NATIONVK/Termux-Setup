
import os
import sys
import time
import subprocess
import webbrowser

# ============================================================
# NATIONVK TERMUX SETUP + THEME MANAGER
# Author : YEASIEN AHMED
# GitHub : NATIONVK
# ============================================================

RESET   = "\033[0m"
RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
BLUE    = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN    = "\033[1;36m"
WHITE   = "\033[1;37m"

GITHUB_URL = "https://github.com/NATIONVK"


logo = f"""{MAGENTA}

█▀█ █▀█ █▀█   █▄░█ ▄▀█ ▀█▀ █ █▀█ █▄░█
█▀▀ █▀▄ █▄█   █░▀█ █▀█ ░█░ █ █▄█ █░▀█ {RED}
 |{GREEN}
\\`-'{YELLOW}

██╗░░░██╗███████╗░█████╗░░██████╗██╗███████╗███╗░░██╗
╚██╗░██╔╝██╔════╝██╔══██╗██╔════╝██║██╔════╝████╗░██║
░╚████╔╝░█████╗░░███████║╚█████╗░██║█████╗░░╔██╗██║
░░╚██╔╝░░██╔══╝░░██╔══██║░╚═══██╗██║██╔══╝░░██║╚████║
░░░██║░░░███████╗██║░░██║██████╔╝██║███████╗██║░╚███║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝

{CYAN}
      `----.
{MAGENTA}

       Follow my github account

       Welcome To My CyBer World##!!

       FIND YOUR OWN PATH
       F🖕ck Your Attitude😏😎😏,

_★_★_★_★_★_★_★_★_★_★_★_★_★_★_
  AUTHOR    : YEASIEN AHMED
  GITHUB    : NATIONVK
  FACEBOOK  : Yeasien Ahmed
  WHATTSAPP : +8801728891894
  CONTACT   : yeasienahmed65@gmail.com
  [ CREATED BY PRO NATION VK]

{RESET}
"""


# ============================================================
# BASIC FUNCTIONS
# ============================================================

def clear():
    os.system("clear")


def line():
    print(f"{CYAN}{'━' * 65}{RESET}")


def pause():
    input(f"\n{YELLOW}Press ENTER to continue...{RESET}")


def run(command, title=None):
    if title:
        print(f"\n{BLUE}[•] {title}{RESET}")

    print(f"{YELLOW}$ {command}{RESET}")

    try:
        result = subprocess.run(command, shell=True)

        if result.returncode == 0:
            print(f"{GREEN}[✓] Done{RESET}")
            return True

        print(f"{RED}[✗] Failed — continuing...{RESET}")
        return False

    except KeyboardInterrupt:
        print(f"\n{RED}[!] Cancelled by user.{RESET}")
        sys.exit(0)

    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")
        return False


def banner():
    clear()
    print(logo)


# ============================================================
# OPEN GITHUB
# ============================================================

def open_github():

    print(f"{CYAN}[•] Opening NATIONVK GitHub...{RESET}")

    try:
        webbrowser.open(GITHUB_URL)
        print(f"{GREEN}[✓] GitHub opened.{RESET}")
    except Exception:
        print(f"{YELLOW}[!] Open manually:{RESET}")
        print(GITHUB_URL)

    time.sleep(2)


# ============================================================
# TERMUX CHECK
# ============================================================

def check_termux():

    prefix = os.environ.get("PREFIX", "")

    if "com.termux" not in prefix:

        print(
            f"{YELLOW}"
            f"[!] Warning: This program is designed for Termux."
            f"{RESET}"
        )

        time.sleep(2)


# ============================================================
# CREATE TERMUX DIRECTORIES
# ============================================================

def prepare_termux():

    termux_dir = os.path.expanduser("~/.termux")

    os.makedirs(termux_dir, exist_ok=True)

    return termux_dir


# ============================================================
# COLORS.PROPERTIES
# ============================================================

def write_colors(
    foreground,
    background,
    cursor,
    color0,
    color1,
    color2,
    color3,
    color4,
    color5,
    color6,
    color7,
    color8,
    color9,
    color10,
    color11,
    color12,
    color13,
    color14,
    color15
):

    termux_dir = prepare_termux()

    path = os.path.join(
        termux_dir,
        "colors.properties"
    )

    content = f"""# NATIONVK Termux Theme

foreground={foreground}
background={background}
cursor={cursor}

color0={color0}
color1={color1}
color2={color2}
color3={color3}
color4={color4}
color5={color5}
color6={color6}
color7={color7}
color8={color8}
color9={color9}
color10={color10}
color11={color11}
color12={color12}
color13={color13}
color14={color14}
color15={color15}
"""

    try:

        with open(path, "w") as f:
            f.write(content)

        return True

    except Exception as e:

        print(
            f"{RED}[!] Could not write colors.properties: "
            f"{e}{RESET}"
        )

        return False


# ============================================================
# BASHRC BACKUP
# ============================================================

def backup_bashrc():

    bashrc = os.path.expanduser("~/.bashrc")
    backup = os.path.expanduser("~/.bashrc.nationvk.backup")

    if os.path.exists(bashrc):

        if not os.path.exists(backup):

            try:
                with open(bashrc, "r") as src:
                    data = src.read()

                with open(backup, "w") as dst:
                    dst.write(data)

            except Exception:
                pass


# ============================================================
# REMOVE OLD NATIONVK CONFIG
# ============================================================

def remove_nationvk_config():

    bashrc = os.path.expanduser("~/.bashrc")

    if not os.path.exists(bashrc):
        return

    try:

        with open(bashrc, "r") as f:
            lines = f.readlines()

        new_lines = []
        skip = False

        for line_text in lines:

            if "# ===== NATIONVK THEME START =====" in line_text:
                skip = True
                continue

            if "# ===== NATIONVK THEME END =====" in line_text:
                skip = False
                continue

            if not skip:
                new_lines.append(line_text)

        with open(bashrc, "w") as f:
            f.writelines(new_lines)

    except Exception:
        pass


# ============================================================
# BASH THEME
# ============================================================

def install_bash_theme(
    name,
    prompt_color,
    symbol="➜"
):

    bashrc = os.path.expanduser("~/.bashrc")

    backup_bashrc()
    remove_nationvk_config()

    block = f"""

# ===== NATIONVK THEME START =====

export NATIONVK_THEME="{name}"

# NATIONVK colorful terminal
PS1='\\[{prompt_color}\\]NATIONVK@TERMUX\\[\\033[0m\\]:\\w {symbol} \\[\\033[0m\\]'

alias ll='ls -lah --color=auto'
alias la='ls -A'
alias cls='clear'

# ===== NATIONVK THEME END =====
"""

    try:

        with open(bashrc, "a") as f:
            f.write(block)

        return True

    except Exception as e:

        print(
            f"{RED}[!] Bash configuration error: {e}{RESET}"
        )

        return False


# ============================================================
# GREEN HACKER
# ============================================================

def green_hacker():

    write_colors(
        "#00FF41",
        "#000000",
        "#00FF41",

        "#000000",
        "#FF3333",
        "#33FF33",
        "#FFFF33",
        "#3366FF",
        "#FF33FF",
        "#33FFFF",
        "#CCCCCC",

        "#555555",
        "#FF5555",
        "#55FF55",
        "#FFFF55",
        "#5555FF",
        "#FF55FF",
        "#55FFFF",
        "#FFFFFF"
    )

    install_bash_theme(
        "Green Hacker",
        "\\033[1;32m",
        "➜"
    )

    print(f"""
{GREEN}
╔════════════════════════════════════════════════════════════╗
║                  GREEN HACKER MODE                         ║
╠════════════════════════════════════════════════════════════╣
║  Terminal      : GREEN                                     ║
║  Background    : BLACK                                     ║
║  Prompt        : NATIONVK@TERMUX                           ║
║  Style         : Hacker                                    ║
╚════════════════════════════════════════════════════════════╝
{RESET}
""")

    apply_settings()


# ============================================================
# MATRIX
# ============================================================

def matrix_theme():

    write_colors(
        "#00FF00",
        "#000000",
        "#00FF00",

        "#000000",
        "#008800",
        "#00AA00",
        "#88FF88",
        "#008800",
        "#00AA00",
        "#00FF00",
        "#AAAAAA",

        "#003300",
        "#00AA00",
        "#00CC00",
        "#AAFFAA",
        "#00AA00",
        "#00CC00",
        "#00FF00",
        "#FFFFFF"
    )

    install_bash_theme(
        "Matrix",
        "\\033[1;32m",
        "λ"
    )

    print(f"""
{GREEN}
╔════════════════════════════════════════════════════════════╗
║                     MATRIX MODE                            ║
╠════════════════════════════════════════════════════════════╣
║  Green Matrix terminal activated                          ║
║  Prompt : NATIONVK@TERMUX                                 ║
╚════════════════════════════════════════════════════════════╝
{RESET}
""")

    apply_settings()


# ============================================================
# PURPLE CYBER
# ============================================================

def purple_theme():

    write_colors(
        "#E6CCFF",
        "#08000F",
        "#FF00FF",

        "#100018",
        "#FF0055",
        "#00FF99",
        "#FFFF00",
        "#4488FF",
        "#CC44FF",
        "#00FFFF",
        "#EEEEEE",

        "#333344",
        "#FF3366",
        "#44FFAA",
        "#FFFF44",
        "#6699FF",
        "#DD66FF",
        "#44FFFF",
        "#FFFFFF"
    )

    install_bash_theme(
        "Cyber Purple",
        "\\033[1;35m",
        "◆"
    )

    print(f"""
{MAGENTA}
╔════════════════════════════════════════════════════════════╗
║                   CYBER PURPLE MODE                        ║
╠════════════════════════════════════════════════════════════╣
║  Neon Cyber terminal activated                            ║
║  Prompt : NATIONVK@TERMUX                                 ║
╚════════════════════════════════════════════════════════════╝
{RESET}
""")

    apply_settings()


# ============================================================
# BLUE CYBER
# ============================================================

def blue_theme():

    write_colors(
        "#66CCFF",
        "#000814",
        "#00CCFF",

        "#00101A",
        "#FF4466",
        "#33FF99",
        "#FFFF55",
        "#3388FF",
        "#CC55FF",
        "#33FFFF",
        "#DDDDDD",

        "#223344",
        "#FF6688",
        "#55FFAA",
        "#FFFF77",
        "#55AAFF",
        "#DD77FF",
        "#55FFFF",
        "#FFFFFF"
    )

    install_bash_theme(
        "Cyber Blue",
        "\\033[1;36m",
        "➤"
    )

    print(f"""
{CYAN}
╔════════════════════════════════════════════════════════════╗
║                    CYBER BLUE MODE                         ║
╠════════════════════════════════════════════════════════════╣
║  Neon Blue terminal activated                             ║
║  Prompt : NATIONVK@TERMUX                                 ║
╚════════════════════════════════════════════════════════════╝
{RESET}
""")

    apply_settings()


# ============================================================
# DEFAULT THEME
# ============================================================

def default_theme():

    termux_dir = prepare_termux()

    colors = os.path.join(
        termux_dir,
        "colors.properties"
    )

    try:

        if os.path.exists(colors):
            os.remove(colors)

    except Exception:
        pass

    bashrc = os.path.expanduser("~/.bashrc")

    backup = os.path.expanduser(
        "~/.bashrc.nationvk.backup"
    )

    remove_nationvk_config()

    if os.path.exists(backup):

        try:

            with open(backup, "r") as f:
                original = f.read()

            with open(bashrc, "w") as f:
                f.write(original)

        except Exception:
            pass

    print(
        f"{GREEN}[✓] Default Termux configuration restored.{RESET}"
    )

    apply_settings()


# ============================================================
# APPLY TERMUX SETTINGS
# ============================================================

def apply_settings():

    print(
        f"\n{CYAN}[•] Applying Termux settings...{RESET}"
    )

    # Termux reloads colors after restart.
    # This command is available in normal Termux.
    result = subprocess.run(
        "command -v termux-reload-settings",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:

        subprocess.run(
            "termux-reload-settings",
            shell=True
        )

        print(
            f"{GREEN}[✓] Theme applied.{RESET}"
        )

    else:

        print(
            f"{YELLOW}"
            f"[!] Restart Termux to apply the theme."
            f"{RESET}"
        )


# ============================================================
# THEME MENU
# ============================================================

def theme_menu():

    while True:

        clear()

        print(f"""
{GREEN}
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              NATIONVK THEME MANAGER                       ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║   [1] 🟢 Green Hacker                                      ║
║   [2] 🟩 Matrix                                            ║
║   [3] 🟣 Cyber Purple                                      ║
║   [4] 🔵 Cyber Blue                                        ║
║   [5] ⚪ Default / Reset                                   ║
║   [6] Exit                                                 ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
{RESET}
""")

        choice = input(
            f"{CYAN}Select Theme ➜ {RESET}"
        ).strip()

        if choice == "1":

            green_hacker()
            pause()

        elif choice == "2":

            matrix_theme()
            pause()

        elif choice == "3":

            purple_theme()
            pause()

        elif choice == "4":

            blue_theme()
            pause()

        elif choice == "5":

            default_theme()
            pause()

        elif choice == "6":

            break

        else:

            print(
                f"{RED}[!] Invalid option.{RESET}"
            )
            time.sleep(1)


# ============================================================
# INSTALL PACKAGES
# ============================================================

def install_packages():

    banner()

    print(
        f"{CYAN}NATIONVK TERMUX ENVIRONMENT SETUP{RESET}"
    )

    print(
        f"{WHITE}Installing development tools...{RESET}"
    )

    line()

    # Storage

    run(
        "termux-setup-storage",
        "Requesting storage permission"
    )

    # Update

    run(
        "pkg update -y",
        "Updating package lists"
    )

    run(
        "pkg upgrade -y",
        "Upgrading Termux"
    )

    # Main packages

    packages = [
        ("python", "Installing Python"),
        ("git", "Installing Git"),
        ("php", "Installing PHP"),
        ("curl", "Installing cURL"),
        ("wget", "Installing Wget"),
        ("nano", "Installing Nano"),
        ("vim", "Installing Vim"),
        ("openssh", "Installing OpenSSH"),
        ("zip", "Installing Zip"),
        ("unzip", "Installing Unzip"),
        ("tree", "Installing Tree"),
    ]

    for package, title in packages:

        run(
            f"pkg install {package} -y",
            title
        )

    # Pip

    run(
        "python -m pip install --upgrade pip",
        "Updating Python pip"
    )

    # Python libraries

    python_packages = [
        "rich",
        "requests",
        "mechanize",
        "beautifulsoup4"
    ]

    for package in python_packages:

        run(
            f"python -m pip install {package}",
            f"Installing Python package: {package}"
        )

    # Legacy pip2 check

    print(
        f"\n{MAGENTA}[+] Checking legacy pip2...{RESET}"
    )

    result = subprocess.run(
        "command -v pip2",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:

        for package in [
            "mechanize",
            "requests",
            "bs4"
        ]:

            run(
                f"pip2 install {package}",
                f"Installing legacy package: {package}"
            )

    else:

        print(
            f"{YELLOW}"
            f"[!] pip2 not available on this Termux."
            f"{RESET}"
        )

    line()


# ============================================================
# VERIFY
# ============================================================

def verify_installation():

    print(
        f"\n{CYAN}SYSTEM VERIFICATION{RESET}"
    )

    line()

    commands = [
        ("Python", "python --version"),
        ("Pip", "python -m pip --version"),
        ("Git", "git --version"),
        ("PHP", "php --version"),
        ("cURL", "curl --version"),
        ("Wget", "wget --version"),
    ]

    for name, command in commands:

        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        if result.returncode == 0:

            first_line = result.stdout.splitlines()

            version = (
                first_line[0]
                if first_line
                else "Installed"
            )

            print(
                f"{GREEN}[✓] {name:<10}{RESET} {version}"
            )

        else:

            print(
                f"{RED}[✗] {name:<10} Not available{RESET}"
            )

    line()


# ============================================================
# MAIN
# ============================================================

def main():

    check_termux()

    banner()

    # Open GitHub first

    open_github()

    # Install everything

    install_packages()

    # Verify

    verify_installation()

    # Theme menu

    print(
        f"""
{GREEN}
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║          SETUP COMPLETE — CHOOSE YOUR STYLE                ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
{RESET}
"""
    )

    theme_menu()

    # Final screen

    banner()

    print(f"""
{GREEN}
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              NATIONVK SETUP COMPLETED                      ║
║                                                            ║
║     Python       : READY                                   ║
║     Git          : READY                                   ║
║     PHP          : READY                                   ║
║     cURL         : READY                                   ║
║     Wget         : READY                                   ║
║     Python Libs  : READY                                   ║
║     Theme System : READY                                   ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
{RESET}
""")

    print(
        f"{CYAN}GitHub:{RESET} {GITHUB_URL}"
    )

    print(f"""
{YELLOW}
Useful commands:

  python --version
  python -m pip list
  git --version

To change your theme again:

  python setup.py

{RESET}
""")

    line()

    print(
        f"{MAGENTA}"
        "Thank you for using NATIONVK Termux Setup."
        f"{RESET}"
    )

    # Open NATIONVK GitHub again after the complete setup.
    open_github()


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()