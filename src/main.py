import RPi.GPIO as GPIO
import time
from sound.crossfade import Crossfade
from gpio.rotary_encoder import RotaryEncoder

def print_tui_table(**kwargs):
    """
    Prints the provided arguments in a table format, overwriting the terminal.
    :param kwargs: Keyword arguments where keys are argument names and values are their values.
    """
    print("\033c", end="")  # Clear the terminal
    print(f"{'Argument':<20} | {'Value':<20}")
    print("-" * 43)
    for key, value in kwargs.items():
        print(f"{key:<20} | {value:<20}")

def main():
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    
    # Setup sound select encoder with GPIO pins 17 and 18
    sound_select_encoder = RotaryEncoder(pin_a=17, pin_b=18)
    
    # Setup volume encoder with GPIO pins 27 and 22
    volume_encoder = RotaryEncoder(pin_a=27, pin_b=22, max=100, min=0, start=50)
    
    # Initialize sound crossfade
    sound_player = Crossfade()

    try:
        while True:
            sound_select_knob = sound_select_encoder.read_position()
            volume_knob = volume_encoder.read_position()
            print_tui_table(
                sound_select_knob=sound_select_knob,
                volume_knob=volume_knob
            )
            # Here you would add logic to trigger sound playback based on position
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # cleanup GPIO resources

if __name__ == "__main__":
    main()