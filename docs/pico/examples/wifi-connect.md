# WiFi Connection Example

Connect Raspberry Pi Pico W to a WiFi network and display connection status.

## Overview

This example demonstrates how to connect the Pico W to a WiFi network and monitor the connection status.

## Source Code

**File**: `src/pico_scripts/02_wifi_connect.py`

## Features

- Connect to WiFi network
- Display connection status (Connected/Not Connected)
- Show IP address and network information
- LED indicates connection status
- Continuous status monitoring

## Hardware Requirements

- **Raspberry Pi Pico W** (WiFi required)
- Micro USB cable
- 2.4 GHz WiFi network

## Configuration

Edit the WiFi credentials in the script:

```python
# Replace with your WiFi details
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
```

## Code Explanation

### WiFi Connection

```python
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    time.sleep(0.2)
```

### Connection Status

```python
def check_connection_status():
    wlan = network.WLAN(network.STA_IF)

    if wlan.isconnected():
        print("Status: CONNECTED")
        led.on()
    else:
        print("Status: NOT CONNECTED")
        led.off()
```

### Network Information

```python
def print_connection_info(wlan):
    status = wlan.ifconfig()
    print(f"IP Address:  {status[0]}")
    print(f"Subnet Mask: {status[1]}")
    print(f"Gateway:     {status[2]}")
    print(f"DNS Server:  {status[3]}")
```

## Usage

1. **Edit WiFi Credentials**
   - Open `02_wifi_connect.py` in Thonny
   - Replace `YOUR_WIFI_SSID` with your network name
   - Replace `YOUR_WIFI_PASSWORD` with your password

2. **Upload and Run**
   - Save to Pico
   - Click "Run" (F5)
   - Watch console for connection status

3. **Expected Output**
   ```
   Connecting to WiFi: MyNetwork
   WiFi connected successfully!

   ==================================================
   WiFi Connection Information
   ==================================================
   IP Address:  192.168.1.100
   Subnet Mask: 255.255.255.0
   Gateway:     192.168.1.1
   DNS Server:  192.168.1.1
   ==================================================

   Status: CONNECTED
   ```

## LED Indicators

- **Blinking**: Connecting to WiFi
- **Solid ON**: Connected
- **OFF**: Not connected

## Troubleshooting

### Can't Connect to WiFi

**Check:**
- SSID and password are correct (case-sensitive)
- Using 2.4 GHz network (Pico W doesn't support 5 GHz)
- Network is WPA2-Personal (not enterprise)
- Move closer to WiFi router

**Debug:**
```python
# Check WiFi status code
print(f"Status: {wlan.status()}")

# Status codes:
# 0 = STAT_IDLE
# 1 = STAT_CONNECTING
# 2 = STAT_WRONG_PASSWORD
# 3 = STAT_NO_AP_FOUND
# 4 = STAT_CONNECT_FAIL
# 5 = STAT_GOT_IP (success)
```

### Connection Drops

- Check WiFi signal strength
- Ensure stable power supply
- Check for network interference

## Next Steps

- [Signal Monitor](signal-monitor.md) - Measure WiFi strength
- [API Consumer](api-consumer.md) - Use WiFi to access APIs

## Reference

Full source: `src/pico_scripts/02_wifi_connect.py`
