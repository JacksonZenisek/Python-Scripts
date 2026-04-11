# Define main function:
def main():
    try:
        file_open = open("number_list.txt" , "r")

# Listed variables:
        total_value = 0
        counter = 0

# Created for loop:
        for line in file_open:
            line = line.strip()
            number = int(line)

            total_value += number
            counter += 1

        file_open.close()

# average operators:
        average_value = total_value / counter

        print(f"Sum: {total_value}")
        print(f"Average: {average_value}")

# Error handlers:
    except IOError:
        print("Error: Could not open file.")

    except ValueError:
        print("Error: File contains non-numeric data.")
    
    except Exception:
        print("Error: Something unexpected happened.")

# Calls the main function:
if __name__ == "__main__":
    main()