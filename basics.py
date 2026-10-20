
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"


def main():
    print("Python Practice")
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

    number = int(input("Enter an integer: "))
    print(f"{number} is {check_number(number)}.")

    print("Numbers from 1 to 5:")
    for i in range(1, 6):
        print(i)


if __name__ == "__main__":
    main()
  
