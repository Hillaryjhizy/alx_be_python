# Define global conversion factors

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor from Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user input and display converted temperatures.
    """
    try:
        # Prompt user for temperature input
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()

        if unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius:.2f}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit:.2f}°F")
        else:
            # Handle invalid unit input
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        # Handle invalid temperature input
        print(f"Error: {e}. Please enter a numeric value for temperature.")

if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()

   
