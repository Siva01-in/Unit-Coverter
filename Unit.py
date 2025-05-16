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
