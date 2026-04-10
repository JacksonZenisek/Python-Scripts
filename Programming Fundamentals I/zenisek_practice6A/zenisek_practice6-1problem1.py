# Defined the main function:
def main():
    open_names_file = open("my_name.txt" , "a")

# The user inputs for both names and an age:
    your_firstname = str(input("Enter your name:"))

    other_name = str(input("Enter another name:"))

    age = int(input("Enter your age:"))

# Writes the input data to the txt file. Used the \n function for neatness:
    open_names_file.write(f"{your_firstname}\n{other_name}\n{age}")
 
if __name__ == "__main__":
    main()