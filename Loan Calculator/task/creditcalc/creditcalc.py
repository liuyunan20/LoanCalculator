# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

# write your code here
print("Enter the loan principal:")
prcp = float(input())
print('''What do you want to calculate? 
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
cal_type = input()
if cal_type == "m":
    print("Enter the monthly payment:")
    m_payment = float(input())
    periods = round(prcp / m_payment)
    if periods != 1:
        print("It will take " + str(periods) + " months to repay the loan")
    else:
        print("It will take 1 month to repay the loan")
if cal_type == "p":
    print("Enter the number of months:")
    periods = int(input())
    if prcp % periods == 0:
        m_payment = int(prcp / periods)
        print("Your monthly payment = " + str(m_payment))
    else:
        if prcp / periods > round(prcp / periods):
            m_payment = round(prcp / periods) + 1
        else:
            m_payment = round(prcp / periods)
        last_payment = int(prcp - m_payment * (periods - 1))
        print("Your monthly payment = " + str(m_payment) + " and the last payment = " + str(last_payment) + ".")
