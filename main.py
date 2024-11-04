import math
import argparse

parser = argparse.ArgumentParser(description="Loan Calculator.")

parser.add_argument("-prin", "--principal",
                    help="You need to give principal amount.")
parser.add_argument("-pay", "--payment",
                    help="You need to give payment amount.")
parser.add_argument("-per", "--periods",
                    help="You need to give number of months.")
parser.add_argument("-i", "--interest",
                    help="You need to give the interest amount.")

args = parser.parse_args()


def find_periods(prin, pay, inter):
    calc_value_for_payments = pay / (pay - (inter * prin))

    num_of_payments = math.ceil(math.log(calc_value_for_payments, 1 + inter))

    if num_of_payments > 12:
        years = num_of_payments // 12
        months = num_of_payments % 12
        if months > 0:
            print(f"It will take {years} years and {months} months to repay this loan!")
        else:
            print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {num_of_payments} months to repay this loan!")


def calc_payments(prin, peri, inter):
    calc_value = math.pow(1 + inter, peri)
    pay = math.ceil(prin * (inter * calc_value) / (calc_value - 1))
    print(f"Your monthly payment = {pay}!")


def calc_principal(pay, peri, inter):
    calc_value = math.pow((1 + inter), peri)

    calc_time = (inter * calc_value) / (calc_value - 1)

    prin = pay / calc_time
    print(f"Your loan principal = {prin}!")


if args.periods is None:
    interest = float(args.interest)
    principal = float(args.principal)
    payment = float(args.payment)
    interest_value = interest / (100 * 12)
    find_periods(principal, payment, interest_value)

if args.payment is None:
    interest = float(args.interest)
    principal = float(args.principal)
    periods = float(args.periods)
    interest_value = interest / (100 * 12)
    calc_payments(principal, periods, interest_value)

if args.principal is None:
    interest = float(args.interest)
    payment = float(args.payment)
    periods = float(args.periods)
    interest_value = interest / (100 * 12)
    calc_principal(payment, periods, interest_value)
