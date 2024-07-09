#Reviewed by Toufique Mahlangu on July 2024
import math

def main():
    print("Choose a calculator:")
    print("1. Investment")
    print("2. Bond")
    choice = input("Enter 'investment' or 'bond': ").lower()

    if choice == 'investment':
        amount = float(input("Enter the amount of money to deposit: "))
        interest_rate = float(input("Enter the interest rate (in %): ")) / 100
        years = int(input("Enter the number of years to invest: "))
        interest_type = input("Enter 'simple' or 'compound': ").lower()

        if interest_type == 'simple':
            total_amount = amount * (1 + interest_rate * years)
        elif interest_type == 'compound':
            total_amount = amount * math.pow((1 + interest_rate), years)
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
            return

        print(f"The total amount after {years} years is: {total_amount:.2f}")

    elif choice == 'bond':
        present_value = float(input("Enter the present value of the house: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
        months = int(input("Enter the number of months to repay the bond: "))

        monthly_interest_rate = annual_interest_rate / 12
        repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

        print(f"The monthly repayment is: {repayment:.2f}")

    else:
        print("Invalid choice. Please enter 'investment' or 'bond'.")

if __name__ == "__main__":
    main()
