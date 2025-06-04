import RPi.GPIO as GPIO
import time
from sound.crossfade import Crossfade
from gpio.rotary_encoder import RotaryEncoder

def main():
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    
    # Setup rotary encoder with GPIO pins 17 and 18
    encoder = RotaryEncoder(pin_a=17, pin_b=18)
    encoder.setup()

    # Initialize sound crossfade
    sound_player = Crossfade()

    try:
        while True:
            position = encoder.read_position()
            print(f"Encoder Position: {position}")
            # Here you would add logic to trigger sound playback based on position
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()