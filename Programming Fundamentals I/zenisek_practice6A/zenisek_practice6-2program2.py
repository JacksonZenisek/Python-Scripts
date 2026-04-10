# Defined the main function:
def main():

# opens the .txt file as "read only".
    open_numbers_file = open("number_list.txt" , "r")

# Terminates the end of the loop by detecting the end of the file:
    for end_line in open_numbers_file:
        print(end_line.rstrip())
    
    open_numbers_file.close()

if __name__ == "__main__":
    main()
