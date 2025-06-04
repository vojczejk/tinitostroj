import RPi.GPIO as GPIO
import time
import os
import sys
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

    sound_files = sys.argv[1:]
    if not sound_files:
        print("No sound files provided.")
        return
    current_index = 0
    last_select_position = sound_select_encoder.read_position()
    sound_player.play_sound(sound_files[current_index])

    last_volume = None

    try:
        while True:
            sound_select_knob = sound_select_encoder.read_position()
            volume_knob = volume_encoder.read_position()
            print_tui_table(
                sound_select_knob=sound_select_knob,
                volume_knob=volume_knob,
                current_sound=sound_files[current_index]
            )
            if last_volume != volume_knob:
                os.system(f"amixer sset 'PCM' {volume_knob}% > /dev/null 2>&1")
                last_volume = volume_knob
            if sound_select_knob != last_select_position:
                direction = 1 if sound_select_knob > last_select_position else -1
                new_index = current_index + direction
                if 0 <= new_index < len(sound_files):
                    sound_player.crossfade(sound_files[current_index], sound_files[new_index], duration=2)
                    current_index = new_index
                last_select_position = sound_select_knob
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # cleanup GPIO resources

if __name__ == "__main__":
    main()