print("\n\t\tWellcome To Fahrenheit Convert Into Celsius\n")

fahrenheit : int = int(input("Enter temperature in Fahrenheit : "))

def main(fahrenheit_value:str):
    convert_fahrenheit = (fahrenheit_value - 32) * 5.0/9.0
    print(f"\nTemperature: {fahrenheit_value} F = {convert_fahrenheit:.2f}")

if __name__ in "__main__":
    main(fahrenheit)