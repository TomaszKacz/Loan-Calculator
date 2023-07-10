import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("-t","--type",choices=["diff","annuity"],help="Select the type of calculation")
parser.add_argument("--principal",help="Enter the Principal amount")
parser.add_argument("--periods",help="Enter the number of periods")
parser.add_argument("--interest",help="Enter the interest")
parser.add_argument("--payment",help="Enter the payment")
args = parser.parse_args()
method = str([args.type, args.principal, args.periods, args.interest, args.payment])
check = 0
for i in range(0, 5):
    if method[i] is None:
        check += 1
if check >= 2:
    print("Incorrect parameters.")
elif method[0] == "annuity" and method[1] != "None" and method[2] == "None" \
        and method[3] != "None" and method[4] != "None" :
    years = 0
    usr_loan_principal = float(method[1])  # "Enter the loan principal: "
    usr_monthly_payment = float(method[4])   # "Enter monthly payment: "
    usr_loan_interest = float(method[3])  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    number_of_months = math.ceil(math.log(usr_monthly_payment /
                                          (usr_monthly_payment - (monthly_interest * usr_loan_principal))
                                          ,1 + monthly_interest))
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
elif method[0] == "annuity" and method[1] == "None" and method[2] != "None" \
        and method[3] != "None" and method[4] != "None":
    pass

elif method[0] == "diff" and method[1] != "None" and method[2] != "None" \
        and method[3] != "None" and method[4] == "None":
    usr_loan_principal = float(input())  # "Enter the loan principal: "
    usr_periods = int(input())  # "Enter the number of periods: "
    usr_loan_interest = float(input())  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    annuity_payment = math.ceil(usr_loan_principal * ((monthly_interest *
                                            (1 + monthly_interest) ** usr_periods)/
                                            ((1 + monthly_interest) ** usr_periods - 1)))
    print(f"Your monthly payment = {annuity_payment}!")
elif method[0] == "diff" and method[1] != "None" and method[2] != "None" \
        and method[3] != "None" and method[4] != "None":
    usr_loan_annuity = float(input())  #"Enter the annuity payment: "
    usr_periods = int(input())  # "Enter the number of periods: "
    usr_loan_interest = float(input())  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    loan_principal = ((usr_loan_annuity) / ((monthly_interest *
                                             (1 + monthly_interest) ** usr_periods) /(
                                            (1 + monthly_interest) ** usr_periods - 1)))
    print(f"Your loan principal = {loan_principal}!")
