# Unit-Coverter
 # Unit
***Length Unit Converter*** <br>

A simple Python function to convert between different units of length, such as meters, kilometers, miles, feet, inches, and more.

*Features*<br>
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




 # Tempareture
