# Unit-Coverter
 # Unit
***Length Unit Converter*** <br>

A simple Python function to convert between different units of length, such as meters, kilometers, miles, feet, inches, and more.

***Features***<br>
 - Easily convert a value from one length unit to another.
 - Supports common units: meters, centimeters, millimeters, kilometers, inches, feet, yards, and miles.
 - Simple and beginner-friendly code. 


***How It Works***<br>

The function uses a dictionary of conversion factors relative to meters. It first converts the input value to meters, then from meters to the desired target unit.

***Supported Units***<br>
 - m (meter)
 - cm (centimeter)
 - mm (millimeter)
 - km (kilometer)
 - in (inch)
 - ft (foot)
 - yd (yard)
 - mile (mile)

***Usage***<br>

 1. Copy the code below
   
   ```
    def convert_length(value, from_unit, to_unit):
    conversions = {
        'm': 1,
        'cm': 100,
        'mm': 1000,
        'km': 0.001,
        'in': 39.3701,
        'ft': 3.28084,
        'yd': 1.09361,
        'mile': 0.000621371
    }
    # Convert the input value to meters, then to the target unit
    value_in_meters = value / conversions[from_unit]
    return value_in_meters * conversions[to_unit]

   # Example usage:
   result = convert_length(10, 'km', 'mile')
   print(f"10 km is {result} miles")
   ```  
 2. Run your Python script.
 3. Change the values and units in the ``` convert_length ``` function call to convert between any supported units.

***Example***<br>
```
result = convert_length(5, 'mile', 'km')
print(f"5 miles is {result} kilometers")
```
***Output***
```
10 km is 6.21371 miles
5 miles is 8.04672 kilometers
```

***Notes***<br>

 1. Make sure to use the correct unit abbreviations as shown above.
 2. The function does not handle invalid units or negative values; you can add error handling as needed.




 # Temperature
***Temperature Converter***<br>

  A simple interactive Python script that converts temperatures between Celsius and Fahrenheit.

***Features*** <br>

 - Convert Celsius to Fahrenheit and vice versa
 - Accepts user input for both Celsius and Fahrenheit values
 - Shows example conversions and user-provided conversions
 - Formats output to one decimal place for better readability

***How It Works*** <br>

The script defines two functions:
 - celsius_to_fahrenheit(c): Converts Celsius to Fahrenheit using the formula
F = C × 9/5 + 32

 - fahrenheit_to_celsius(f): Converts Fahrenheit to Celsius using the formula
C = (F − 32) × 5/9

***The script also:*** <br>

 - Prompts the user to enter a Celsius value and a Fahrenheit value
 - Displays example conversions for 25°C and 77°F
 - Displays the conversion results for the user’s input

***Usage*** <br>

 1. Copy the following code into a Python file (e.g., temp_converter.py):

     ```
      def celsius_to_fahrenheit(c):
          return c * 9/5 + 32
      
      def fahrenheit_to_celsius(f):
          return (f - 32) * 5/9
      
      c = int(input("Enter a Celsius: "))
      f = int(input("Enter a Fahrenheit: "))
      
      print(f"25°C is {celsius_to_fahrenheit(25)}°F")
      print(f"77°F is {fahrenheit_to_celsius(77)}°C")
      print("User given Data")
      print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")
      print(f"{f}°F is {fahrenheit_to_celsius(f):.1f}°C")

     ```
     
 2. Run the script:

    ```
    python Tempareture.py
    ```
 3. Enter the Celsius and Fahrenheit values when prompted.

***Example Output*** <br>
 ```
 Enter a Celsius: 30
 Enter a Fahrenheit: 86
 25°C is 77.0°F
 77°F is 25.0°C
 User given Data
 30°C is 86.0°F
 86°F is 30.0°C

 ```

***Notes***<br>
 1. The script uses int(input(...)), so only integer values are accepted.
 2. You can change int to float if you want to allow decimal inputs.
 3. Output for Fahrenheit to Celsius is formatted to one decimal place for clarity.
