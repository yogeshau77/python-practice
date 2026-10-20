
def calculate_average(marks):
    return sum(marks) / len(marks)


def main():
    marks = []

    count = int(input("How many subjects? "))

    if count <= 0:
        print("Enter at least one subject.")
        return

    for i in range(count):
        mark = float(input(f"Enter mark for subject {i + 1}: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    average = calculate_average(marks)

    print("\nMarks:", marks)
    print("Average:", round(average, 2))
    print("Highest mark:", max(marks))
    print("Lowest mark:", min(marks))


if __name__ == "__main__":
    main()
  
