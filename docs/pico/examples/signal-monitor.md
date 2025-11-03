# WiFi Signal Strength Monitor

Monitor WiFi signal strength (RSSI) on Raspberry Pi Pico W.

## Overview

This example continuously monitors WiFi signal strength and displays it with quality classifications and visual bars.

## Source Code

**File**: `src/pico_scripts/03_wifi_signal_monitor.py`

## Features

- Real-time RSSI measurement
- Signal quality classification
- Percentage conversion
- Visual bar graph display
- Average signal calculation
- Console output

## Hardware Requirements

- Raspberry Pi Pico W
- WiFi network (2.4 GHz)

## Signal Strength Reference

| RSSI (dBm) | Quality | Description |
|------------|---------|-------------|
| -30 to -50 | Excellent | Best possible signal |
| -50 to -60 | Good | Very reliable |
| -60 to -70 | Fair | Acceptable |
| -70 to -80 | Weak | May have issues |
| -80 to -90 | Very Weak | Poor connection |
| Below -90 | Unusable | Connection problems |

## Configuration

```python
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
UPDATE_INTERVAL = 2  # seconds
```

## Code Explanation

### Get Signal Strength

```python
def get_signal_strength(wlan):
    rssi = wlan.status('rssi')
    return rssi
```

### Classify Signal

```python
def classify_signal(rssi):
    if rssi >= -50:
        return "Excellent"
    elif rssi >= -60:
        return "Good"
    elif rssi >= -70:
        return "Fair"
    elif rssi >= -80:
        return "Weak"
    else:
        return "Very Weak"
```

### Visual Bar

```python
def create_signal_bar(percentage, bar_length=20):
    filled = int((percentage / 100) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    return f"[{bar}]"
```

## Expected Output

```
WiFi Signal Strength Monitor
============================================================
Press Ctrl+C to stop

Sample #1
Signal Strength: -55 dBm
Quality: Good
Percentage: 64%
Visual: [████████████████░░░░]
Average RSSI: -55.0 dBm

Sample #2
Signal Strength: -58 dBm
Quality: Good
Percentage: 60%
Visual: [████████████░░░░░░░░]
Average RSSI: -56.5 dBm
```

## Usage

1. Edit WiFi credentials
2. Upload to Pico
3. Run the script
4. Watch signal strength updates
5. Press Ctrl+C to stop

## Interpreting Results

### Good Signal (-50 to -60 dBm)
- Stable connection
- Fast data transfer
- Suitable for all applications

### Fair Signal (-60 to -70 dBm)
- Generally reliable
- May have occasional issues
- Good for most uses

### Weak Signal (below -70 dBm)
- Unstable connection
- Slow speeds
- Move closer to router

## Improving Signal

1. **Move Closer** - Reduce distance to router
2. **Remove Obstacles** - Clear line of sight
3. **Change Channel** - Reduce interference
4. **Use External Antenna** - If supported

## Next Steps

- [Signal to Blink](signal-to-blink.md) - Convert to LED frequency
- [WiFi Connection](wifi-connect.md) - Basic connection

## Reference

Full source: `src/pico_scripts/03_wifi_signal_monitor.py`
