
def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice.")
        return

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = a + b
    elif choice == "2":
        result = a - b
    elif choice == "3":
        result = a * b
    else:
        if b == 0:
            print("Cannot divide by zero.")
            return
        result = a / b

    print("Result:", result)


if __name__ == "__main__":
    calculator()
  
