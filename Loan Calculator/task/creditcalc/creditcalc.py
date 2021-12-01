# write your code here
import math
import argparse

# parse arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument("--type",
                    choices=["annuity", "diff"],
                    help="You need to choose one of the two calculation types")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()
arg_list = [args.tpye, args.payment, args.principal, args.periods, args.interest]
if len(arg_list) < 4 or args.interest is None:
    print("Incorrect parameters")
else:
    if args.type == "annuity":


print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
cal_type = input()

# calculate loan principal
if cal_type == "p":
    print("Enter the monthly payment:")
    a = float(input())  # annuity payment
    print("Enter the number of periods:")
    n = int(input())  # number of payments
    print("Enter the loan interest:")
    i = float(input()) / 1200  # interest
    p = round(a / (i * math.pow((1 + i), n) / (math.pow((1 + i), n) - 1)))
    print(f"Your loan principal = {str(p)}!")
# calculate annuity payment
if cal_type == "a":
    print("Enter the loan principal:")
    p = float(input())  # loan principal
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the loan interest:")
    i = float(input()) / 1200
    a = math.ceil(p * i * math.pow((1 + i), n) / (math.pow((1 + i), n) - 1))
    print(f"Your monthly payment = {str(a)}!")
# calculate number of payments
if cal_type == "n":
    print("Enter the loan principal:")
    p = float(input())
    print("Enter the monthly payment:")
    a = float(input())
    print("Enter the loan interest:")
    i = float(input()) / 1200
    n = math.ceil(math.log((a / (a - i * p)), (1 + i)))
    if n % 12 == 0:
        month = ""
    elif n % 12 == 1:
        month = "1 month"
    else:
        month = str(n % 12) + " months"
    if n // 12 == 0:
        year = ""
    elif n // 12 == 1:
        year = "1 year"
    else:
        year = str(n // 12) + " years"
    if month == "" or year == "":
        connection = ""
    else:
        connection = " and "
    print(f"It will take {year}{connection}{month} to repay this loan!")

