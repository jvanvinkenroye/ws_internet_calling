"""
Basic LED Blink Example for Raspberry Pi Pico

This script demonstrates the most basic Raspberry Pi Pico functionality:
blinking the onboard LED on and off.

Hardware:
- Raspberry Pi Pico (or Pico W)
- Onboard LED (GPIO 25 on regular Pico, "LED" on Pico W)

Usage:
1. Save this file to your Raspberry Pi Pico
2. Run it in Thonny or save as main.py for autostart
"""

import machine
import time

# Configure LED pin
# For Pico W, use Pin("LED")
# For regular Pico, use Pin(25)
led = machine.Pin("LED", machine.Pin.OUT)

def blink_led(times=10, delay=0.5):
    """
    Blink the LED a specified number of times.

    Args:
        times (int): Number of times to blink
        delay (float): Delay between on/off in seconds
    """
    print(f"Starting LED blink: {times} times with {delay}s delay")

    for i in range(times):
        led.on()
        print(f"Blink {i+1}/{times}: LED ON")
        time.sleep(delay)

        led.off()
        print(f"Blink {i+1}/{times}: LED OFF")
        time.sleep(delay)

    print("Blink sequence completed")


def blink_forever(on_time=0.5, off_time=0.5):
    """
    Blink the LED continuously until interrupted.

    Args:
        on_time (float): How long LED stays on in seconds
        off_time (float): How long LED stays off in seconds
    """
    print(f"Starting continuous blink: ON={on_time}s, OFF={off_time}s")
    print("Press Ctrl+C to stop")

    try:
        count = 0
        while True:
            led.on()
            time.sleep(on_time)

            led.off()
            time.sleep(off_time)

            count += 1
            if count % 10 == 0:
                print(f"Blinked {count} times")

    except KeyboardInterrupt:
        print("\nBlink stopped by user")
        led.off()


# Main execution
if __name__ == "__main__":
    print("=" * 50)
    print("Raspberry Pi Pico - LED Blink Example")
    print("=" * 50)

    # Option 1: Blink a specific number of times
    # blink_led(times=5, delay=0.5)

    # Option 2: Blink continuously
    blink_forever(on_time=0.5, off_time=0.5)
