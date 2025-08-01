import math


def calculator():
    while True:
        print("\n--- CALCULATOR ---")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Square Root")
        print("6: Exit")

        choice = input("Select operation (1/2/3/4/5/6): ")

        if choice == '6':
            print("Shutting down calculator...")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid number input!")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                try:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero!")

        elif choice == '5':
            try:
                num = float(input("Enter number to find square root: "))
                if num < 0:
                    print("Error: Cannot calculate square root of negative numbers!")
                else:
                    print(f"Result: √{num} = {math.sqrt(num)}")
            except ValueError:
                print("Error: Invalid number input!")

        else:
            print("Invalid selection! Please enter a number between 1-6.")


        continue_calc = input("\nDo you want to perform another operation? (Y/N): ")
        if continue_calc.lower() != 'y':
            print("Shutting down calculator...")
            break


calculator()
