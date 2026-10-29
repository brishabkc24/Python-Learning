"""Convert a Celsius temperature to Fahrenheit and print it with one decimal."""

celsius = float(input("Temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius} C is {fahrenheit:.1f} F")
