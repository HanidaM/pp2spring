def convert_to_ounces(n):
    ounces = 28.3495231 * n

    print("Weight in ounces: ", ounces)




if __name__ == "__main__":
    n = int(input("Weight in grams: "))

    convert_to_ounces(n)