"""
WiFi Signal Strength Monitor for Raspberry Pi Pico W

This script connects to WiFi and continuously monitors the signal strength (RSSI),
displaying it on the console.

Hardware:
- Raspberry Pi Pico W (WiFi required)

Configuration:
- Update WIFI_SSID and WIFI_PASSWORD with your network credentials

Signal Strength Reference (RSSI in dBm):
- -30 to -50 dBm: Excellent signal
- -50 to -60 dBm: Good signal
- -60 to -70 dBm: Fair signal
- -70 to -80 dBm: Weak signal
- -80 to -90 dBm: Very weak signal
- Below -90 dBm: Extremely weak/unusable signal

Usage:
1. Edit the WiFi credentials below
2. Save this file to your Raspberry Pi Pico W
3. Run it in Thonny
"""

import network
import time
import machine

# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# Update interval in seconds
UPDATE_INTERVAL = 2

# LED for status indication
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
    print("Connected to WiFi")
    return wlan


def get_signal_strength(wlan):
    """
    Get WiFi signal strength (RSSI).

    Args:
        wlan: WLAN object

    Returns:
        int: Signal strength in dBm, or None if not available
    """
    try:
        # Get RSSI (Received Signal Strength Indicator)
        rssi = wlan.status('rssi')
        return rssi
    except Exception as error:
        print(f"Error getting signal strength: {error}")
        return None


def classify_signal(rssi):
    """
    Classify signal strength into quality categories.

    Args:
        rssi (int): Signal strength in dBm

    Returns:
        str: Signal quality description
    """
    if rssi >= -50:
        return "Excellent"
    elif rssi >= -60:
        return "Good"
    elif rssi >= -70:
        return "Fair"
    elif rssi >= -80:
        return "Weak"
    elif rssi >= -90:
        return "Very Weak"
    else:
        return "Extremely Weak"


def rssi_to_percentage(rssi):
    """
    Convert RSSI to percentage (0-100%).

    Args:
        rssi (int): Signal strength in dBm

    Returns:
        int: Signal strength as percentage
    """
    # RSSI typically ranges from -100 (worst) to -30 (best)
    # Convert to 0-100 scale
    if rssi <= -100:
        return 0
    elif rssi >= -30:
        return 100
    else:
        return int(((rssi + 100) / 70) * 100)


def create_signal_bar(percentage, bar_length=20):
    """
    Create a visual signal strength bar.

    Args:
        percentage (int): Signal strength percentage
        bar_length (int): Length of the bar

    Returns:
        str: Visual bar representation
    """
    filled = int((percentage / 100) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    return f"[{bar}]"


def monitor_signal_strength(wlan, interval=2):
    """
    Continuously monitor and display signal strength.

    Args:
        wlan: WLAN object
        interval (float): Update interval in seconds
    """
    print("\n" + "=" * 60)
    print("WiFi Signal Strength Monitor")
    print("=" * 60)
    print("Press Ctrl+C to stop\n")

    try:
        sample_count = 0
        rssi_sum = 0

        while True:
            if not wlan.isconnected():
                print("WiFi disconnected! Attempting to reconnect...")
                led.off()
                break

            rssi = get_signal_strength(wlan)

            if rssi is not None:
                sample_count += 1
                rssi_sum += rssi
                avg_rssi = rssi_sum / sample_count

                percentage = rssi_to_percentage(rssi)
                quality = classify_signal(rssi)
                bar = create_signal_bar(percentage)

                # Display signal information
                print(f"\nSample #{sample_count}")
                print(f"Signal Strength: {rssi} dBm")
                print(f"Quality: {quality}")
                print(f"Percentage: {percentage}%")
                print(f"Visual: {bar}")
                print(f"Average RSSI: {avg_rssi:.1f} dBm")

                # Blink LED based on signal quality
                led.on()
                time.sleep(0.1)
                led.off()

            else:
                print("Unable to read signal strength")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user")
        print(f"Total samples: {sample_count}")
        if sample_count > 0:
            print(f"Average RSSI: {rssi_sum / sample_count:.1f} dBm")
        led.off()


# Main execution
if __name__ == "__main__":
    print("=" * 60)
    print("Raspberry Pi Pico W - WiFi Signal Strength Monitor")
    print("=" * 60)

    if WIFI_SSID == "YOUR_WIFI_SSID":
        print("\nERROR: Please update WIFI_SSID and WIFI_PASSWORD")
        led.off()
    else:
        wlan = connect_wifi(WIFI_SSID, WIFI_PASSWORD)

        if wlan:
            # Display connection info
            status = wlan.ifconfig()
            print(f"\nConnected to: {WIFI_SSID}")
            print(f"IP Address: {status[0]}")

            # Start monitoring
            monitor_signal_strength(wlan, UPDATE_INTERVAL)
        else:
            print("\nFailed to connect to WiFi")
            led.off()
