# API Consumer Example

Query the Number Transmitter API over WiFi and display results via LED.

## Overview

This example demonstrates how to consume REST APIs from MicroPython, query the Number Transmitter API, and visualize the data by blinking the LED.

## Source Code

**File**: `src/pico_scripts/05_api_consumer.py`

## Features

- WiFi connectivity
- HTTP GET requests to REST API
- JSON parsing
- LED visualization (blinks N times for number N)
- Error handling and retry logic
- Statistics tracking

## Hardware Requirements

- Raspberry Pi Pico W (WiFi required)
- Onboard LED
- Running Number Transmitter API on local network

## Prerequisites

1. Number Transmitter API must be running
2. Pico W and API server on same network
3. Know the API server's IP address

## Configuration

```python
# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# API Configuration
API_BASE_URL = "http://192.168.1.100:5001"  # Replace with your API server IP
API_ENDPOINT = "/api/number"

# Query interval
QUERY_INTERVAL = 2  # seconds
```

## Code Explanation

### Querying the API

```python
import urequests

def query_api(url):
    try:
        response = urequests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            response.close()
            return data
        else:
            print(f"API error: HTTP {response.status_code}")
            return None

    except Exception as error:
        print(f"Request failed: {error}")
        return None
```

### Blinking to Represent Number

```python
def blink_number(number, blink_speed=0.2):
    # Blink LED N times where N is the number
    for i in range(number):
        led.on()
        time.sleep(blink_speed)
        led.off()
        time.sleep(blink_speed)
```

### Main Loop

```python
def monitor_api(wlan, api_url, interval=2):
    while True:
        # Query API
        data = query_api(api_url)

        if data:
            current_number = data.get('number')
            print(f"Current number: {current_number}")

            # Blink LED
            blink_number(current_number)

        time.sleep(interval)
```

## Usage

### Setup API Server

First, start the Number Transmitter API on your computer:

```bash
# On your computer
source .venv/bin/activate
python src/api/app.py
# Note the IP address shown in output
```

### Configure Pico Script

1. Edit WiFi credentials
2. Set `API_BASE_URL` to your computer's IP address:
   ```python
   # Find your IP:
   # macOS/Linux: ifconfig | grep inet
   # Windows: ipconfig

   API_BASE_URL = "http://192.168.1.100:5001"  # Your actual IP
   ```

### Upload and Run

1. Upload script to Pico
2. Run in Thonny
3. Watch console output and LED

## Expected Output

```
Raspberry Pi Pico W - API Consumer
============================================================
Connected to: MyNetwork
Pico IP Address: 192.168.1.101

Testing API connection to http://192.168.1.100:5001/api/number...
API connection successful!
Current number from API: 5

Number Transmitter API Consumer
============================================================
API URL: http://192.168.1.100:5001/api/number
Query interval: 2 seconds
Press Ctrl+C to stop

Query #1...
--------------------------------------------------
Current Number: 5
Timestamp: 2025-01-15T10:30:45.123456
Total Cycles: 12345
Next change in: 0.87s
--------------------------------------------------
Blinking 5 times...

Query #2...
--------------------------------------------------
Current Number: 6
Timestamp: 2025-01-15T10:30:47.123456
Total Cycles: 12345
Next change in: 0.65s
--------------------------------------------------
Number changed: 5 -> 6
Blinking 6 times...
```

## LED Behavior

- **Quick blinks**: Number from API (1-9 blinks)
- **3 rapid flashes**: Error occurred
- **Pauses between**: Waiting for next query

## API Response Structure

```json
{
  "number": 5,
  "timestamp": "2025-01-15T10:30:45.123456",
  "unix_timestamp": 1736935845.123456,
  "next_change_in": 0.876,
  "cycle_position": 5,
  "total_cycles": 12345
}
```

## Troubleshooting

### Connection Refused

```
Request failed: Connection refused
```

**Solutions:**
- Verify API server is running
- Check firewall allows port 5001
- Confirm IP address is correct
- Test with: `curl http://YOUR_IP:5001/api/status`

### Network Issues

```
Request failed: [Errno 113] EHOSTUNREACH
```

**Solutions:**
- Ensure same network/subnet
- Check WiFi credentials
- Ping API server from another device
- Verify 2.4 GHz WiFi enabled

### Timeout Errors

```
Request failed: timeout
```

**Solutions:**
- Increase timeout value
- Check network congestion
- Move Pico closer to router
- Reduce query interval

### JSON Parsing Errors

```
ValueError: invalid syntax for JSON
```

**Solutions:**
- Verify API is returning valid JSON
- Test API in browser
- Check API error messages
- Update MicroPython firmware

## Advanced Usage

### Custom Error Handling

```python
error_count = 0
max_errors = 5

if not data:
    error_count += 1
    if error_count >= max_errors:
        print("Too many errors, reconnecting WiFi...")
        wlan.disconnect()
        connect_wifi(WIFI_SSID, WIFI_PASSWORD)
        error_count = 0
```

### Statistics Tracking

```python
query_count = 0
success_count = 0

if data:
    success_count += 1

success_rate = (success_count / query_count) * 100
print(f"Success rate: {success_rate:.1f}%")
```

## Next Steps

- [Access Point](access-point.md) - Create your own web interface
- [Web App API](../../web-app/api.md) - API documentation
- [Signal Monitor](signal-monitor.md) - Check WiFi quality

## Reference

Full source: `src/pico_scripts/05_api_consumer.py`

API documentation: See [API Reference](../../web-app/api.md)
