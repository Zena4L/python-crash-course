# Program : Future value

# psuedocodes for problem

# Input: principal/ initial amount
# interest rate is fixed @ 3%/ann

# Output: value of investment in 10 years time

# author  : Clement Owireku-Bogyah



# total amount after one year  = p(1+r)
import math

def bank():
    print("Welcome to my Interest calculator\n------- HELLO ------")
    init = eval(input("Principal amount : "))
    temp = init
    print("Rate is flat @ 3%\n")
    rate = 3/100
    years = eval(input("How many years : "))
    for i in range(years):
        init = init * (1 + rate)

    print("In ",years,"years\nCalcualating ...")
    # print("Principal : ",p)
    profit = init - temp
    print("Rate : ",rate)
    print("Profit : ",round(profit,3))
    print("Total amout : ",round(init,3))

bank()