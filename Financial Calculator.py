import math

def main():
    # Display the main menu and prompt the user to choose a calculator type
    print("Choose a calculator:")
    print("1. Investment")
    print("2. Bond")
    choice = input("Enter 'investment' or 'bond': ").lower()

    if choice == 'investment':
        # Prompt the user for investment details
        amount = float(input("Enter the amount of money to deposit: "))
        interest_rate = float(input("Enter the interest rate (in %): ")) / 100
        years = int(input("Enter the number of years to invest: "))
        interest_type = input("Enter 'simple' or 'compound': ").lower()

        if interest_type == 'simple':
            # Calculate total amount for simple interest
            total_amount = amount * (1 + interest_rate * years)
        elif interest_type == 'compound':
            # Calculate total amount for compound interest
            total_amount = amount * math.pow((1 + interest_rate), years)
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
            return

        # Display the result of the investment calculation
        print(f"The total amount after {years} years is: {total_amount:.2f}")

    elif choice == 'bond':
        # Prompt the user for bond details
        present_value = float(input("Enter the present value of the house: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): ")) / 100
        months = int(input("Enter the number of months to repay the bond: "))

        # Calculate the monthly interest rate
        monthly_interest_rate = annual_interest_rate / 12
        # Calculate the monthly repayment amount
        repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

        # Display the result of the bond repayment calculation
        print(f"The monthly repayment is: {repayment:.2f}")

    else:
        # Handle invalid choices
        print("Invalid choice. Please enter 'investment' or 'bond'.")

if __name__ == "__main__":
    main()
