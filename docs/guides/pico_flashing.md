# Raspberry Pi Pico Flashing Guide

This comprehensive guide covers how to flash MicroPython firmware onto your Raspberry Pi Pico and upload your first program.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Understanding Raspberry Pi Pico](#understanding-raspberry-pi-pico)
3. [Method 1: Flashing with Thonny (Recommended)](#method-1-flashing-with-thonny-recommended)
4. [Method 2: Manual Flashing](#method-2-manual-flashing)
5. [Uploading Your First Program](#uploading-your-first-program)
6. [Setting Up Autostart](#setting-up-autostart)
7. [File Management](#file-management)
8. [Common Issues](#common-issues)

---

## Prerequisites

Before you begin, make sure you have:

- ✅ Raspberry Pi Pico or Pico W
- ✅ Micro USB cable (data cable, not charging-only)
- ✅ Computer with USB port
- ✅ Thonny IDE installed ([Installation Guide](thonny_installation.md))
- ✅ Internet connection (to download firmware)

---

## Understanding Raspberry Pi Pico

### Raspberry Pi Pico Specifications

| Feature | Specification |
|---------|--------------|
| Microcontroller | RP2040 (Raspberry Pi custom chip) |
| CPU | Dual-core ARM Cortex-M0+ @ 133MHz |
| RAM | 264KB SRAM |
| Flash Memory | 2MB |
| GPIO Pins | 26 multi-function pins |
| PWM Channels | 16 |
| ADC | 3 channels, 12-bit |
| UART, SPI, I2C | Multiple interfaces |
| USB | 1x USB 1.1 controller |
| Temperature Sensor | Built-in |

### Pico vs Pico W

- **Pico**: Standard version without wireless
- **Pico W**: Includes WiFi and Bluetooth (via Infineon CYW43439)

### Boot Modes

The Pico has two boot modes:

1. **BOOTSEL Mode** (USB Mass Storage)
   - Appears as a USB drive
   - Used for flashing firmware
   - Accessed by holding BOOTSEL button while plugging in

2. **Normal Mode** (Running Code)
   - Executes uploaded MicroPython code
   - Regular operation mode

---

## Method 1: Flashing with Thonny (Recommended)

This is the easiest method for beginners.

### Step 1: Enter BOOTSEL Mode

1. **Disconnect** the Pico from your computer (if connected)
2. **Locate** the BOOTSEL button on the Pico (small white button near the USB port)
3. **Press and hold** the BOOTSEL button
4. **While holding** the button, connect the Pico to your computer via USB
5. **Release** the BOOTSEL button after 2 seconds

**Result**: The Pico appears as a USB drive named "RPI-RP2"

*The BOOTSEL button is a small white button located near the USB port on the Pico board.*

### Step 2: Flash Firmware via Thonny

1. **Launch Thonny IDE**

2. **Check Connection**
   - The Pico should be detected as "RPI-RP2" drive

3. **Install MicroPython Firmware**
   - Click `Tools` → `Options`
   - Select the `Interpreter` tab
   - Choose "MicroPython (Raspberry Pi Pico)" or "MicroPython (Raspberry Pi Pico W)"
   - Click `Install or update MicroPython`

4. **Configure Installation**
   - **Target volume**: Select "RPI-RP2" drive
   - **MicroPython variant**:
     - For Pico: "Raspberry Pi Pico / Pico H"
     - For Pico W: "Raspberry Pi Pico W / Pico WH"
   - **Version**: Select the latest stable version
   - Click `Install`

5. **Wait for Completion**
   - Installation takes 10-30 seconds
   - Don't disconnect during installation
   - Pico will restart automatically

6. **Verify Installation**
   - After restart, Thonny's Shell should show:
   ```
   MicroPython v1.x.x on YYYY-MM-DD; Raspberry Pi Pico with RP2040
   Type "help()" for more information.
   >>>
   ```

7. **Test with Simple Code**
   ```python
   >>> print("Hello, Pico!")
   Hello, Pico!
   ```

---

## Method 2: Manual Flashing

Advanced method for those who prefer manual control.

### Step 1: Download MicroPython Firmware

1. **Visit MicroPython Download Page**
   - Go to [https://micropython.org/download/](https://micropython.org/download/)

2. **Select Your Device**
   - For Pico: [Raspberry Pi Pico](https://micropython.org/download/rp2-pico/)
   - For Pico W: [Raspberry Pi Pico W](https://micropython.org/download/rp2-pico-w/)

3. **Download Latest .UF2 File**
   - Click on the latest stable release
   - Save the `.uf2` file (e.g., `rp2-pico-latest.uf2`)

### Step 2: Enter BOOTSEL Mode

Follow the same steps as Method 1, Step 1.

### Step 3: Copy Firmware to Pico

1. **Locate RPI-RP2 Drive**
   - macOS: Check Finder sidebar
   - Windows: Check "This PC"
   - Linux: Usually mounted in `/media/` or `/mnt/`

2. **Copy UF2 File**
   - Drag and drop the `.uf2` file to the RPI-RP2 drive
   - Or use command line:

   ```bash
   # macOS/Linux
   cp rp2-pico-latest.uf2 /Volumes/RPI-RP2/

   # Linux (adjust mount point)
   cp rp2-pico-latest.uf2 /media/$USER/RPI-RP2/
   ```

   ```cmd
   # Windows (adjust drive letter)
   copy rp2-pico-latest.uf2 D:\
   ```

3. **Wait for Auto-Reset**
   - The Pico will automatically reboot
   - RPI-RP2 drive will disappear
   - Flashing is complete!

### Step 4: Verify in Thonny

1. Open Thonny
2. Go to `Tools` → `Options` → `Interpreter`
3. Select "MicroPython (Raspberry Pi Pico)"
4. Port should auto-detect
5. Click OK
6. Check Shell for MicroPython prompt `>>>`

---

## Uploading Your First Program

### Using Thonny

1. **Create New File**
   - Click `File` → `New`

2. **Write Code**
   ```python
   # blink.py - Simple LED blink example
   import machine
   import time

   led = machine.Pin("LED", machine.Pin.OUT)

   while True:
       led.toggle()
       time.sleep(0.5)
   ```

3. **Save to Pico**
   - Click `File` → `Save as...`
   - Select "Raspberry Pi Pico"
   - Name it `blink.py`
   - Click OK

4. **Run the Program**
   - Click the green `Run` button (F5)
   - Or click `Run` → `Run current script`
   - The LED should start blinking!

5. **Stop the Program**
   - Click the red `Stop` button
   - Or press `Ctrl+C` in the Shell

---

## Setting Up Autostart

To make your program run automatically when the Pico powers on:

### Method: Rename to main.py

1. **Save or Rename Your Script**
   - In Thonny, save your working script as `main.py`
   - Or rename existing file on Pico to `main.py`

2. **Upload to Pico**
   - Make sure `main.py` is saved to the Pico (not your computer)

3. **Test Autostart**
   - Disconnect the Pico from USB
   - Reconnect it (without holding BOOTSEL)
   - The program should start automatically

### Example: Autostart Blink

```python
# main.py - Autostart LED blink
import machine
import time

led = machine.Pin("LED", machine.Pin.OUT)

print("Autostart: LED blink program")
print("Press Ctrl+C to stop")

try:
    while True:
        led.toggle()
        time.sleep(0.5)
except KeyboardInterrupt:
    led.off()
    print("Program stopped")
```

**To disable autostart:**
- Delete or rename `main.py` on the Pico
- Or add a long delay at the start and interrupt with Ctrl+C

---

## File Management

### Viewing Files on Pico

In Thonny:
1. Click `View` → `Files`
2. You'll see two file browsers:
   - **This computer**: Your local files
   - **Raspberry Pi Pico**: Files on the Pico

### Uploading Files

**Drag and drop:**
- Drag files from "This computer" to "Raspberry Pi Pico"

**Or use menu:**
- Right-click file in "This computer"
- Select "Upload to /"

### Downloading Files

- Right-click file in "Raspberry Pi Pico"
- Select "Download to..."
- Choose destination on your computer

### Deleting Files

- Right-click file in "Raspberry Pi Pico"
- Select "Delete"
- Confirm deletion

### Creating Directories

- Right-click in "Raspberry Pi Pico" area
- Select "New directory"
- Enter directory name

---

## Common Issues

### Pico Not Detected

**Symptoms:**
- RPI-RP2 drive doesn't appear
- Thonny can't find Pico

**Solutions:**
1. Try a different USB cable (must be data cable, not charge-only)
2. Try a different USB port
3. Make sure you're holding BOOTSEL while connecting
4. Check [Troubleshooting Guide](../troubleshooting/common_issues.md)

### Upload Failed

**Symptoms:**
- "Could not write to port" error
- Upload hangs indefinitely

**Solutions:**
1. Reconnect the Pico
2. Restart Thonny
3. Check port permissions (Linux/macOS)
4. Re-flash MicroPython firmware

### Code Runs Once Then Stops

**Symptoms:**
- Program runs in Thonny but not on restart

**Solutions:**
1. Make sure file is saved as `main.py`
2. Check file is on Pico, not your computer
3. Add error handling to catch and print exceptions

### Import Errors

**Symptoms:**
- `ImportError: no module named 'xxx'`

**Solutions:**
1. Some modules are not available in MicroPython
2. Check [MicroPython documentation](https://docs.micropython.org/)
3. Use MicroPython-specific libraries

---

## File Size Limitations

The Pico has **2MB** of flash storage:
- MicroPython firmware: ~500KB
- Available for your code: ~1.5MB

**Tips:**
- Keep code files small and modular
- Delete unused files
- Use `.mpy` compiled files for larger libraries

---

## Next Steps

Now that you've flashed your Pico:

1. **Try Example Scripts** - Run the provided examples
   - [01_blink.py](../../src/pico_scripts/01_blink.py)
   - [02_wifi_connect.py](../../src/pico_scripts/02_wifi_connect.py)

2. **Explore MicroPython** - Learn the differences from standard Python
   - [MicroPython Documentation](https://docs.micropython.org/)

3. **Build Projects** - Try the seminar projects
   - WiFi signal monitor
   - API consumer
   - Access point web server

---

## Additional Resources

- **Raspberry Pi Pico Getting Started**: [Official PDF Guide](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
- **MicroPython Forum**: [https://forum.micropython.org/](https://forum.micropython.org/)
- **Raspberry Pi Forums**: [https://forums.raspberrypi.com/](https://forums.raspberrypi.com/)
- **Pico SDK Documentation**: [https://raspberrypi.github.io/pico-sdk-doxygen/](https://raspberrypi.github.io/pico-sdk-doxygen/)

---

## Troubleshooting

For more detailed troubleshooting, see the [Troubleshooting Guide](../troubleshooting/common_issues.md).
