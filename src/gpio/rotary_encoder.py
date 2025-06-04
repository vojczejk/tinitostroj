class RotaryEncoder:
    def __init__(self, pin_a, pin_b, max=None, min=None, start=0):
        import RPi.GPIO as GPIO
        self.GPIO = GPIO  # Store GPIO as an instance attribute
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.max = max
        self.min = min
        self.position = start

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(pin_a, self.GPIO.IN)
        self.GPIO.setup(pin_b, self.GPIO.IN)


        self.GPIO.add_event_detect(pin_a, self.GPIO.RISING, callback=self.update_position)

    def update_position(self, channel):
        b = self.GPIO.input(self.pin_b)
        if b:
            self.position += 1
        else:
            self.position -= 1

        if self.max is not None and self.position > self.max:
            self.position = self.max
        if self.min is not None and self.position < self.min:
            self.position = self.min

    def read_position(self):
        return self.position