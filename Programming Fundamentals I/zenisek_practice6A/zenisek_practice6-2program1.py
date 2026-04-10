# Defined the main function:
def main():

# Writes to the txt file, and using the "a" method for saving data.
    write_numbers = open("number_list.txt" , "a")
    
# Used a for loop to create the range object:
    for numbers in range(50 , 101):

        write_numbers.write(str(numbers) + "\n")

    write_numbers.close()

if __name__ == "__main__":
    main()