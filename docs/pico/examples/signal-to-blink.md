# WiFi Signal to LED Blink Frequency

Convert WiFi signal strength to visual LED blink frequency.

## Overview

This example demonstrates data visualization by converting WiFi signal strength to LED blink speed. Stronger signal = faster blinking, weaker signal = slower blinking.

## Source Code

**File**: `src/pico_scripts/04_wifi_signal_to_blink.py`

## Features

- WiFi signal strength to blink frequency conversion
- Automatic updates every 5 seconds
- Visual feedback through LED
- Demo mode (works without WiFi)
- Quality-based blinking patterns

## Hardware Requirements

- Raspberry Pi Pico W
- Onboard LED (no external components)
- WiFi network (or demo mode)

## Blink Frequency Mapping

| Signal Quality | RSSI Range | Blink Interval |
|----------------|------------|----------------|
| Excellent | -30 to -50 dBm | 0.1s (very fast) |
| Good | -50 to -60 dBm | 0.3s (fast) |
| Fair | -60 to -70 dBm | 0.5s (medium) |
| Weak | -70 to -80 dBm | 1.0s (slow) |
| Very Weak | Below -80 dBm | 2.0s (very slow) |

## Configuration

```python
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
SIGNAL_CHECK_INTERVAL = 5  # Update blink rate every 5 seconds
DEMO_MODE = False  # Set True for demo without WiFi
```

## Code Explanation

### RSSI to Blink Interval

```python
def rssi_to_blink_interval(rssi):
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
```

### Blinking with Signal Updates

```python
def blink_with_signal(wlan):
    current_interval = 1.0
    last_check_time = 0

    while True:
        # Update interval periodically
        if time.time() - last_check_time >= 5:
            rssi = get_signal_strength(wlan)
            current_interval, quality = rssi_to_blink_interval(rssi)
            print(f"RSSI: {rssi} dBm, Quality: {quality}")

        # Blink at current interval
        led.on()
        time.sleep(current_interval / 2)
        led.off()
        time.sleep(current_interval / 2)
```

## Usage

### Normal Mode (With WiFi)

1. Edit WiFi credentials in script
2. Upload to Pico
3. Run the script
4. Observe LED blinking speed
5. Move Pico closer/farther from router to see speed change

### Demo Mode (Without WiFi)

1. Set `DEMO_MODE = True` in script
2. Upload and run
3. Watch LED cycle through all signal levels
4. Good for testing without WiFi

## Expected Output

```
Raspberry Pi Pico W - Signal to Blink Converter
============================================================
Connected to: MyNetwork
IP Address: 192.168.1.100

WiFi Signal Strength to LED Blink Converter
============================================================
LED blink speed indicates signal strength:
  - Very fast = Excellent signal
  - Fast = Good signal
  - Medium = Fair signal
  - Slow = Weak signal
  - Very slow = Very weak signal

Press Ctrl+C to stop

Signal Update:
  RSSI: -55 dBm
  Quality: Good
  Blink interval: 0.3s

Blinking (Good): 20 blinks
```

## Visual Interpretation

### Very Fast Blinking (10 blinks/sec)
- Excellent signal (-30 to -50 dBm)
- Optimal performance
- Very close to router

### Fast Blinking (3 blinks/sec)
- Good signal (-50 to -60 dBm)
- Reliable connection
- Normal operating distance

### Medium Blinking (2 blinks/sec)
- Fair signal (-60 to -70 dBm)
- Acceptable performance
- Consider moving closer

### Slow Blinking (1 blink/sec)
- Weak signal (-70 to -80 dBm)
- Poor performance
- Move closer to router

### Very Slow Blinking (0.5 blinks/sec)
- Very weak signal (< -80 dBm)
- Unstable connection
- Immediate action needed

## Demo Mode Example

```python
DEMO_MODE = True

# Simulates all signal levels
# LED will cycle through:
# - Very fast (Excellent)
# - Fast (Good)
# - Medium (Fair)
# - Slow (Weak)
# - Very slow (Very weak)
```

## Applications

- **Visual Signal Strength Indicator** - Quick signal check
- **Placement Optimization** - Find best Pico location
- **Teaching Tool** - Demonstrate data visualization
- **Range Testing** - Test WiFi coverage area

## Troubleshooting

### LED Not Changing Speed

- Check if connected to WiFi
- Verify `SIGNAL_CHECK_INTERVAL` setting
- Try demo mode to test LED

### Always Blinking Slowly

- Poor WiFi signal
- Wrong network credentials
- Move closer to router
- Check 2.4 GHz band enabled

## Next Steps

- [API Consumer](api-consumer.md) - Use WiFi for data
- [Signal Monitor](signal-monitor.md) - Detailed monitoring

## Reference

Full source: `src/pico_scripts/04_wifi_signal_to_blink.py`
