import sys
import time

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    if y == 0:
        return "Error! Division by zero"
    return x / y

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("3. Subtract")
    print("3. Multiply")
    print("4. Devide")
    print("5. Exit")

    choice = input("Choose operation (1/2/3/4/5): ")

    if choice == '5' or choice.lower() == 'exit':
        print("Exiting the calculator. Goodbye!", end="", flush=True)
        for _ in range(3): 
            time.sleep(0.5)
            print(".", end="", flush=True)
        time.sleep(2)
        sys.exit()

    if choice in ('1', '2', '3', '4'):
        try: 
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {devide(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter numeric values..")
    else:
        print("Invalid choice! Please select a valid operation.")