# Jackson Zenisek
# Complete
"""
This program gets the numbers from random_numbers.txt, adds them, lists how many were input by the user, and lists the average based on
the sum and the amount of numbers in that file.
"""

# Defined the main function:
def main():
    try:
        open_file = open("random_numbers.txt", "r")

# Defined the variables:
        total_amount = 0
        counter = 0

        for line in open_file:
            number = int(line.strip())

            total_amount += number
            counter += 1

        open_file.close()

        average_amount = total_amount/ counter

# Displays the output of the sum, amount of numbers, and the average of all numbers:
        print(f"Total: {total_amount}")
        print(f"Count: {counter}")
        print(f"Average: {average_amount}")

# Error exception handlers:
    except IOError:
        print("Error: File not found.")

    except ValueError:
        print("Error: File contains invalid data.")

    except Exception:
        print("Error: Something unexpected happened.")

# Calls the main function:
if __name__ == "__main__":
    main()