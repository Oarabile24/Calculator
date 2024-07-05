# Financial Calculators

This repository contains a simple Python program that allows users to access two different financial calculators: an investment calculator and a home loan repayment calculator.

## Features

- **Investment Calculator**: Calculate the future value of an investment based on either simple or compound interest.
- **Home Loan Repayment Calculator**: Calculate the monthly repayment amount for a home loan.

## How to Use

1. **Clone the repository**:
    ```sh
    [git clone https://github.com/yourusername/financial-calculators.git](https://github.com/Oarabile24/Calculator.git)
    cd financial-calculators
    ```

2. **Run the program**:
    ```sh
    python finance_calculators.py
    ```

3. **Follow the prompts**:
    - Choose either "investment" or "bond" to proceed.
    - For investment:
        - Enter the amount of money you are depositing.
        - Enter the interest rate (as a percentage).
        - Enter the number of years you plan on investing for.
        - Choose either "simple" or "compound" interest.
    - For bond:
        - Enter the present value of the house.
        - Enter the interest rate (as a percentage).
        - Enter the number of months you plan to take to repay the bond.

## Example

### Investment Calculator
- **Input**:
  - Amount: 1000
  - Interest Rate: 8
  - Years: 5
  - Interest Type: compound
- **Output**:
  - The total amount after 5 years is: 1469.33

### Home Loan Repayment Calculator
- **Input**:
  - Present Value: 100000
  - Interest Rate: 7
  - Months: 120
- **Output**:
  - The monthly repayment is: 1160.91

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
