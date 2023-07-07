import math

method = str(input())  # 'What do you want to calculate? type "n" for number of monthly payments, type "a" for annuity monthly payment amount, type "p" for loan principal: '
if method == "n":
    years = 0
    usr_loan_principal = float(input())   # "Enter the loan principal: "
    usr_monthly_payment = float(input())   # "Enter monthly payment: "
    usr_loan_interest = float(input())  # "Enter the loan interest: "
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
elif method == "a":
    usr_loan_principal = float(input())  # "Enter the loan principal: "
    usr_periods = int(input())  # "Enter the number of periods: "
    usr_loan_interest = float(input())  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    annuity_payment = math.ceil(usr_loan_principal * ((monthly_interest *
                                            (1 + monthly_interest) ** usr_periods)/
                                            ((1 + monthly_interest) ** usr_periods - 1)))
    print(f"Your monthly payment = {annuity_payment}!")
elif method == "p":
    usr_loan_annuity = float(input())  #"Enter the annuity payment: "
    usr_periods = int(input())  # "Enter the number of periods: "
    usr_loan_interest = float(input())  # "Enter the loan interest: "
    monthly_interest = float((usr_loan_interest / 100) / 12)
    loan_principal = ((usr_loan_annuity) / ((monthly_interest *
                                             (1 + monthly_interest) ** usr_periods) /(
                                            (1 + monthly_interest) ** usr_periods - 1)))
    print(f"Your loan principal = {loan_principal}!")