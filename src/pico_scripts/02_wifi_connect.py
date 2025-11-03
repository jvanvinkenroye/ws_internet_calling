"""
WiFi Connection Example for Raspberry Pi Pico W

This script demonstrates how to connect the Raspberry Pi Pico W to a WiFi network
and display the connection status.

Hardware:
- Raspberry Pi Pico W (WiFi required)

Configuration:
- Update WIFI_SSID and WIFI_PASSWORD with your network credentials

Usage:
1. Edit the WiFi credentials below
2. Save this file to your Raspberry Pi Pico W
3. Run it in Thonny or save as main.py for autostart
"""

import network
import time
import machine

# WiFi Configuration
# IMPORTANT: Replace these with your WiFi credentials
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# LED for status indication
led = machine.Pin("LED", machine.Pin.OUT)


def connect_wifi(ssid, password, timeout=10):
    """
    Connect to a WiFi network.

    Args:
        ssid (str): WiFi network name
        password (str): WiFi password
        timeout (int): Connection timeout in seconds

    Returns:
        bool: True if connected, False otherwise
    """
    # Initialize WiFi interface in station mode
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Check if already connected
    if wlan.isconnected():
        print("Already connected to WiFi")
        print_connection_info(wlan)
        return True

    print(f"Connecting to WiFi: {ssid}")
    wlan.connect(ssid, password)

    # Wait for connection with timeout
    start_time = time.time()
    while not wlan.isconnected():
        # Blink LED while connecting
        led.toggle()
        time.sleep(0.2)

        # Check timeout
        if time.time() - start_time > timeout:
            print(f"Connection timeout after {timeout} seconds")
            led.off()
            return False

    # Connection successful
    led.on()
    print("WiFi connected successfully!")
    print_connection_info(wlan)
    return True


def disconnect_wifi():
    """
    Disconnect from WiFi network.
    """
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print("Disconnecting from WiFi...")
        wlan.disconnect()
        wlan.active(False)
        led.off()
        print("Disconnected")
    else:
        print("Not connected to WiFi")


def print_connection_info(wlan):
    """
    Print WiFi connection information.

    Args:
        wlan: WLAN object
    """
    if wlan.isconnected():
        status = wlan.ifconfig()
        print("\n" + "=" * 50)
        print("WiFi Connection Information")
        print("=" * 50)
        print(f"IP Address:  {status[0]}")
        print(f"Subnet Mask: {status[1]}")
        print(f"Gateway:     {status[2]}")
        print(f"DNS Server:  {status[3]}")
        print(f"MAC Address: {':'.join(['%02x' % b for b in wlan.config('mac')])}")
        print("=" * 50 + "\n")
    else:
        print("Not connected to WiFi")


def check_connection_status():
    """
    Continuously check and display WiFi connection status.
    """
    wlan = network.WLAN(network.STA_IF)

    print("Monitoring WiFi connection status...")
    print("Press Ctrl+C to stop")

    try:
        while True:
            if wlan.isconnected():
                led.on()
                print("Status: CONNECTED")
            else:
                led.off()
                print("Status: NOT CONNECTED")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user")
        led.off()


# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("Raspberry Pi Pico W - WiFi Connection Example")
    print("=" * 50)

    # Check if WiFi credentials are set
    if WIFI_SSID == "YOUR_WIFI_SSID":
        print("\nERROR: Please update WIFI_SSID and WIFI_PASSWORD")
        print("Edit this file and replace the placeholder values")
        led.off()
    else:
        # Attempt to connect to WiFi
        if connect_wifi(WIFI_SSID, WIFI_PASSWORD, timeout=15):
            # Monitor connection status
            check_connection_status()
        else:
            print("\nFailed to connect to WiFi")
            print("Please check your credentials and try again")
            led.off()
