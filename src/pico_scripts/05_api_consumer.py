"""
Number Transmitter API Consumer for Raspberry Pi Pico W

This script queries the Number Transmitter API over WiFi and displays
the transmitted number both on the console and by blinking the LED.
The LED blinks N times where N is the current number from the API.

Hardware:
- Raspberry Pi Pico W (WiFi required)
- Onboard LED

Configuration:
- Update WIFI_SSID and WIFI_PASSWORD with your network credentials
- Update API_BASE_URL with your API server address

Usage:
1. Ensure the Number Transmitter API is running
2. Edit the configuration below
3. Save this file to your Raspberry Pi Pico W
4. Run it in Thonny or save as main.py for autostart
"""

import network
import time
import machine
import ujson
import urequests

# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# API Configuration
API_BASE_URL = "http://192.168.1.100:5001"  # Update with your API server IP
API_ENDPOINT = "/api/number"

# Query interval in seconds
QUERY_INTERVAL = 2

# LED
led = machine.Pin("LED", machine.Pin.OUT)


def connect_wifi(ssid, password, timeout=15):
    """
    Connect to WiFi network.

    Args:
        ssid (str): WiFi network name
        password (str): WiFi password
        timeout (int): Connection timeout in seconds

    Returns:
        network.WLAN: WLAN object if connected, None otherwise
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        print("Already connected to WiFi")
        return wlan

    print(f"Connecting to {ssid}...")
    wlan.connect(ssid, password)

    start_time = time.time()
    while not wlan.isconnected():
        led.toggle()
        time.sleep(0.2)

        if time.time() - start_time > timeout:
            print("Connection timeout")
            led.off()
            return None

    led.on()
    time.sleep(0.5)
    led.off()
    print("Connected to WiFi!")
    return wlan


def query_api(url):
    """
    Query the Number Transmitter API.

    Args:
        url (str): Full API endpoint URL

    Returns:
        dict: API response data, or None if request failed
    """
    try:
        response = urequests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            response.close()
            return data
        else:
            print(f"API error: HTTP {response.status_code}")
            response.close()
            return None

    except Exception as error:
        print(f"Request failed: {error}")
        return None


def blink_number(number, blink_speed=0.2):
    """
    Blink LED N times to represent the number.

    Args:
        number (int): Number to represent (1-9)
        blink_speed (float): Speed of each blink in seconds
    """
    for i in range(number):
        led.on()
        time.sleep(blink_speed)
        led.off()
        time.sleep(blink_speed)


def display_api_data(data):
    """
    Display API data on console.

    Args:
        data (dict): API response data
    """
    print("\n" + "-" * 50)
    print(f"Current Number: {data.get('number', 'N/A')}")
    print(f"Timestamp: {data.get('timestamp', 'N/A')}")
    print(f"Total Cycles: {data.get('total_cycles', 'N/A')}")
    print(f"Next change in: {data.get('next_change_in', 'N/A'):.2f}s")
    print("-" * 50)


def monitor_api(wlan, api_url, interval=2):
    """
    Continuously query API and display results.

    Args:
        wlan: WLAN object
        api_url (str): Full API endpoint URL
        interval (float): Query interval in seconds
    """
    print("\n" + "=" * 60)
    print("Number Transmitter API Consumer")
    print("=" * 60)
    print(f"API URL: {api_url}")
    print(f"Query interval: {interval} seconds")
    print("Press Ctrl+C to stop\n")

    query_count = 0
    error_count = 0
    last_number = None

    try:
        while True:
            # Check WiFi connection
            if not wlan.isconnected():
                print("\nWiFi disconnected!")
                for _ in range(5):
                    led.toggle()
                    time.sleep(0.1)
                led.off()
                break

            # Query API
            print(f"Query #{query_count + 1}...", end=" ")
            data = query_api(api_url)

            if data:
                query_count += 1
                current_number = data.get('number')

                # Display data
                display_api_data(data)

                # Blink LED to represent the number
                if current_number and 1 <= current_number <= 9:
                    print(f"Blinking {current_number} times...")
                    blink_number(current_number)

                    # Check if number changed
                    if last_number != current_number:
                        print(f"Number changed: {last_number} -> {current_number}")

                    last_number = current_number
                else:
                    print("Invalid number from API")

            else:
                error_count += 1
                print(f"Failed (Error #{error_count})")

                # Flash LED to indicate error
                for _ in range(3):
                    led.on()
                    time.sleep(0.1)
                    led.off()
                    time.sleep(0.1)

            # Wait before next query
            time.sleep(interval)

    except KeyboardInterrupt:
        print(f"\n\nStopped by user")
        print(f"Statistics:")
        print(f"  Total queries: {query_count}")
        print(f"  Errors: {error_count}")
        print(f"  Success rate: {(query_count / (query_count + error_count) * 100):.1f}%")
        led.off()


def test_api_connection(api_url):
    """
    Test API connectivity before starting monitoring.

    Args:
        api_url (str): Full API endpoint URL

    Returns:
        bool: True if API is reachable, False otherwise
    """
    print(f"\nTesting API connection to {api_url}...")

    data = query_api(api_url)

    if data:
        print("API connection successful!")
        print(f"Current number from API: {data.get('number')}")
        return True
    else:
        print("API connection failed!")
        return False


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Raspberry Pi Pico W - API Consumer")
    print("=" * 60)

    if WIFI_SSID == "YOUR_WIFI_SSID":
        print("\nERROR: Please update configuration:")
        print("  - WIFI_SSID and WIFI_PASSWORD")
        print("  - API_BASE_URL")
        led.off()
    else:
        # Connect to WiFi
        wlan = connect_wifi(WIFI_SSID, WIFI_PASSWORD)

        if wlan:
            status = wlan.ifconfig()
            print(f"\nConnected to: {WIFI_SSID}")
            print(f"Pico IP Address: {status[0]}")

            # Build full API URL
            full_api_url = API_BASE_URL.rstrip('/') + API_ENDPOINT

            # Test API connection
            if test_api_connection(full_api_url):
                # Start monitoring
                time.sleep(2)
                monitor_api(wlan, full_api_url, QUERY_INTERVAL)
            else:
                print("\nCannot proceed without API connection")
                print("Please check:")
                print("  1. API server is running")
                print("  2. API_BASE_URL is correct")
                print("  3. Pico and API server are on same network")
                led.off()
        else:
            print("\nFailed to connect to WiFi")
            led.off()
