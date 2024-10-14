def main():
    fc = input("Celsius or Fahrenheit (C/F): ")
    try:
        temp = float(input("Input the temperature you want to convert: "))
    except ValueError:
        print("Please enter a valid temperature.")
        return

    if fc.lower() in ["c", "celsius"]:
        result = temp * 1.8 + 32  # Celsius to Fahrenheit
        print(f"{temp}°C is {result:.2f}°F")
    elif fc.lower() in ["f", "fahrenheit"]:
        result = (temp - 32) * 5 / 9  # Fahrenheit to Celsius
        print(f"{temp}°F is {result:.2f}°C")
    else:
        print("Please enter a valid temperature convention (C/F).")

if __name__ == "__main__":
    main()
