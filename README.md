# ⚡ NATIONVK • Termux Setup

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=25&duration=2500&pause=800&color=00FF41&center=true&vCenter=true&width=700&lines=NATIONVK+TERMUX+SETUP;ANDROID+%7C+PYTHON+%7C+GIT+%7C+PHP;GREEN+HACKER+%7C+MATRIX+%7C+CYBER+THEMES;ONE+COMMAND.+COMPLETE+SETUP." alt="Typing Animation">

</p>

<p align="center">

<img src="https://img.shields.io/badge/Platform-Termux-00ff41?style=for-the-badge&logo=android&logoColor=white">
<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Git-Ready-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">

</p>

<p align="center">

**A modern Termux environment setup by NATIONVK.**

Install essential development tools, Python libraries, utilities and choose your own terminal style — all from one setup.

</p>

---

## 🟢 What is NATIONVK Termux Setup?

**NATIONVK Termux Setup** is an automated Termux environment installer designed to quickly prepare an Android device for Python, Git, PHP and general terminal development.

The setup includes:

* ⚡ Automatic package installation
* 🐍 Python environment
* 📦 Python libraries
* 🔧 Git
* 🌐 PHP
* 🌍 cURL
* 📥 Wget
* 📁 Storage permission
* 🛠️ Useful terminal utilities
* 🎨 Terminal theme manager
* 🟢 Green Hacker theme
* 🟩 Matrix theme
* 🟣 Cyber Purple theme
* 🔵 Cyber Blue theme
* ⚪ Default theme reset

---

# ⚡ ONE-LINE INSTALL

### 🚀 Recommended

```bash
pkg update -y && pkg install git -y && git clone https://github.com/NATIONVK/Termux-Setup.git && cd Termux-Setup &&  python termux_setup.py
```

That's it.

**Clone → Setup → Theme → Ready.**

---

# 🔥 Quick Start

If you already cloned the repository:

```bash
cd Termux-Setup
python termux_setup.py
```

If the script is executable:

```bash
./setup.py
```

---

# 🧰 What Gets Installed?

| Component  | Purpose                   |
| ---------- | ------------------------- |
| 🐍 Python  | Python development        |
| 📦 pip     | Python package management |
| 🔗 Git     | Git/GitHub workflow       |
| 🐘 PHP     | PHP development           |
| 🌐 cURL    | Network requests          |
| 📥 Wget    | File downloading          |
| 📝 Nano    | Lightweight editor        |
| ⚡ Vim      | Advanced terminal editor  |
| 🔐 OpenSSH | SSH support               |
| 📦 Zip     | Archive creation          |
| 📂 Unzip   | Archive extraction        |
| 🌳 Tree    | Directory visualization   |

---

# 🐍 Python Libraries

The setup automatically installs:

```text
rich
requests
mechanize
beautifulsoup4
```

Check installed packages:

```bash
python -m pip list
```

Check Python:

```bash
python --version
```

---

# 🎨 NATIONVK THEME MANAGER

After the main setup, you can select your terminal style.

```text
╔════════════════════════════════════════════════════════════╗
║              NATIONVK THEME MANAGER                        ║
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
```

### 🟢 Green Hacker

```text
NATIONVK@TERMUX:~ ➜
```

Black background + green terminal aesthetic.

### 🟩 Matrix

Matrix-inspired green terminal environment.

### 🟣 Cyber Purple

Neon purple cyberpunk style.

### 🔵 Cyber Blue

Neon blue cyber terminal style.

### ⚪ Default

Restore the normal Termux configuration.

---

# 🖥️ Terminal Customization

The theme manager configures Termux color settings and shell prompt.

Example:

```text
NATIONVK@TERMUX:~ ➜
```

Instead of the standard shell prompt.

The setup also creates useful aliases such as:

```bash
ll
la
cls
```

---

# 🔄 Theme Reset

You can run the setup again whenever you want to change the theme:

```bash
python setup.py
```

Then choose:

```text
[5] Default / Reset
```

---

# 📱 Storage Setup

The installer requests Termux storage access using:

```bash
termux-setup-storage
```

After permission is granted, Termux provides the usual storage links under:

```text
~/storage/
```

---

# 🔍 Installation Verification

At the end of the installation, the script checks:

```text
✓ Python
✓ Pip
✓ Git
✓ PHP
✓ cURL
✓ Wget
✓ Python Libraries
✓ Theme System
```

Example:

```text
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
```

---

# 📂 Repository Structure

```text
Termux-Setup/
│
├── setup.py
├── README.md
└── LICENSE
```

---

# 🚀 Installation Flow

```text
┌──────────────────────┐
│   Start Installation │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Open NATIONVK      │
│      GitHub          │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Storage Permission │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Update & Upgrade     │
│       Termux         │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Install Core Tools   │
│ Python / Git / PHP   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Install Python       │
│ Libraries            │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Verify Installation  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Choose Theme       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│       READY 🚀       │
└──────────────────────┘
```

---

# ⚠️ Important

This project is intended for **Termux environment setup and customization**.

It does not provide unauthorized access to devices, accounts or systems.

Use installed networking and development tools responsibly and only on systems you own or are authorized to test.

---

# 📌 Requirements

* Android device
* Termux
* Internet connection
* Sufficient storage
* Permission to access Android storage

For the best compatibility, use a currently maintained Termux distribution rather than an outdated build.

---

# 🧪 Useful Commands

### Python

```bash
python
```

### Python version

```bash
python --version
```

### Installed Python packages

```bash
python -m pip list
```

### Git

```bash
git --version
```

### PHP

```bash
php --version
```

### Storage

```bash
termux-setup-storage
```

---

# 🌐 NATIONVK

<p align="center">

<a href="https://github.com/NATIONVK">

<img src="https://img.shields.io/badge/GitHub-NATIONVK-181717?style=for-the-badge&logo=github">

</a>

</p>

<p align="center">

<b>Follow • Star • Fork • Learn • Build</b>

</p>

---

# ⭐ Support

If this project helped you:

```text
⭐ Star the repository
🍴 Fork the project
🐛 Report bugs
💡 Suggest improvements
```

---

# 👨‍💻 Author

```text
AUTHOR    : YEASIEN AHMED
GITHUB    : NATIONVK
PROJECT   : Termux-Setup
```

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=3000&pause=1000&color=00FF41&center=true&vCenter=true&width=600&lines=Welcome+To+My+CyBer+World;FIND+YOUR+OWN+PATH;BUILD.+LEARN.+CREATE.;NATIONVK+TERMUX+SETUP">

</p>

---

<p align="center">

**⚡ NATIONVK • BUILD YOUR OWN TERMINAL ⚡**

</p>
```

**README-তে থাকা one-line command-টাই মূল quick installer:**

```bash
pkg update -y && pkg install git -y && git clone https://github.com/NATIONVK/Termux-Setup.git && cd Termux-Setup && python setup.py
```

এটা ব্যবহার করলে আলাদা আলাদা `git clone`, `cd`, `python setup.py` লিখতে হবে না। একই ধরনের Termux setup projects-এও Git clone → setup script চালানোর workflow ব্যবহৃত হয়।

