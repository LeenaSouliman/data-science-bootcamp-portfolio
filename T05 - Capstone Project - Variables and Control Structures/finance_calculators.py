import math

# welcome comment to the finanacial calculator 
# add import math
# define the type of investment
# ask user to input the type of investment from 2 options investment or bond
# ensure that the output is not case sensative i.e use str.lower to place output into lower case
# display selected option
# include 'break' to exit loop when condition is met
#
# hierachy summery: Calculator --> option 1.'investment' followed by two options 1a-simple or 1b-compound investment
# hierachy summery: Calculator --> option 2.'bond'
# use while loop to ask user unknown number of times until condition is met
#---------------------------------------------------------------------------------------------------------------
# if investment is selected, use input function to request the following: 
#  - amount of money being deposited 
#  - interest rate percentage
#  - number of years they plan on investing
#  - type of interest 'simple' or 'compund' 
#  
# if simple is selected within investment 
#  - apply equation: A= P*(1+r*t)
#  - where:
#   - A is total amount once interest has been applied
#   - p deposit amount
#   - r interest/100 
#   - t number of year of investment


print("Welcome to investment calculator! We offer two investment calulator options: \n")
print ("Investment - to calculate the amount of interest you'll earn on your investment")
print ("Bond - to calculate the amount you'll have to pay on a home loan \n")

while True :
    investment_result = str.lower(input("Enter either 'investemnt' or 'bond' to proced: "))
    investment_selected = investment_result.strip()
    
    if (investment_selected == "bond"):
        print("You have selected Bond \n")
        break 
    
    elif (investment_selected == "investment"):
        print("You have selected Investment \n")
        break
    
    else: 
        print("You have selected an invalid option, try again")
        
if investment_selected == "investment" :
    money_deposited = float(input("Enter money to be deposited: ")) # float as a decimal can occure, this is 'p' in the equation
    interest_rate=int(input("Enter the interest rate precentage: ")) 
    investment_years=int(input("Enter the number of years you plan on investing: ")) #this is 't' in the equation 
    interest = str.lower(input("Enter either 'Simple' or 'Compound' interest:  "))
    r= interest_rate / 100 #'r' in the equation 
    
    if interest == "simple" :
        simple_interest = money_deposited * (1+(r * investment_years ))
        print("Payment" , simple_interest)
        
    elif (interest =="compound") :
        compound_interst = money_deposited * math.pow(1+r,investment_years)
        print("Payment" , compound_interst)
    else: 
        print("Entered option incorrect, try again ")
        
elif (investment_selected =="bond") :
    property_value = int(input("Enter the value of property:  ")) # 'P' in eqution as the present value of the house
    annual_interest_rate = int(input("Enter the interest rate percentage: ")) # 'r' in the equation 
    monthly_interest_rate = (annual_interest_rate /100)/12 #'i' in the equation, divide by 100 to get precentage and divide by 12 to get per month 
    repayment_month = int(input("Enter the number of months you plan to take to repay:  ")) #'n' in the equation 
    repayment = (monthly_interest_rate * property_value) / (1- (1+monthly_interest_rate)** (-repayment_month))
    print("Repayemnt on the homeloan:", repayment)


