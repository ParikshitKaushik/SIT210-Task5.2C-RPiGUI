import tkinter as tk  # Import the tkinter library for creating the GUI
import RPi.GPIO as GPIO  # Import the RPi.GPIO library for controlling the Raspberry Pi's GPIO pins

# Define the GPIO pins for each LED color
LED_PINS = {
    "Red": 17,
    "Green": 18,
    "Blue": 27,
}

GPIO.setwarnings(False)  # Disable GPIO warnings
GPIO.setmode(GPIO.BCM)  # Set the GPIO pin numbering mode to BCM

# Initialize and set the LED pins to LOW
for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)  # Set the pin as an output
    GPIO.output(pin, GPIO.LOW)  # Set the pin to LOW (LED off)

# Define a function to set the LED color
def set_led_color(color):
    for pin in LED_PINS.values():
        GPIO.output(pin, GPIO.LOW)  # Turn off all LEDs
    GPIO.output(LED_PINS[color], GPIO.HIGH)  # Turn on the selected LED

# Create a tkinter window
root = tk.Tk()
root.title("LED Controller")
root.geometry("400x300")

label = tk.Label(root, text="Select LED Color", font=("Comic Sans", 20))
label.pack(pady=20)

# Define a function to handle button clicks and set the LED color
def button_click(color):
    set_led_color(color)

# Create buttons for each LED color
for color in LED_PINS.keys():
    button = tk.Button(root, text=color, command=lambda c=color: button_click(c))
    button.pack(pady=15)

exit_button = tk.Button(root, text="Exit", command=root.quit)  # Create an exit button
exit_button.pack(pady=10)

root.mainloop()  # Start the tkinter main loop to display the GUI

GPIO.cleanup()  # Clean up and release GPIO resources when the program exits
