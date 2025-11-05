while True:
    try:
        selection = int(input("Select conversion type:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter 1 or 2: "))
        if selection not in [1, 2]:
            print("Invalid selection. Please enter 1 or 2.")
            continue
        temp_input = float(input("Enter the temperature to convert: "))
        if selection == 1:
            converted_temp = (temp_input * 9/5) + 32
            print(f"{temp_input}°C is {converted_temp}°F\n")
        else:
            converted_temp = (temp_input - 32) * 5/9
            print(f"{temp_input}°F is {converted_temp}°C\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")