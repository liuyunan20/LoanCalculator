# write your code here
import math
import argparse

# parse arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument("--type",
                    choices=["annuity", "diff"],
                    help="You need to choose one of the two calculation types")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
arg_list = [args.type, args.payment, args.principal, args.periods, args.interest]
if len(arg_list) < 4 \
        or args.interest is None\
        or args.interest < 0\
        or (args.payment is not None and args.payment < 0)\
        or (args.principal is not None and args.principal < 0)\
        or (args.periods is not None and args.periods < 0):
    print("Incorrect parameters")
else:
    i = args.interest / 1200
    if args.type == "annuity":
        # calculate loan principal
        if args.principal is None:
            p = round(args.payment / (i * math.pow((1 + i), args.periods) / (math.pow((1 + i), args.periods) - 1)))
            over_payment = args.payment * args.periods - p
            print(f"Your loan principal = {str(p)}!")
            print(f"Overpayment = {str(over_payment)}")
        # calculate annuity payment
        if args.payment is None:
            a = math.ceil(args.principal * i * math.pow((1 + i), args.periods) / (math.pow((1 + i), args.periods) - 1))
            print(f"Your monthly payment = {str(a)}!")
            over_payment = a * args.periods - args.principal
            print(f"Overpayment = {str(over_payment)}")
        # calculate number of payments
        if args.periods is None:
            n = math.ceil(math.log((args.payment / (args.payment - i * args.principal)), (1 + i)))
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
            over_payment = args.payment * n - args.principal
            print(f"Overpayment = {str(over_payment)}")
    if args.type == "diff":
        if args.payment is not None:
            print("Incorrect parameters")
        else:
            diff_pays = [math.ceil(args.principal / args.periods + i * (args.principal - args.principal * m / args.periods)) for m in range(args.periods)]
            total_payment = 0
            for m in range(args.periods):
                print(f"Month {m + 1}: payment is {diff_pays[m]}")
                total_payment += diff_pays[m]
                over_payment = total_payment - args.principal
            print(f"Overpayment = {str(over_payment)}")
