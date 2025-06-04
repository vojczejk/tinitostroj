# Raspberry Pi GPIO Sound Project

This project is designed to interface with a Raspberry Pi to read a rotary encoder and play sounds with crossfade effects. It utilizes the GPIO pins for reading the encoder's position and a sound library for audio playback.

## Project Structure

```
raspberry-pi-gpio-sound
├── src
│   ├── main.py          # Entry point of the application
│   ├── gpio
│   │   └── rotary_encoder.py  # Rotary encoder handling
│   ├── sound
│   │   └── crossfade.py  # Sound playback and crossfade functionality
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── .gitignore            # Files to ignore in version control
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd raspberry-pi-gpio-sound
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Connect the Rotary Encoder:**
   Follow the wiring diagram to connect the rotary encoder to the GPIO pins on the Raspberry Pi.

4. **Run the application:**
   Execute the main script:
   ```
   python src/main.py
   ```

## Usage

- The application will read the position of the rotary encoder and trigger sound playback based on the encoder's position.
- The crossfade functionality will allow smooth transitions between different sound files.

## Additional Information

- Ensure that you have the necessary permissions to access GPIO pins on your Raspberry Pi.
- Modify the `requirements.txt` file to add any additional libraries you may need for your specific use case.

## License

This project is licensed under the MIT License - see the LICENSE file for details.