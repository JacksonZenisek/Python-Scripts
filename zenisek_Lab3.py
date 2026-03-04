# Jackson Zenisek
# Complete
"""
This program calculates the total discount amount, and the total amount baed on the amount of software packages purchased with the users input.
It is labeled with the dollar sign and rounds to the nearest two decimal places.
"""

# User is asked how many packages were purchased:
number_of_purchases_packages = int(input("Enter the number of packages purchased?"))

# The calculation before discount amount:
value_before_discount = number_of_purchases_packages * 149


# The selected discount based on the user's input. Ex: User inputs 10 weere purchased, so it calculates the 10% discount, followed by the total amount.
# If the input value is a negative nukber, then the program prints "Invalid number", and exits the program.
if number_of_purchases_packages < 0:
    print("Invalid number.")
    exit()

if number_of_purchases_packages <10:
    print(f"Discount Amount:${value_before_discount == 0:,.2f}")

elif number_of_purchases_packages >=10 and number_of_purchases_packages <=49 :
    print(f"Discount Amount:${value_before_discount / 10:,.2f}")

elif number_of_purchases_packages >=50 and number_of_purchases_packages <=99:
    print(f"Discount Amount:${value_before_discount / 5:,.2f}")

elif number_of_purchases_packages >=100 and number_of_purchases_packages <=149:
    print(f"Discount Amount:${value_before_discount / 10 * 7:,.2f}")

else:
    print(f"Discount Amount:${value_before_discount / 5 * 2:,.2f}")

# The total amount is displayed regardless of the amount of software packages purchased, and the amount discounted.
print(f"Total Amount:${value_before_discount:,.2f}")