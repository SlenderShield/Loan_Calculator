import math
import argparse

loan_principal = int(input("Enter the loan principal:"))

print(
    """What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:"""
)
value = input()


def calc_num_months(amount):
    months = math.ceil(loan_principal / amount)
    print(f"It will take {months} month to repay the loan")


def calc_pay_monthly(months):
    if loan_principal % months == 0:
        payment = loan_principal / months
        print(f"Your monthly payment = {payment}")
    else:
        payment = math.ceil(loan_principal / months)
        last = loan_principal - (months - 1) * payment
        print(f"Your monthly payment = {payment} and the last payment = {last}.")


if value == "m":
    monthly = int(input("Enter the monthly payment:"))
    calc_num_months(monthly)
elif value == "p":
    numOfMonths = int(input("Enter the number of months:"))
    calc_pay_monthly(numOfMonths)
