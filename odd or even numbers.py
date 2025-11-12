try:
    value = input("Enter an integer: ")
    number = int(value)  

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

except ValueError:
    print("Error: Please enter a valid integer.")