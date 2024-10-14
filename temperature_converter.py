from tkinter import *

def convert_fahrenheit_to_celsius():
    """Convert the value from Fahrenheit to Celsius and display the result."""
    try:
        fahrenheit_value = float(fahrenheit_entry.get())
        celsius_value = to_celsius(fahrenheit_value)
        celsius_entry.delete(0, END)
        celsius_entry.insert(0, f'{celsius_value:.2f}')
    except ValueError:
        error_label.config(text="Invalid Input")
        celsius_entry.delete(0, END)

def convert_celsius_to_fahrenheit():
    """Convert the value from Celsius to Fahrenheit and display the result."""
    try:
        celsius_value = float(celsius_entry.get())
        fahrenheit_value = to_fahrenheit(celsius_value)
        fahrenheit_entry.delete(0, END)
        fahrenheit_entry.insert(0, f'{fahrenheit_value:.2f}')
    except ValueError:
        error_label.config(text="Invalid Input")
        fahrenheit_entry.delete(0, END)

def to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9.0

def to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5.0 + 32

# Initialize the main application window
app = Tk()
app.title('Temperature Converter')

# Labels
fahrenheit_label = Label(app, text='Fahrenheit:')
fahrenheit_label.grid(row=0, column=0, padx=8, pady=6, sticky=E)

celsius_label = Label(app, text='Celsius:')
celsius_label.grid(row=1, column=0, padx=8, pady=6, sticky=E)

# Text Entry for Fahrenheit
fahrenheit_entry = Entry(app)
fahrenheit_entry.grid(row=0, column=1, padx=5, pady=5)

# Text Entry for Celsius
celsius_entry = Entry(app)
celsius_entry.grid(row=1, column=1, padx=5, pady=5)

# Fahrenheit to Celsius Button
convert_to_celsius_button = Button(app, text='Convert to Celsius', command=convert_fahrenheit_to_celsius)
convert_to_celsius_button.grid(row=0, column=2, padx=6, pady=6, sticky=N + S + E + W)

# Celsius to Fahrenheit Button
convert_to_fahrenheit_button = Button(app, text='Convert to Fahrenheit', command=convert_celsius_to_fahrenheit)
convert_to_fahrenheit_button.grid(row=1, column=2, padx=6, pady=6, sticky=N + S + E + W)

# Error Label
error_label = Label(app, text="", fg="red")
error_label.grid(row=2, columnspan=3, padx=8, pady=6)

# Start the main event loop
app.mainloop()
