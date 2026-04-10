def main():
    open_names_file = open("my_name.txt" , "r")

    line_one = open_names_file.readline()
    line_two = open_names_file.readline()
    line_three = open_names_file.readline()

    line_one = line_one.rstrip("\n")
    line_two = line_two.rstrip("\n")
    line_three = line_three.rstrip("\n")

    age = int(line_three)

    half_age = age / 2

    open_names_file.close()

    print(line_one)
    print(line_two)
    print(age)
    print(f"{half_age:.0f}")

if __name__ == '__main__':
    main()