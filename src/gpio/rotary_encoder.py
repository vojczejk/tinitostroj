class RotaryEncoder:
    def __init__(self, pin_a, pin_b):
        import RPi.GPIO as GPIO
        self.GPIO = GPIO  # Store GPIO as an instance attribute
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.position = 0

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(pin_a, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)
        self.GPIO.setup(pin_b, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)

        self.last_a = self.GPIO.input(pin_a)

        self.GPIO.add_event_detect(pin_a, self.GPIO.BOTH, callback=self.update_position)
        self.GPIO.add_event_detect(pin_b, self.GPIO.BOTH, callback=self.update_position)

    def update_position(self, channel):
        a = self.GPIO.input(self.pin_a)
        b = self.GPIO.input(self.pin_b)

        if a != self.last_a:
            if b != a:
                self.position += 1
            else:
                self.position -= 1

        self.last_a = a

    def read_position(self):
        return self.position

    def setup(self):
        pass  # GPIO setup is already handled in __init__