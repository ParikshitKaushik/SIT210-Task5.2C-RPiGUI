import tkinter as tk
import RPi.GPIO as GPIO

LED_PINS = {
    "Red": 17,    
    "Green": 18,
    "Blue": 27,
}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def set_led_color(color):
    for pin in LED_PINS.values():
        GPIO.output(pin, GPIO.LOW)  
    GPIO.output(LED_PINS[color], GPIO.HIGH)
root = tk.Tk()
root.title("LED Controller")
root.geometry("400x300")
label = tk.Label(root, text="Select LED Color", font=("Comic Sans", 20))
label.pack(pady=20)

def button_click(color):
    set_led_color(color)

for color in LED_PINS.keys():
    button = tk.Button(root, text=color, command=lambda c=color: button_click(c))
    button.pack(pady=15)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)
root.mainloop()
GPIO.cleanup()
