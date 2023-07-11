import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["diff", "annuity"], help="Select the type of calculation")
parser.add_argument("--principal", help="Enter the Principal amount")
parser.add_argument("--periods", help="Enter the number of periods")
parser.add_argument("--interest", help="Enter the interest")
parser.add_argument("--payment", help="Enter the payment")
args = parser.parse_args()
method = [args.type, args.principal, args.periods, args.interest, args.payment]

if method[0] == "diff" and method[1] and method[2] and method[3]:
    usr_loan_principal = float(method[1])  # "Enter the loan principal: "
    usr_periods = int(method[2])  # "Enter the number of periods: "
    usr_loan_interest = float(method[3])  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    overpayment = 0
    for i in range(1, usr_periods + 1):
        diff_payment = math.ceil(usr_loan_principal / usr_periods + monthly_interest *
                                 (usr_loan_principal - (usr_loan_principal*(i-1)/usr_periods)))
        overpayment = overpayment + diff_payment
        print(f"Month {i}: payment is {diff_payment}")
    overpayment = overpayment - usr_loan_principal
    print(f"Overpayment = {-overpayment}")
elif method[0] == "annuity" and method[1] and not method[2] \
        and method[3] and method[4]:
    years = 0
    usr_loan_principal = float(method[1])  # "Enter the loan principal: "
    usr_monthly_payment = float(method[4])   # "Enter monthly payment: "
    usr_loan_interest = float(method[3])  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    number_of_months = math.ceil(math.log(usr_monthly_payment /
                                          (usr_monthly_payment - (monthly_interest * usr_loan_principal))
                                          , 1 + monthly_interest))
    over_payment = usr_monthly_payment * number_of_months - usr_loan_principal
    while True:
        if number_of_months >= 12:
            years += 1
            number_of_months -= 12
        else:
            break
    if years != 0 and number_of_months != 0:
        print(f"It will take {years} years and {number_of_months} months to repay this loan!")
    elif years != 0 and number_of_months == 0:
        print(f"It will take {years} years to repay this loan!")
    elif years == 0:
        print(f"It will take {number_of_months} months to repay this loan!")

    print(f"Overpayment {math.ceil(over_payment)}")


elif method[0] == "annuity" and method[1] and method[2] \
        and method[3] and not method[4]:
    usr_loan_principal = float(method[1])  # "Enter the loan principal: "
    usr_periods = float(method[2])  # "Enter the number of periods: "
    usr_loan_interest = float(method[3])  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    annuity_payment = math.ceil(usr_loan_principal * ((monthly_interest *
                                            (1 + monthly_interest) ** usr_periods) /
                                            ((1 + monthly_interest) ** usr_periods - 1)))
    print(f"Your monthly payment = {annuity_payment}!")
elif method[0] == "annuity" and method[2] \
        and method[3] and method[4]:
    usr_loan_annuity = float(method[4])  # "Enter the annuity payment: "
    usr_periods = float(method[2])  # "Enter the number of periods: "
    usr_loan_interest = float(method[3])  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    loan_principal = ((usr_loan_annuity) / ((monthly_interest *
                                             (1 + monthly_interest) ** usr_periods) / (
                                            (1 + monthly_interest) ** usr_periods - 1)))
    over_payment = usr_loan_annuity * usr_periods - loan_principal
    print(f"Your loan principal = {math.floor(loan_principal)}!")
    print(f"Overpayment = {math.ceil(over_payment)}")
else:
    print("Incorrect parameters. ")
