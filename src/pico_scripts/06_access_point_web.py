"""
Raspberry Pi Pico W as WiFi Access Point with Web Interface

This script configures the Pico W as a WiFi access point and serves a web page
that allows you to control the onboard LED (turn it on/off).

Hardware:
- Raspberry Pi Pico W (WiFi required)
- Onboard LED

Features:
- Creates a WiFi access point
- Serves a web interface on the access point's IP
- Allows LED control via web buttons
- Simple HTTP server implementation

Default Access Point Settings:
- SSID: PicoW-LED-Control
- Password: pico12345
- IP Address: 192.168.4.1

Usage:
1. Upload this script to your Raspberry Pi Pico W
2. Run it in Thonny or save as main.py for autostart
3. Connect to the "PicoW-LED-Control" WiFi network (password: pico12345)
4. Open browser and navigate to http://192.168.4.1
5. Use the web interface to control the LED
"""

import network
import socket
import time
import machine

# Access Point Configuration
AP_SSID = "PicoW-LED-Control"
AP_PASSWORD = "pico12345"  # Minimum 8 characters required
AP_CHANNEL = 11

# LED
led = machine.Pin("LED", machine.Pin.OUT)

# LED state
led_state = False


def create_access_point(ssid, password, channel=11):
    """
    Create a WiFi access point.

    Args:
        ssid (str): Access point name
        password (str): Access point password (min 8 chars)
        channel (int): WiFi channel (1-11)

    Returns:
        network.WLAN: Access point object, or None if failed
    """
    print("=" * 60)
    print("Creating WiFi Access Point")
    print("=" * 60)

    # Create access point interface
    ap = network.WLAN(network.AP_IF)
    ap.active(True)

    # Configure access point
    ap.config(essid=ssid, password=password, channel=channel)

    # Wait for AP to become active
    timeout = 10
    start_time = time.time()

    while not ap.active():
        if time.time() - start_time > timeout:
            print("Failed to activate access point")
            return None
        time.sleep(0.5)

    print(f"\nAccess Point created successfully!")
    print(f"SSID: {ssid}")
    print(f"Password: {password}")
    print(f"Channel: {channel}")

    # Get IP configuration
    ip_config = ap.ifconfig()
    print(f"\nNetwork Configuration:")
    print(f"  IP Address: {ip_config[0]}")
    print(f"  Subnet Mask: {ip_config[1]}")
    print(f"  Gateway: {ip_config[2]}")
    print(f"  DNS Server: {ip_config[3]}")
    print("=" * 60)

    return ap


def generate_html():
    """
    Generate HTML page for LED control.

    Returns:
        str: HTML content
    """
    led_status = "ON" if led_state else "OFF"
    led_color = "#4CAF50" if led_state else "#f44336"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pico W LED Control</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        .container {{
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 500px;
            width: 100%;
            text-align: center;
        }}
        h1 {{
            color: #333;
            margin-bottom: 10px;
        }}
        .subtitle {{
            color: #666;
            margin-bottom: 30px;
        }}
        .led-status {{
            background: {led_color};
            color: white;
            padding: 20px;
            border-radius: 10px;
            font-size: 2rem;
            font-weight: bold;
            margin: 20px 0;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }}
        .controls {{
            display: flex;
            gap: 15px;
            margin: 30px 0;
        }}
        .btn {{
            flex: 1;
            padding: 15px;
            font-size: 1.1rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
            color: white;
        }}
        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }}
        .btn-on {{
            background: #4CAF50;
        }}
        .btn-on:hover {{
            background: #45a049;
        }}
        .btn-off {{
            background: #f44336;
        }}
        .btn-off:hover {{
            background: #da190b;
        }}
        .info {{
            background: #f7fafc;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            text-align: left;
        }}
        .info p {{
            color: #4a5568;
            margin: 8px 0;
        }}
        footer {{
            margin-top: 20px;
            padding-top: 20px;
            border-top: 2px solid #e2e8f0;
            color: #718096;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔌 Pico W LED Control</h1>
        <p class="subtitle">Raspberry Pi Pico W Access Point</p>

        <div class="led-status">
            LED: {led_status}
        </div>

        <div class="controls">
            <a href="/led/on" class="btn btn-on">Turn ON</a>
            <a href="/led/off" class="btn btn-off">Turn OFF</a>
        </div>

        <div class="info">
            <p><strong>Network:</strong> {AP_SSID}</p>
            <p><strong>Device:</strong> Raspberry Pi Pico W</p>
            <p><strong>Status:</strong> Connected</p>
        </div>

        <footer>
            <p>Seminar: Nummernsender im Internet</p>
        </footer>
    </div>
</body>
</html>
"""
    return html


def handle_request(client_socket, request):
    """
    Handle HTTP request and generate response.

    Args:
        client_socket: Client socket connection
        request (str): HTTP request string
    """
    global led_state

    # Parse request
    try:
        request_line = request.split('\n')[0]
        method, path, _ = request_line.split()

        print(f"Request: {method} {path}")

        # Handle LED control
        if path == "/led/on":
            led.on()
            led_state = True
            print("LED turned ON")

        elif path == "/led/off":
            led.off()
            led_state = False
            print("LED turned OFF")

        # Generate response
        html = generate_html()
        response = f"""HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html)}
Connection: close

{html}"""

        client_socket.send(response.encode())

    except Exception as error:
        print(f"Error handling request: {error}")

        error_html = "<html><body><h1>Error</h1><p>Bad request</p></body></html>"
        response = f"""HTTP/1.1 400 Bad Request
Content-Type: text/html
Content-Length: {len(error_html)}
Connection: close

{error_html}"""
        client_socket.send(response.encode())


def start_web_server(ip_address, port=80):
    """
    Start HTTP server to handle web requests.

    Args:
        ip_address (str): IP address to bind to
        port (int): Port number (default 80)
    """
    print(f"\nStarting web server on {ip_address}:{port}")
    print("=" * 60)

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip_address, port))
    server_socket.listen(5)

    print(f"Web server running!")
    print(f"Connect to WiFi: {AP_SSID}")
    print(f"Then open browser to: http://{ip_address}")
    print("=" * 60)
    print("\nWaiting for connections...\n")

    try:
        connection_count = 0

        while True:
            # Accept connection
            client_socket, client_address = server_socket.accept()
            connection_count += 1

            print(f"\n[Connection #{connection_count}] Client: {client_address[0]}:{client_address[1]}")

            try:
                # Receive request
                request = client_socket.recv(1024).decode()

                if request:
                    # Handle request
                    handle_request(client_socket, request)

            except Exception as error:
                print(f"Error processing request: {error}")

            finally:
                # Close connection
                client_socket.close()

    except KeyboardInterrupt:
        print(f"\n\nServer stopped by user")
        print(f"Total connections handled: {connection_count}")

    finally:
        server_socket.close()
        led.off()


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Raspberry Pi Pico W - Access Point Web Server")
    print("=" * 60)

    # Create access point
    ap = create_access_point(AP_SSID, AP_PASSWORD, AP_CHANNEL)

    if ap:
        # Get IP address
        ip_address = ap.ifconfig()[0]

        # Blink LED to indicate ready
        for _ in range(3):
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)

        # Start web server
        start_web_server(ip_address)
    else:
        print("\nFailed to create access point")
        led.off()
