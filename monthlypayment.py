# Write a function that calculates and returns the monthly payments for a loan. 
# This function accepts three parameters in the exact order (principal, annual_interest_rate, duration):


def calc_monthly_payment(principal, annual_interest_rate, duration):
    p = float(principal)
    r = float((annual_interest_rate / 100) / 12)
    n = duration * 12

    if (annual_interest_rate == 0):
        monthly_payment = p / n
        print(monthly_payment)
    else:
        monthly_payment = p * r *((1+r)**n) / (((1+r)**n) - 1)
        print(monthly_payment)


money_lent = float(input("Enter loan amount: "))
rate = float(input("Enter rate: "))
length = int(input("For how long? "))

calc_monthly_payment(money_lent, rate, length)
