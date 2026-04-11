# Defines the main function:
def main():

#Defining the variables:
    NAME_HEAD = "Name"
    SCORE_HEAD = "Score"
    
    open_results = open("students.txt","r")

# Setting the header:
    print(f"{NAME_HEAD}{SCORE_HEAD:>22}")
    print("-" *27)

    name = open_results.readline()
    
# Created the while loop for the \n rstrip and the alignment of the data from students.txt:
    while name != "":
        score = open_results.readline()

        name = name.rstrip("\n")
        score = score.rstrip("\n")

        print(f"{name:<15}{float(score):>10.1f}")

        name = open_results.readline()
    
    open_results.close()

# Calls the main function:
if __name__ == "__main__":
    main()