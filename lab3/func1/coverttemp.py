from tokenize import Double


def convert_temp(n):
    celsius = (5 / 9) * (n - 32)

    print("Temperatire in Celsius is:",int(celsius) )

if __name__ == "__main__":
    n = int(input("Temperature in Fahrenheit: "))
    
    convert_temp(n)