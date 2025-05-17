def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

c=int(input("Enter a Celsius:"))
f=int(input("Enter a Fahrenheit:"))

print(f"25°C is {celsius_to_fahrenheit(25)}°F")
print(f"77°F is {fahrenheit_to_celsius(77)}°C")
print("User given Data")
print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")
print(f"{f}°F is {fahrenheit_to_celsius(f):.1f}°C")
