# 59s Makelangelo-software.git trigger-ci λ sudo apt install python3-serial

import serial
import time


def send_gcode(port, baudrate, commands):
    try:
        # Open the serial port
        with serial.Serial(port, baudrate, timeout=2) as ser:
            time.sleep(1)  # Wait for the connection to establish

            for command in commands:
                print(f"Command: {command}")
                ser.write((command + '\n').encode('utf-8'))

                time.sleep(0.1)  # Short delay between commands
                response = ser.readline().strip().decode('utf-8')
                print(f"Response: {response}")

    except serial.SerialException as e:
        print(f"Serial error: {e}")


# Define the G-code commands to send
gcode_commands = [
    "G28",  # Home all axes
    "G1 X10 Y10 Z0 F3000",  # Move to (10, 10, 0) at 3000 mm/min
    "G1 X20 Y20 Z0 F3000",  # Move to (20, 20, 0) at 3000 mm/min
    # Add more G-code commands as needed
]

# Send G-code commands to Makelangelo plotter
send_gcode('/dev/ttyACM0', 250000, gcode_commands)
