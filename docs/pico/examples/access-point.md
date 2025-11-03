# Access Point with Web Interface

Create a WiFi access point on Pico W and serve a web page for LED control.

## Overview

This advanced example demonstrates how to configure the Pico W as a WiFi access point and serve a complete web interface for controlling the onboard LED.

## Source Code

**File**: `src/pico_scripts/06_access_point_web.py`

## Features

- WiFi Access Point mode
- HTTP web server
- Responsive HTML interface
- LED control via web buttons
- DHCP IP assignment
- Error handling
- Clean shutdown

## Hardware Requirements

- Raspberry Pi Pico W (WiFi required)
- Onboard LED
- No external components needed

## Default Configuration

```python
AP_SSID = "PicoW-LED-Control"
AP_PASSWORD = "pico12345"  # Min 8 characters
AP_CHANNEL = 11
IP_ADDRESS = "192.168.4.1"  # Default AP IP
```

## Code Explanation

### Create Access Point

```python
import network

def create_access_point(ssid, password, channel=11):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password, channel=channel)

    while not ap.active():
        time.sleep(0.5)

    return ap
```

### Web Server

```python
import socket

def start_web_server(ip_address, port=80):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip_address, port))
    server_socket.listen(5)

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024).decode()

        handle_request(client_socket, request)
        client_socket.close()
```

### LED Control Endpoints

```python
def handle_request(client_socket, request):
    path = request.split()[1]

    if path == "/led/on":
        led.on()
        led_state = True
    elif path == "/led/off":
        led.off()
        led_state = False

    html = generate_html()
    response = f"""HTTP/1.1 200 OK
Content-Type: text/html

{html}"""
    client_socket.send(response.encode())
```

### HTML Interface

The script generates a responsive web page with:
- Modern design with gradients
- LED status display
- ON/OFF control buttons
- Network information
- Mobile-friendly layout

## Usage

### 1. Upload Script

1. Open `06_access_point_web.py` in Thonny
2. Upload to Pico W
3. Run the script

### 2. Connect to Access Point

**From any device (phone, tablet, laptop):**

1. Open WiFi settings
2. Look for network: **PicoW-LED-Control**
3. Connect using password: **pico12345**
4. Wait for connection (may take 10-20 seconds)

### 3. Access Web Interface

1. Open web browser
2. Navigate to: **http://192.168.4.1**
3. The LED control page should load
4. Click buttons to control LED

## Expected Output (Console)

```
============================================================
Raspberry Pi Pico W - Access Point Web Server
============================================================
============================================================
Creating WiFi Access Point
============================================================

Access Point created successfully!
SSID: PicoW-LED-Control
Password: pico12345
Channel: 11

Network Configuration:
  IP Address: 192.168.4.1
  Subnet Mask: 255.255.255.0
  Gateway: 192.168.4.1
  DNS Server: 192.168.4.1
============================================================

Starting web server on 192.168.4.1:80
============================================================
Web server running!
Connect to WiFi: PicoW-LED-Control
Then open browser to: http://192.168.4.1
============================================================

Waiting for connections...

[Connection #1] Client: 192.168.4.2:54321
Request: GET / HTTP/1.1

[Connection #2] Client: 192.168.4.2:54322
Request: GET /led/on HTTP/1.1
LED turned ON
```

## Web Interface Features

### LED Status Display

- **Green background**: LED is ON
- **Red background**: LED is OFF
- Large, clear status text

### Control Buttons

- **Turn ON**: Green button, turns LED on
- **Turn OFF**: Red button, turns LED off
- Instant feedback on click

### Network Information

- Access point name
- Device type
- Connection status

## Customization

### Change Network Name

```python
AP_SSID = "MyCustomName"
AP_PASSWORD = "MySecurePassword123"
```

### Change IP Address

```python
# In create_access_point():
ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '192.168.4.1'))
```

### Modify Web Page

Edit the `generate_html()` function to customize:
- Colors and styling
- Button text
- Additional controls
- Page layout

## Advanced Features

### Add More LED Patterns

```python
if path == "/led/blink":
    for _ in range(5):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
```

### Add Status API

```python
if path == "/api/status":
    response = f"""HTTP/1.1 200 OK
Content-Type: application/json

{{"led_state": {led_state}, "uptime": {time.time()}}}"""
```

### Multiple Clients

The server can handle multiple connections sequentially. For better performance, consider:
- Reducing HTML size
- Minimizing CSS
- Keeping responses fast

## Troubleshooting

### Can't Find WiFi Network

**Check:**
- Pico is powered on
- Script is running (check console)
- Device supports 2.4 GHz WiFi
- Not too far from Pico

**Try:**
- Restart Pico
- Check SSID in console output
- Scan for networks again

### Can't Connect to Network

**Check:**
- Password is correct (min 8 characters)
- WiFi is enabled on device
- No other access point with same name

**Try:**
- Forget network and reconnect
- Restart device WiFi
- Try different device

### Web Page Won't Load

**Check:**
- Connected to PicoW-LED-Control WiFi
- Using correct IP: http://192.168.4.1
- Not using HTTPS (use HTTP only)

**Try:**
- Refresh browser (Ctrl+F5)
- Try different browser
- Check console for connection logs
- Restart web browser

### LED Not Responding

**Check:**
- Web page loads correctly
- Console shows request received
- Correct endpoint (/led/on or /led/off)

**Try:**
- Check console for LED status
- Test LED manually in code
- Restart Pico

## Security Notes

⚠️ **Important Security Considerations:**

- **Change default password** in production
- **No encryption** for web traffic (HTTP, not HTTPS)
- **Basic access only** - no authentication
- **Open network** - anyone can connect with password

For production use, consider:
- Stronger password (12+ characters)
- Adding web authentication
- Implementing HTTPS
- Rate limiting connections

## Use Cases

- **IoT Device Control** - Control hardware remotely
- **Standalone Systems** - No internet required
- **Education** - Learn web servers and networking
- **Prototyping** - Quick web interface testing
- **Remote Monitoring** - Add sensor readings to page

## Performance

- **Connection time**: 10-20 seconds
- **Page load**: < 1 second
- **Response time**: Near instant
- **Concurrent connections**: 1 at a time (sequential)

## Next Steps

- Add sensor readings to web page
- Implement form inputs for settings
- Create API endpoints for automation
- Add real-time updates with AJAX

## Reference

Full source: `src/pico_scripts/06_access_point_web.py`

Related examples:
- [WiFi Connection](wifi-connect.md) - Client mode basics
- [API Consumer](api-consumer.md) - HTTP requests

## Additional Resources

- [MicroPython Network](https://docs.micropython.org/en/latest/library/network.html)
- [MicroPython Socket](https://docs.micropython.org/en/latest/library/socket.html)
- [Pico W Datasheet](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)
