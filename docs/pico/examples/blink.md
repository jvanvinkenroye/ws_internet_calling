# LED Blink Example

Basic LED control example for Raspberry Pi Pico.

## Overview

This is the simplest example demonstrating how to control the onboard LED on the Raspberry Pi Pico.

## Source Code

**File**: `src/pico_scripts/01_blink.py`

## Features

- Control onboard LED
- Two modes: blink N times or blink forever
- Configurable blink speed
- Clean error handling with Ctrl+C

## Hardware Requirements

- Raspberry Pi Pico or Pico W
- Micro USB cable
- No external components needed (uses onboard LED)

## Code Explanation

### LED Setup

```python
import machine

# For Pico W, use "LED"
# For regular Pico, use Pin(25)
led = machine.Pin("LED", machine.Pin.OUT)
```

### Blink Functions

**Blink N times:**
```python
def blink_led(times=10, delay=0.5):
    for i in range(times):
        led.on()
        time.sleep(delay)
        led.off()
        time.sleep(delay)
```

**Blink continuously:**
```python
def blink_forever(on_time=0.5, off_time=0.5):
    while True:
        led.on()
        time.sleep(on_time)
        led.off()
        time.sleep(off_time)
```

## Usage

### Upload to Pico

1. Open `01_blink.py` in Thonny
2. Connect your Pico via USB
3. Click "Run current script" (F5)
4. LED should start blinking!

### Customize Blink Pattern

Edit the main section:

```python
# Blink 5 times slowly
blink_led(times=5, delay=1.0)

# Or blink continuously fast
blink_forever(on_time=0.2, off_time=0.2)
```

### Stop the Program

Press **Ctrl+C** in Thonny Shell to stop the blinking.

## Autostart on Power-Up

To make this run automatically when Pico powers on:

1. Save the file as `main.py` on the Pico
2. Disconnect and reconnect USB
3. LED will start blinking automatically

## Troubleshooting

### LED Not Blinking

**Check:**
- Pico is properly connected
- Code is running (check Thonny Shell for output)
- Using correct Pin ("LED" for Pico W, 25 for regular Pico)

**Try:**
```python
# Test LED manually in Shell
from machine import Pin
led = Pin("LED", Pin.OUT)
led.on()   # Should turn on
led.off()  # Should turn off
```

### Program Won't Stop

- Press Ctrl+C multiple times
- Click "Stop/Restart backend" in Thonny
- Disconnect USB cable

## Next Steps

- [WiFi Connection](wifi-connect.md) - Connect to WiFi
- [More Examples](../introduction.md) - See all examples

## Reference

See full source code: `src/pico_scripts/01_blink.py`
