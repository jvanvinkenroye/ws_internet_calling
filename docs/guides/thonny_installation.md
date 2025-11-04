# Thonny IDE Installation Guide

Thonny is a beginner-friendly Python IDE that has excellent support for programming Raspberry Pi Pico devices. This guide covers installation on macOS, Windows, and Linux.

## What is Thonny?

Thonny is a Python IDE designed for beginners, featuring:
- Simple and clean interface
- Built-in Python interpreter
- Excellent support for MicroPython and Raspberry Pi Pico
- Easy file management between your computer and Pico
- Real-time code execution and debugging

## System Requirements

- **macOS**: macOS 10.13 (High Sierra) or later
- **Windows**: Windows 7 or later
- **Linux**: Most modern distributions (Ubuntu 18.04+, Debian 10+, Fedora 30+, etc.)
- **RAM**: Minimum 2 GB (4 GB recommended)
- **Disk Space**: ~200 MB for Thonny installation

---

## Installation on macOS

### Method 1: Official Installer (Recommended)

1. **Download Thonny**
   - Visit [https://thonny.org](https://thonny.org)
   - Click on the macOS download link
   - Download the `.pkg` installer file

2. **Install Thonny**
   - Open the downloaded `.pkg` file
   - Follow the installation wizard
   - Enter your password when prompted
   - Click "Install" to complete the installation

3. **Launch Thonny**
   - Open Thonny from Applications folder
   - Or use Spotlight (Cmd + Space) and type "Thonny"

4. **Verify Installation**
   ```bash
   # Open Terminal and check version
   /Applications/Thonny.app/Contents/MacOS/thonny --version
   ```

### Method 2: Homebrew

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Thonny using Homebrew Cask
brew install --cask thonny

# Launch Thonny
open -a Thonny
```

### macOS Troubleshooting

**Issue: "Thonny cannot be opened because the developer cannot be verified"**

Solution:
1. Go to System Preferences → Security & Privacy
2. Click "Open Anyway" next to the Thonny warning
3. Or right-click Thonny.app → Open → Click "Open"

**Issue: Permission denied when accessing USB**

Solution:
```bash
# Grant Terminal access to USB devices
sudo dseditgroup -o edit -a $(whoami) -t user dialout
# Restart your Mac
```

---

## Installation on Windows

### Method 1: Official Installer (Recommended)

1. **Download Thonny**
   - Visit [https://thonny.org](https://thonny.org)
   - Click on the Windows download link
   - Download the `.exe` installer (choose 32-bit or 64-bit based on your system)

2. **Check Your Windows Architecture**
   - Press `Win + Pause/Break`
   - Look for "System type"
   - Download the matching installer

3. **Install Thonny**
   - Double-click the downloaded `.exe` file
   - Click "Yes" if prompted by User Account Control
   - Choose installation options:
     - "Install for me only" (recommended) or "Install for all users"
     - Default installation directory: `C:\Users\<YourName>\AppData\Local\Programs\Thonny`
   - Click "Install"

4. **Launch Thonny**
   - Find Thonny in Start Menu
   - Or create a desktop shortcut during installation

5. **Verify Installation**
   ```cmd
   # Open Command Prompt and check version
   thonny --version
   ```

### Method 2: Windows Package Manager (winget)

```powershell
# Install using Windows Package Manager
winget install AivarAnnamaa.Thonny

# Launch Thonny
thonny
```

### Windows Troubleshooting

**Issue: "USB device not recognized"**

Solution:
1. Install Pico drivers manually
2. Download from [Raspberry Pi Pico documentation](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
3. Restart your computer

**Issue: Thonny doesn't start**

Solution:
- Make sure you have admin rights
- Temporarily disable antivirus software
- Re-download installer and try again

---

## Installation on Linux

### Ubuntu/Debian-based Distributions

```bash
# Update package list
sudo apt update

# Install Thonny
sudo apt install thonny -y

# Launch Thonny
thonny &
```

### Fedora/RHEL-based Distributions

```bash
# Install Thonny
sudo dnf install thonny -y

# Launch Thonny
thonny &
```

### Arch Linux

```bash
# Install from AUR
yay -S thonny

# Or using pacman (if available in repos)
sudo pacman -S thonny

# Launch Thonny
thonny &
```

### Installing from Python pip (All Linux Distributions)

```bash
# Install pip if not already installed
sudo apt install python3-pip python3-tk  # Ubuntu/Debian
# OR
sudo dnf install python3-pip python3-tkinter  # Fedora
# OR
sudo pacman -S python-pip tk  # Arch

# Install Thonny using pip
pip3 install thonny

# Launch Thonny
thonny &
```

### Installing via Snap (Ubuntu and Snap-enabled Distributions)

Snap is a universal package manager available on Ubuntu and many other Linux distributions. Installing Thonny via snap is convenient, but requires an additional step to enable USB access.

#### Installation Steps

```bash
# Install Thonny from Snap Store
sudo snap install thonny

# Launch Thonny
thonny &
```

#### **CRITICAL: Enable USB Access for Snap**

By default, snap applications run in a sandboxed environment and **cannot access USB devices**. You **must** connect the `raw-usb` interface to allow Thonny to communicate with your Raspberry Pi Pico:

```bash
# Connect the raw-usb interface (required for USB serial communication)
sudo snap connect thonny:raw-usb

# Verify the connection
snap connections thonny | grep raw-usb
```

You should see output similar to:
```
raw-usb              thonny:raw-usb             :raw-usb                -
```

#### **Connecting to Raspberry Pi Pico via USB**

After enabling USB access:

1. **Connect your Pico**
   - Plug your Raspberry Pi Pico into a USB port using a data cable (not power-only)
   - The Pico should be recognized by the system

2. **Verify USB Detection**
   ```bash
   # Check if the Pico is detected
   ls -l /dev/ttyACM*
   # You should see something like: /dev/ttyACM0

   # Or check USB devices
   lsusb | grep "2e8a"
   # Should show: "Raspberry Pi RP2 Boot" or "MicroPython Board"
   ```

3. **Configure Thonny for Pico**
   - Launch Thonny
   - Go to `Tools` → `Options` → `Interpreter`
   - Select **"MicroPython (Raspberry Pi Pico)"**
   - Port should auto-detect as `/dev/ttyACM0` (or similar)
   - Click **"OK"**

4. **Verify Connection**
   - You should see `>>>` prompt in the Shell panel at the bottom
   - Bottom-right corner should show "MicroPython" and the port
   - Try typing: `print("Hello Pico!")` in the Shell

#### **Snap-Specific Troubleshooting**

**Issue: Thonny doesn't detect the Pico after snap installation**

This is almost always due to missing USB permissions. Solutions:

```bash
# 1. Ensure raw-usb interface is connected
sudo snap connect thonny:raw-usb

# 2. Add your user to dialout and tty groups
sudo usermod -a -G dialout $USER
sudo usermod -a -G tty $USER

# 3. Log out and log back in (or reboot)
# This is necessary for group changes to take effect

# 4. Verify group membership
groups
# Should include: dialout tty

# 5. Check snap interface connections
snap connections thonny

# 6. Restart snap services (if still not working)
sudo systemctl restart snapd
```

**Issue: "Permission denied" error when accessing /dev/ttyACM0**

```bash
# Check device permissions
ls -l /dev/ttyACM0

# Should show group ownership as 'dialout'
# If you're not in the dialout group, add yourself:
sudo usermod -a -G dialout $USER

# Create udev rule for Pico (if needed)
sudo tee /etc/udev/rules.d/99-pico.rules > /dev/null <<EOF
SUBSYSTEMS=="usb", ATTRS{idVendor}=="2e8a", MODE:="0666", GROUP="dialout"
EOF

# Reload udev rules
sudo udevadm control --reload-rules
sudo udevadm trigger

# Unplug and replug the Pico
```

**Issue: Snap version is outdated**

```bash
# Update Thonny snap to latest version
sudo snap refresh thonny

# Or switch to a different channel (e.g., latest/edge for newer features)
sudo snap refresh thonny --channel=latest/edge
```

**Issue: Need to remove snap version and use apt instead**

If snap version continues to have USB issues, you can switch to apt:

```bash
# Remove snap version
sudo snap remove thonny

# Install via apt
sudo apt update
sudo apt install thonny -y
```

### Linux Troubleshooting

**Issue: Permission denied when accessing USB/serial ports**

Solution:
```bash
# Add your user to dialout group
sudo usermod -a -G dialout $USER

# Add to tty group as well
sudo usermod -a -G tty $USER

# Log out and log back in (or reboot)
# Verify group membership
groups
```

**Issue: Thonny doesn't detect Raspberry Pi Pico**

Solution:
```bash
# Install serial port tools
sudo apt install python3-serial

# Check if device is detected
ls -l /dev/ttyACM*
# or
ls -l /dev/ttyUSB*

# Create udev rule for Pico
sudo nano /etc/udev/rules.d/99-pico.rules

# Add this line:
# SUBSYSTEMS=="usb", ATTRS{idVendor}=="2e8a", MODE:="0666"

# Reload udev rules
sudo udevadm control --reload-rules
sudo udevadm trigger

# Unplug and replug the Pico
```

---

## First-Time Setup (All Platforms)

After installing Thonny, follow these steps:

1. **Launch Thonny**
   - Start the application

2. **Select Interface Language**
   - Choose your preferred language
   - Click "Let's go!"

3. **Configure for Raspberry Pi Pico**
   - Go to `Tools` → `Options` → `Interpreter`
   - Select "MicroPython (Raspberry Pi Pico)"
   - Port should be auto-detected
   - Click "OK"

4. **Verify Connection**
   - Connect your Raspberry Pi Pico via USB
   - Look for "MicroPython" in the bottom-right corner
   - You should see `>>>` prompt in the Shell

5. **Test Installation**
   ```python
   # Type this in the Shell:
   print("Hello from Thonny!")
   ```

---

## Updating Thonny

### macOS
```bash
# If installed via Homebrew:
brew upgrade thonny

# If installed via .pkg:
# Download and install the latest .pkg from thonny.org
```

### Windows
```powershell
# If installed via winget:
winget upgrade AivarAnnamaa.Thonny

# If installed via .exe:
# Download and run the latest installer from thonny.org
```

### Linux
```bash
# Ubuntu/Debian:
sudo apt update && sudo apt upgrade thonny

# Fedora:
sudo dnf upgrade thonny

# Via pip:
pip3 install --upgrade thonny
```

---

## Next Steps

After successfully installing Thonny:

1. **[Flash Raspberry Pi Pico](pico_flashing.md)** - Set up your Pico with MicroPython
2. **[Run Example Scripts](../pico/introduction.md)** - Try the sample code
3. **[Troubleshooting](../troubleshooting/common_issues.md)** - Solutions to common problems

---

## Additional Resources

- **Official Thonny Website**: [https://thonny.org](https://thonny.org)
- **Thonny Documentation**: [https://github.com/thonny/thonny/wiki](https://github.com/thonny/thonny/wiki)
- **Raspberry Pi Pico Documentation**: [https://www.raspberrypi.com/documentation/microcontrollers/](https://www.raspberrypi.com/documentation/microcontrollers/)
- **MicroPython Documentation**: [https://docs.micropython.org/](https://docs.micropython.org/)

---

## Support

If you encounter issues not covered in this guide:

1. Check the [Troubleshooting Guide](../troubleshooting/common_issues.md)
2. Visit the [Thonny Forum](https://github.com/thonny/thonny/discussions)
3. Check the [Raspberry Pi Forums](https://forums.raspberrypi.com/)
