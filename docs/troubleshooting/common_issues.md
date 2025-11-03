# Troubleshooting Guide

This guide covers common issues you might encounter while working with Raspberry Pi Pico, Thonny, and the Number Transmitter project.

## Table of Contents

1. [Thonny Issues](#thonny-issues)
2. [Raspberry Pi Pico Connection Issues](#raspberry-pi-pico-connection-issues)
3. [Flashing and Firmware Issues](#flashing-and-firmware-issues)
4. [WiFi Connection Issues](#wifi-connection-issues)
5. [API and Networking Issues](#api-and-networking-issues)
6. [Code Execution Issues](#code-execution-issues)
7. [Web Application Issues](#web-application-issues)
8. [Performance Issues](#performance-issues)

---

## Thonny Issues

### Thonny Won't Start

**Symptoms:**
- Double-clicking Thonny does nothing
- Application crashes on startup
- Error messages on launch

**Solutions:**

**Windows:**
```cmd
# Try running as administrator
# Right-click Thonny → Run as administrator

# Check if Python is accessible
python --version

# Reinstall Thonny
# Uninstall via Control Panel, then reinstall from thonny.org
```

**macOS:**
```bash
# Check if Thonny is in quarantine
xattr -d com.apple.quarantine /Applications/Thonny.app

# Or remove and reinstall
brew uninstall thonny
brew install --cask thonny

# Check permissions
ls -la /Applications/Thonny.app
```

**Linux:**
```bash
# Run from terminal to see error messages
thonny

# Reinstall dependencies
sudo apt install python3-tk python3-pip
pip3 install --upgrade thonny

# Check file permissions
chmod +x $(which thonny)
```

---

### Thonny Interface Issues

**Symptoms:**
- Missing panels (Shell, Files, Variables)
- UI elements not displaying correctly
- Buttons not working

**Solutions:**

1. **Reset View to Defaults**
   - `View` → `Reset view`
   - Restart Thonny

2. **Check Theme Settings**
   - `Tools` → `Options` → `Theme`
   - Try different themes

3. **Clear Configuration**
   ```bash
   # Backup and remove Thonny config
   # macOS/Linux
   mv ~/.config/Thonny ~/.config/Thonny.backup

   # Windows
   # Delete or rename: %APPDATA%\Thonny
   ```

---

## Raspberry Pi Pico Connection Issues

### Pico Not Detected

**Symptoms:**
- No device shown in Thonny
- "No device found" error
- RPI-RP2 drive doesn't appear

**Solutions:**

1. **Check USB Cable**
   - Use a data cable, not charge-only cable
   - Try different USB cable
   - Test cable with another device

2. **Try Different USB Port**
   - Use USB 2.0 port (avoid USB 3.0 hubs initially)
   - Try direct connection, not through hub
   - Test both front and back ports on desktop

3. **Verify BOOTSEL Mode**
   - Disconnect Pico
   - Hold BOOTSEL button
   - Connect USB while holding
   - Release after 2 seconds
   - Check for RPI-RP2 drive

4. **Check Device Manager (Windows)**
   ```cmd
   # Open Device Manager
   devmgmt.msc

   # Look for:
   # - "USB Serial Device (COMx)" - Normal mode
   # - "RP2 Boot" - BOOTSEL mode
   # - Unknown devices or errors
   ```

5. **Check System Info (macOS)**
   ```bash
   # List USB devices
   system_profiler SPUSBDataType | grep -A 10 "Pico"

   # Check for serial devices
   ls -la /dev/tty.*
   ls -la /dev/cu.*
   ```

6. **Check Devices (Linux)**
   ```bash
   # List USB devices
   lsusb | grep -i "Raspberry\|2e8a"

   # Check serial devices
   ls -la /dev/ttyACM*
   ls -la /dev/ttyUSB*

   # Check dmesg for connection messages
   dmesg | tail -n 50 | grep -i "usb\|tty"
   ```

---

### Permission Denied (Linux/macOS)

**Symptoms:**
- "Permission denied: '/dev/ttyACM0'"
- Can't access serial port
- Upload fails with permission error

**Solutions:**

**Linux:**
```bash
# Add user to dialout group
sudo usermod -a -G dialout $USER
sudo usermod -a -G tty $USER

# Create udev rule
sudo nano /etc/udev/rules.d/99-pico.rules

# Add this line:
SUBSYSTEMS=="usb", ATTRS{idVendor}=="2e8a", MODE:="0666", GROUP="dialout"

# Reload udev
sudo udevadm control --reload-rules
sudo udevadm trigger

# Log out and back in (or reboot)
```

**macOS:**
```bash
# Check permissions
ls -la /dev/cu.usbmodem*

# If needed, grant access
sudo chmod 666 /dev/cu.usbmodem*

# For permanent fix, add user to dialout equivalent
# (macOS doesn't have dialout, but check group memberships)
groups
```

---

## Flashing and Firmware Issues

### Flashing Fails

**Symptoms:**
- "Failed to write firmware"
- Process hangs during flash
- Pico doesn't reboot after flash

**Solutions:**

1. **Verify BOOTSEL Mode**
   - Must be in BOOTSEL mode (RPI-RP2 visible)
   - Try entering BOOTSEL mode again

2. **Try Manual Flashing**
   - Download .uf2 file from micropython.org
   - Drag and drop to RPI-RP2 drive
   - Wait for automatic reboot

3. **Check Disk Space**
   ```bash
   # Make sure your computer has space
   df -h
   ```

4. **Re-download Firmware**
   - Corrupt download might cause issues
   - Download fresh .uf2 file

5. **Try Different Computer**
   - Rule out computer-specific issues

---

### Wrong Firmware Version

**Symptoms:**
- Imports fail for Pico W features
- `network` module not available
- Unexpected module errors

**Solutions:**

1. **Check Current Version**
   ```python
   import sys
   print(sys.version)
   print(sys.implementation)
   ```

2. **Reflash Correct Firmware**
   - Pico W requires Pico W firmware (with WiFi support)
   - Regular Pico uses standard firmware
   - Download correct version from micropython.org

---

## WiFi Connection Issues

### Can't Connect to WiFi

**Symptoms:**
- `wlan.isconnected()` returns False
- Connection timeout
- "Failed to connect" errors

**Solutions:**

1. **Verify Pico W Hardware**
   ```python
   # Check if you have Pico W (not regular Pico)
   import network
   wlan = network.WLAN(network.STA_IF)
   # If this fails, you may have regular Pico (no WiFi)
   ```

2. **Check WiFi Credentials**
   ```python
   # Common mistakes:
   # - Wrong SSID (case-sensitive)
   # - Wrong password (case-sensitive)
   # - Special characters in password
   # - Spaces in SSID/password

   WIFI_SSID = "YourNetwork"  # Exact name
   WIFI_PASSWORD = "YourPassword"  # Exact password
   ```

3. **Check WiFi Network**
   - Pico W supports 2.4 GHz only (not 5 GHz)
   - Check router is broadcasting 2.4 GHz
   - Some enterprise/WPA-Enterprise networks not supported
   - Try personal hotspot for testing

4. **Check Signal Strength**
   - Move Pico closer to router
   - Remove obstacles between Pico and router
   - Check for interference

5. **Debug Connection**
   ```python
   import network
   import time

   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)

   print("Connecting...")
   wlan.connect("SSID", "PASSWORD")

   # Wait and show status
   timeout = 10
   while timeout > 0:
       if wlan.isconnected():
           print("Connected!")
           print(wlan.ifconfig())
           break
       print(f"Status: {wlan.status()}")
       time.sleep(1)
       timeout -= 1

   if not wlan.isconnected():
       print("Failed to connect")
       print(f"Final status: {wlan.status()}")
   ```

6. **Status Code Reference**
   ```python
   # wlan.status() return values:
   # 0 = STAT_IDLE -- no connection and no activity
   # 1 = STAT_CONNECTING -- connecting in progress
   # 2 = STAT_WRONG_PASSWORD -- failed due to incorrect password
   # 3 = STAT_NO_AP_FOUND -- failed because no access point replied
   # 4 = STAT_CONNECT_FAIL -- failed due to other problems
   # 5 = STAT_GOT_IP -- connection successful
   ```

---

### Weak WiFi Signal

**Symptoms:**
- Intermittent connection
- Slow data transfer
- Frequent disconnections

**Solutions:**

1. **Check RSSI**
   ```python
   rssi = wlan.status('rssi')
   print(f"Signal strength: {rssi} dBm")

   # Good: -30 to -60 dBm
   # Weak: -60 to -80 dBm
   # Very weak: below -80 dBm
   ```

2. **Improve Signal**
   - Move Pico closer to router
   - Use external antenna (if supported)
   - Remove metal objects nearby
   - Change WiFi channel on router

---

## API and Networking Issues

### API Not Accessible

**Symptoms:**
- "Connection refused"
- "No route to host"
- Timeout errors

**Solutions:**

1. **Check API Server Running**
   ```bash
   # On API server machine
   curl http://localhost:5001/api/status

   # Should return JSON response
   ```

2. **Check Firewall**
   ```bash
   # macOS - allow Python/Flask
   # Go to System Preferences → Security → Firewall

   # Linux - allow port
   sudo ufw allow 5001

   # Windows - allow in Windows Defender Firewall
   ```

3. **Check Network Connectivity**
   ```python
   # On Pico, ping test
   import urequests

   try:
       response = urequests.get("http://example.com", timeout=5)
       print("Internet works:", response.status_code)
   except Exception as e:
       print("No internet:", e)
   ```

4. **Verify Same Network**
   - Pico and API server must be on same network
   - Check IP addresses in same subnet
   ```python
   # On Pico
   print(wlan.ifconfig()[0])  # Pico IP

   # On server
   # macOS/Linux
   ifconfig
   # Windows
   ipconfig
   ```

5. **Use Correct IP Address**
   ```python
   # Don't use localhost on Pico
   # Use actual IP address of server
   API_BASE_URL = "http://192.168.1.100:5001"  # Replace with actual IP
   ```

---

### CORS Errors (Web Application)

**Symptoms:**
- Browser console shows CORS errors
- "Access-Control-Allow-Origin" errors
- API works in curl but not browser

**Solutions:**

1. **Enable CORS in Flask**
   ```python
   from flask_cors import CORS

   app = Flask(__name__)
   CORS(app)  # Enable CORS for all routes
   ```

2. **Specific Origin**
   ```python
   CORS(app, resources={r"/api/*": {"origins": "*"}})
   ```

---

## Code Execution Issues

### ImportError: No Module

**Symptoms:**
- `ImportError: no module named 'requests'`
- `ImportError: no module named 'flask'`

**Solutions:**

1. **MicroPython vs Python**
   - MicroPython has limited libraries
   - Use `urequests` instead of `requests`
   - Some modules not available

   ```python
   # MicroPython (on Pico)
   import urequests  # Not 'requests'
   import ujson      # Not 'json'

   # Regular Python (on computer)
   import requests
   import json
   ```

2. **Install Missing Packages (Computer)**
   ```bash
   # Activate venv first
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows

   # Install package
   uv add package-name
   # or
   pip install package-name
   ```

---

### Memory Errors on Pico

**Symptoms:**
- `MemoryError`
- Pico crashes or resets
- Code runs once then fails

**Solutions:**

1. **Check Memory Usage**
   ```python
   import gc
   gc.collect()
   print(f"Free memory: {gc.mem_free()} bytes")
   print(f"Allocated: {gc.mem_alloc()} bytes")
   ```

2. **Optimize Code**
   ```python
   # Call garbage collector regularly
   import gc
   gc.collect()

   # Use generators instead of lists
   # Delete large variables when done
   del large_variable
   gc.collect()

   # Avoid string concatenation in loops
   # Use list and join instead
   ```

3. **Simplify Code**
   - Remove debug print statements
   - Use shorter variable names
   - Split large files into modules

---

### Infinite Loops/Hangs

**Symptoms:**
- Code doesn't respond
- Can't stop program
- Thonny frozen

**Solutions:**

1. **Interrupt with Ctrl+C**
   - In Thonny Shell, press Ctrl+C
   - May need to press multiple times

2. **Disconnect/Reconnect**
   - Unplug Pico USB
   - Wait 2 seconds
   - Reconnect

3. **Reset Pico**
   - Press RUN button on Pico (if available)
   - Or disconnect power

4. **Add Safety Timeouts**
   ```python
   import time

   start_time = time.time()
   while True:
       # Your code here

       # Safety timeout
       if time.time() - start_time > 60:  # 60 seconds
           print("Timeout!")
           break
   ```

---

## Web Application Issues

### Flask App Won't Start

**Symptoms:**
- "Address already in use"
- "Permission denied"
- Import errors

**Solutions:**

1. **Port Already in Use**
   ```bash
   # Find process using port 5000
   # macOS/Linux
   lsof -i :5000
   sudo kill -9 <PID>

   # Windows
   netstat -ano | findstr :5000
   taskkill /PID <PID> /F

   # Or use different port
   app.run(port=5001)
   ```

2. **Permission Denied (Port < 1024)**
   ```bash
   # Use port >= 1024
   app.run(port=5000)  # Good

   # Or run with sudo (not recommended)
   sudo python app.py
   ```

3. **Module Import Errors**
   ```bash
   # Make sure venv is activated
   source .venv/bin/activate

   # Install dependencies
   uv add flask flask-cors
   ```

---

### Page Not Loading

**Symptoms:**
- "This site can't be reached"
- "Connection refused"
- Blank page

**Solutions:**

1. **Check Flask is Running**
   ```bash
   # Should see:
   # * Running on http://0.0.0.0:5000
   # * Running on http://127.0.0.1:5000
   ```

2. **Use Correct URL**
   ```
   # Local testing
   http://localhost:5000
   http://127.0.0.1:5000

   # From other devices
   http://<your-ip>:5000
   # e.g., http://192.168.1.100:5000
   ```

3. **Check Browser Console**
   - Press F12 to open developer tools
   - Check Console tab for JavaScript errors
   - Check Network tab for failed requests

---

## Performance Issues

### Slow Response Times

**Symptoms:**
- API responses take too long
- Web page loads slowly
- Pico responses delayed

**Solutions:**

1. **Check Network Latency**
   ```bash
   # Ping test
   ping <pico-ip>
   ping <server-ip>
   ```

2. **Optimize API Queries**
   - Reduce query frequency
   - Cache responses
   - Use smaller data payloads

3. **Reduce Print Statements**
   ```python
   # Remove or reduce print() calls in production
   # Printing to serial is slow
   ```

---

### High CPU Usage

**Symptoms:**
- Computer fan running high
- Flask using lots of CPU
- System slowdown

**Solutions:**

1. **Check for Infinite Loops**
   - Review code for tight loops
   - Add delays in loops

2. **Disable Debug Mode**
   ```python
   # Production
   app.run(debug=False)

   # Development only
   app.run(debug=True)
   ```

3. **Limit Concurrent Requests**
   - Flask development server is single-threaded
   - For production, use gunicorn or similar

---

## Getting Additional Help

If your issue isn't covered here:

1. **Check Project Documentation**
   - Read the relevant guide
   - Review example code

2. **Community Resources**
   - [Raspberry Pi Forums](https://forums.raspberrypi.com/)
   - [MicroPython Forum](https://forum.micropython.org/)
   - [Thonny Issues](https://github.com/thonny/thonny/issues)

3. **Debug Systematically**
   - Isolate the problem
   - Test components individually
   - Add debug print statements
   - Check logs and error messages

4. **Report Issues**
   - Include error messages
   - Specify OS and versions
   - Describe steps to reproduce
   - Include minimal code example

---

## Quick Reference: Common Commands

### Thonny Debug Commands
```python
# Check MicroPython version
import sys
print(sys.version)

# Check memory
import gc
gc.collect()
print(f"Free: {gc.mem_free()}")

# List files
import os
print(os.listdir())

# Check WiFi (Pico W)
import network
wlan = network.WLAN(network.STA_IF)
print(f"Connected: {wlan.isconnected()}")
if wlan.isconnected():
    print(f"IP: {wlan.ifconfig()[0]}")
```

### System Commands
```bash
# Check USB devices (Linux)
lsusb

# Check serial ports (Linux)
ls /dev/ttyACM*

# Check serial ports (macOS)
ls /dev/cu.*

# Check COM ports (Windows)
mode

# Test API
curl http://localhost:5001/api/status
```

---

Need more help? See the [Installation Guide](../guides/thonny_installation.md) or [Flashing Guide](../guides/pico_flashing.md).
