"""
WiFi Signal Strength to LED Blink Frequency Converter for Raspberry Pi Pico W

This script connects to WiFi and converts the signal strength to LED blink frequency:
- Stronger signal = faster blinking
- Weaker signal = slower blinking

Hardware:
- Raspberry Pi Pico W (WiFi required)
- Onboard LED

Configuration:
- Update WIFI_SSID and WIFI_PASSWORD with your network credentials

Blink Frequency Mapping:
- Excellent signal (-30 to -50 dBm): Very fast (0.1s interval)
- Good signal (-50 to -60 dBm): Fast (0.3s interval)
- Fair signal (-60 to -70 dBm): Medium (0.5s interval)
- Weak signal (-70 to -80 dBm): Slow (1.0s interval)
- Very weak signal (below -80 dBm): Very slow (2.0s interval)

Usage:
1. Edit the WiFi credentials below
2. Save this file to your Raspberry Pi Pico W
3. Run it in Thonny or save as main.py for autostart
"""

import network
import time
import machine

# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# Signal check interval (how often to update blink rate)
SIGNAL_CHECK_INTERVAL = 5  # seconds

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

    print("Connected to WiFi!")
    return wlan


def get_signal_strength(wlan):
    """
    Get WiFi signal strength (RSSI).

    Args:
        wlan: WLAN object

    Returns:
        int: Signal strength in dBm, or -100 if not available
    """
    try:
        rssi = wlan.status('rssi')
        return rssi if rssi else -100
    except:
        return -100


def rssi_to_blink_interval(rssi):
    """
    Convert RSSI to LED blink interval.
    Stronger signal = faster blinking (shorter interval)
    Weaker signal = slower blinking (longer interval)

    Args:
        rssi (int): Signal strength in dBm

    Returns:
        tuple: (interval in seconds, quality description)
    """
    if rssi >= -50:
        return (0.1, "Excellent")
    elif rssi >= -60:
        return (0.3, "Good")
    elif rssi >= -70:
        return (0.5, "Fair")
    elif rssi >= -80:
        return (1.0, "Weak")
    else:
        return (2.0, "Very Weak")


def blink_with_signal(wlan):
    """
    Blink LED based on WiFi signal strength.
    Updates blink rate periodically based on signal strength.

    Args:
        wlan: WLAN object
    """
    print("\n" + "=" * 60)
    print("WiFi Signal Strength to LED Blink Converter")
    print("=" * 60)
    print("LED blink speed indicates signal strength:")
    print("  - Very fast = Excellent signal")
    print("  - Fast = Good signal")
    print("  - Medium = Fair signal")
    print("  - Slow = Weak signal")
    print("  - Very slow = Very weak signal")
    print("\nPress Ctrl+C to stop\n")

    last_check_time = 0
    current_interval = 1.0
    current_quality = "Unknown"

    try:
        blink_count = 0

        while True:
            # Check if WiFi is still connected
            if not wlan.isconnected():
                print("\nWiFi disconnected!")
                # Flash rapidly to indicate disconnection
                for _ in range(10):
                    led.toggle()
                    time.sleep(0.05)
                led.off()
                break

            # Update blink interval based on signal strength
            current_time = time.time()
            if current_time - last_check_time >= SIGNAL_CHECK_INTERVAL:
                rssi = get_signal_strength(wlan)
                current_interval, current_quality = rssi_to_blink_interval(rssi)

                print(f"\nSignal Update:")
                print(f"  RSSI: {rssi} dBm")
                print(f"  Quality: {current_quality}")
                print(f"  Blink interval: {current_interval}s")

                last_check_time = current_time

            # Blink LED at current interval
            led.on()
            time.sleep(current_interval / 2)

            led.off()
            time.sleep(current_interval / 2)

            blink_count += 1

            # Print status every 20 blinks
            if blink_count % 20 == 0:
                print(f"Blinking ({current_quality}): {blink_count} blinks")

    except KeyboardInterrupt:
        print(f"\n\nStopped by user after {blink_count} blinks")
        led.off()


def run_demo_mode():
    """
    Demo mode that simulates different signal strengths.
    Useful for testing without WiFi connection.
    """
    print("\n" + "=" * 60)
    print("DEMO MODE - Simulating different signal strengths")
    print("=" * 60)

    signal_levels = [
        (-40, "Excellent", 0.1),
        (-55, "Good", 0.3),
        (-65, "Fair", 0.5),
        (-75, "Weak", 1.0),
        (-85, "Very Weak", 2.0)
    ]

    try:
        for rssi, quality, interval in signal_levels:
            print(f"\nSimulating {quality} signal ({rssi} dBm, {interval}s interval)")

            for i in range(10):
                led.on()
                time.sleep(interval / 2)
                led.off()
                time.sleep(interval / 2)

            time.sleep(1)

        print("\nDemo completed!")
        led.off()

    except KeyboardInterrupt:
        print("\nDemo stopped by user")
        led.off()


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Raspberry Pi Pico W - Signal to Blink Converter")
    print("=" * 60)

    # Check for demo mode
    DEMO_MODE = False  # Set to True to run demo without WiFi

    if DEMO_MODE:
        print("\nRunning in DEMO MODE")
        run_demo_mode()
    elif WIFI_SSID == "YOUR_WIFI_SSID":
        print("\nERROR: Please update WIFI_SSID and WIFI_PASSWORD")
        print("Or set DEMO_MODE = True to run without WiFi")
        led.off()
    else:
        wlan = connect_wifi(WIFI_SSID, WIFI_PASSWORD)

        if wlan:
            status = wlan.ifconfig()
            print(f"Connected to: {WIFI_SSID}")
            print(f"IP Address: {status[0]}")

            # Start blinking based on signal strength
            blink_with_signal(wlan)
        else:
            print("\nFailed to connect to WiFi")
            print("Set DEMO_MODE = True to run demo without WiFi")
            led.off()
