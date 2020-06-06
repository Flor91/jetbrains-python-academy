import math
import argparse
import sys


def beginning():
    credit_principal = 'Credit principal: 1000'
    final_output = 'The credit has been repaid!'
    first_month = 'Month 1: paid out 250'
    second_month = 'Month 2: paid out 250'
    third_month = 'Month 3: paid out 500'

    # write your code here
    print(credit_principal)
    print(first_month)
    print(second_month)
    print(third_month)
    print(final_output)


def old_menu():
    print("""
    What do you want to calculate? 
    type "n" - for count of months, 
    type "a" - for annuity monthly payment,
    type "p" - for credit principal:
    """)
    calculation = input()

    if calculation == "n":
        months_count()
    elif calculation == "a":
        annuity_monthly_payments()
    elif calculation == "p":
        credit_principal()
    else:
        print("Invalid option")


def menu(type, payment, principal, period, interest):
    if type == "diff":
        differentiated_payments(principal, period, interest)
    elif type == "annuity" and not payment:
        annuity_monthly_payments(principal, period, interest)
    elif type == "annuity" and not principal:
        credit_principal(payment, period, interest)
    elif type == "annuity" and not period:
        months_count(payment, principal, interest)


def differentiated_payments(principal, periods, interest):
    total_payed = 0
    for month in range(1, periods + 1):
        ivalue = interest / 1200
        pvalue = principal - (principal * (month - 1) / periods)
        diff_payment = math.ceil((principal / periods) + ivalue * pvalue)

        total_payed += diff_payment
        print("Month {}: paid out {}".format(month, int(diff_payment)))

    overpayment = total_payed - principal
    print("")
    print("Overpayment {}".format(int(overpayment)))


def months_count(monthly_payments, credit_principal, credit_interest):
    nominal_interest_rate = credit_interest / (12 * 100)

    x = monthly_payments / (monthly_payments - nominal_interest_rate * credit_principal)
    base = 1 + nominal_interest_rate
    log = math.log(x, base)
    periods = math.ceil(log)

    years = int(math.floor(periods / 12))
    months = int(math.ceil(periods % 12))

    overpayment = monthly_payments * periods - credit_principal

    month_string = "and " + str(months) + " month{s}".format(s=("s" if months > 1 else "")) if months > 0 else ""
    print("You need {years} year{s} {month_string} to repay this credit!".format(years=years,
                                                                                 s=("s" if years > 1 else ""),
                                                                                 month_string=month_string))
    print("Overpayment: " + str(int(overpayment)))


def annuity_monthly_payments(credit_principal, months, credit_interest):
    nominal_interest_rate = credit_interest / (12 * 100)
    y = math.pow(1 + nominal_interest_rate, months)
    x = (nominal_interest_rate * y) / (y - 1)
    annuity_payment = math.ceil(credit_principal * x)
    overpayment = annuity_payment*months - credit_principal

    print("Your annuity payment = {payment}!".format(payment=int(annuity_payment)))
    print("Overpayment: " + str(int(overpayment)))


def credit_principal(monthly_payment, months, credit_interest):
    nominal_interest_rate = credit_interest / (12 * 100)
    y = math.pow(1 + nominal_interest_rate, months)
    x = (nominal_interest_rate * y) / (y - 1)

    credit_principal = math.floor(monthly_payment / x)

    print("Your credit principal = {credit}!".format(credit=int(credit_principal)))
    overpayment = int(monthly_payment*months - credit_principal)
    print("Overpayment: " + str(overpayment))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="type of payments: 'annuity' or 'diff' (differentiated).")
    parser.add_argument("-pa", "--payment", help="a monthly payment", type=int)
    parser.add_argument("-pr", "--principal", help="used for calculations of both types of payment. You can get its value "
                                          "knowing the interest, annuity payment and periods", type=int)
    parser.add_argument("-pe", "--periods", help="parameter denotes the number of months and/or years needed to repay the "
                                        "credit. It's calculated based on the interest, annuity payment and "
                                        "principal.", type=int)
    parser.add_argument("-i", "--interest", help="nominal interest rate", type=float)
    args = parser.parse_args()
    print(args)

    # Validate arguments
    if "type" not in args or (args.type != "annuity" and args.type != "diff") or "interest" not in args:
        print("Incorrect parameters")
    elif args.type == "diff" and args.payment:
        print("Incorrect parameters")
    elif len(sys.argv) < 5:
        print("Incorrect parameters")
    elif args.payment and args.payment < 0:
        print("Incorrect parameters")
    elif args.principal and args.principal < 0:
        print("Incorrect parameters")
    elif args.periods and args.periods < 0:
        print("Incorrect parameters")
    elif args.interest and args.interest < 0:
        print("Incorrect parameters")
    else:
        menu(type=args.type, payment=args.payment, principal=args.principal, period=args.periods, interest=args.interest)
