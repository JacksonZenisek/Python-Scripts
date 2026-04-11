# Jackson Zenisek
# Complete
"""
This program asks the user how many random numbers they would like to save to random_numbers.txt
The numbers are then stored in the file for later use,
"""

# Imported the random module:
import random

# Defined the main function:
def main():
    try:
# Asks the user how many random numbers:
        counter = int(input("How many random numbers do you want? "))

        open_file = open("random_numbers.txt", "w")

# Created the for loop. Generates numbers 1 - 500, with each number having its own line:
        for _ in range(counter):
            rand_numbers = random.randint(1, 500)
            open_file.write(str(rand_numbers) + "\n")

        open_file.close()
# Confirms that the numbers have been written to the file:
        print("Random numbers written to file.")

# Error exception handlers:
    except ValueError:
        print("Error: Please enter a valid number.")

    except Exception:
        print("Error: Something went wrong.")

# Calls the main function
if __name__ == "__main__":
    main()