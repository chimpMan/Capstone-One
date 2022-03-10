#fetching the math library so that we can use thr pow function
import math


#declaring variables to be used in both investment calculation and bond calculation
principle_amount=0.00

final_amount= 0.00

interest_rate = 0.00

period_years = 0

interest = ''

#declaring variables to be used in bond calculation only
house_value = 0.00

period_months = 0


#prompting user input by asking to choose a menu option
selection = input ("choose either 'investment' or 'bond' from the menu below to proceed:\n\n"\
                   
"investment  -  To calculate the amount that you earn on interest\n"\
                   
"bond        -  To calculate the amount you'll have to pay on a home loan\n")


#determining the user's choice and calculating according to the selection

#the first selection is investment

if selection == "investment":
    
    principle_amount = float(input("How much money are you depositing\n"))
    
    interest_rate = float(input("What interest rate do you want to apply to your amount? (hint : type in a number only)\n"))
    
    period_years = float(input("How many years are you planning to make your investment\n"))
    
    interest = input("Do you want compound interest or simple interest?\n")
    
    if interest == "simple":
        
        final_amount = principle_amount*(1+(interest_rate/100)*period_years)
        
        print (f"Your investment will be R{round(final_amount,2)} after {period_years} years\n")
        
    elif interest == "compound" :
        
        final_amount = principle_amount*pow((1+(interest_rate/100)),period_years)
        
        print (f" Your investment will be R{round(final_amount,2)} after {period_years} years\n")
        
    else:#displaying an error when neither simple nor compound options are chosen
        
        print("Choose between 'Simple' and 'Compound' interest only")
        
    
#bond is chosen instead of investment
        
elif selection == "bond" :
    
    house_value = float(input("What is the value of the house\n"))
    
    interest_rate = float(input("What is the interest rate for the house\n"))
    
    interest_rate = interest_rate/100
    
    period_months = int(input("How many months do you plan to make monthly payments\n"))
    
    final_amount =  (interest_rate*house_value)/(1-pow((1+interest_rate),(-period_months)))
    
    print (f"Your monthly payment on the house will be R{round(final_amount,2)}\n")

else: # displying an error when neither bond nor investment are chosen
    
    print("invalid option, please choose again")

