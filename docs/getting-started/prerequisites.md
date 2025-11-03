# Prerequisites

Before starting with the Nummernsender project, ensure you have the following prerequisites in place.

## Software Requirements

### Required

- **Python 3.12 or later**
  ```bash
  python --version
  # Should show 3.12.x or higher
  ```

- **Package Manager**
  - `uv` (recommended) or `pip`
  ```bash
  # Check if uv is installed
  uv --version
  ```

- **Web Browser**
  - Chrome, Firefox, Safari, or Edge (latest version)

### Optional (for Pico Development)

- **Thonny IDE**
  - Required for Raspberry Pi Pico programming
  - [Installation Guide](../guides/thonny_installation.md)

- **Git**
  - For version control
  ```bash
  git --version
  ```

## Hardware Requirements

### For Web Development Only

- Computer with:
  - macOS, Windows, or Linux
  - Minimum 4GB RAM (8GB recommended)
  - 1GB free disk space
  - Internet connection

### For IoT Development (Raspberry Pi Pico)

- **Raspberry Pi Pico W**
  - WiFi-enabled version required for wireless examples
  - Regular Pico works for basic LED examples only

- **Micro USB Cable**
  - Must be a data cable (not charge-only)
  - For programming and power

- **WiFi Network**
  - 2.4 GHz network (Pico W doesn't support 5 GHz)
  - Network credentials (SSID and password)

## Knowledge Prerequisites

### Basic Level (Recommended)

- **Python Programming**
  - Variables, functions, loops
  - Basic data types (lists, dictionaries)
  - Import statements

- **Command Line**
  - Navigate directories (`cd`, `ls`/`dir`)
  - Run Python scripts
  - Basic file operations

- **HTML/CSS**
  - Basic HTML structure
  - CSS selectors
  - Understanding of web pages

### Nice to Have

- JavaScript basics
- HTTP/REST API concepts
- Git version control
- Virtual environments in Python

## Checking Your System

### Python Installation

```bash
# Check Python version
python --version
# or
python3 --version

# Check pip
pip --version
# or
pip3 --version
```

### Install uv (Recommended)

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify Installation

```bash
# Create test virtual environment
uv venv test-env
source test-env/bin/activate  # macOS/Linux
# or test-env\Scripts\activate  # Windows

# Test Flask installation
uv add flask
python -c "import flask; print(f'Flask {flask.__version__} works!')"

# Clean up
deactivate
rm -rf test-env
```

## Network Requirements

### For Web Development

- Internet access for:
  - Downloading dependencies
  - Accessing documentation
  - Testing external APIs (optional)

### For Pico Development

- **Local Network**
  - Computer and Pico W on same network
  - Router access for troubleshooting
  - Ability to determine local IP addresses

- **WiFi Requirements**
  - 2.4 GHz frequency band
  - WPA2-Personal security (most common)
  - No enterprise authentication
  - No captive portal

## Development Environment

### Text Editor/IDE

Choose one:

- **VS Code** (Recommended for web development)
  - Python extension
  - Syntax highlighting
  - Integrated terminal

- **PyCharm** (Full-featured IDE)
  - Community or Professional edition
  - Built-in Python support

- **Thonny** (For Pico development)
  - Simple, beginner-friendly
  - Built-in Pico support
  - [Installation Guide](../guides/thonny_installation.md)

- **Any text editor**
  - Sublime Text, Atom, Vim, etc.
  - As long as you can edit Python files

### Terminal/Command Prompt

- **macOS**: Terminal (built-in)
- **Windows**: Command Prompt, PowerShell, or Windows Terminal
- **Linux**: Any terminal emulator

## Optional Tools

### Development

- **Postman** or **Insomnia**
  - For testing API endpoints
  - Not required (can use curl or browser)

- **Browser DevTools**
  - Built into all modern browsers
  - Press F12 to open

### Version Control

- **Git**
  - Track changes
  - Collaborate with others
  - Optional but recommended

### Documentation

- **MkDocs** (included in project dependencies)
  - For viewing documentation locally
  - Installed via `uv add mkdocs mkdocs-material`

## Troubleshooting Prerequisites

### Can't Install Python

- **Windows**: Download from [python.org](https://python.org)
- **macOS**: Use Homebrew: `brew install python@3.12`
- **Linux**: Use package manager: `sudo apt install python3.12`

### Permission Errors

- Don't use `sudo` with pip/uv
- Use virtual environments
- Check user permissions

### USB/Serial Issues (Pico)

- **Linux**: Add user to dialout group
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- **macOS**: Check system preferences → Security
- **Windows**: Install drivers from Raspberry Pi

## Ready to Start?

Once you have:

- ✅ Python 3.12+ installed
- ✅ uv or pip available
- ✅ Text editor ready
- ✅ Terminal/command prompt accessible
- ✅ (Optional) Raspberry Pi Pico W and USB cable

You're ready to proceed to the [Quick Start Guide](quickstart.md)!

## Need Help?

- [Installation Issues](../troubleshooting/common_issues.md)
- [Thonny Installation](../guides/thonny_installation.md)
- [System-specific guides](../guides/thonny_installation.md)
