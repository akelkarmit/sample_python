## age of the person

age_input = input("What is your age in years? ")
age = int(age_input)

## marital status of the person

single = str(input("Are you single (Y/N)? " ))
if single == "N" or single == "n":
        spouse = input("Does your spouse work full-time(Y/N)? ")
else: spouse = "N"

## does the person have children

children = input("Do you have any children(Y/N)? ")        
if children == "Y" or children == "y":
        number_children = input("How many kids do you have? " )
else: children = "N"


## retirement plans

employer_plan = input("Does your employer have a 401k plan(Y/N)? ")        
if employer_plan == "Y" or employer_plan == "y":
        max_employer_plan = input("Are you maxing your 401k contributions(Y/N)? " )

ira_plan = input("Do you have an IRA or Roth IRA (Y/N)? ")


## does the person own a home
home = input("Do you own a home? (Y/N) ")		
if home == "Y" or home == "y":
	mortgage = int(input("What is your approximate monthly mortgage? " ))
	prop_tax = int(input("What is your annual property tax? " ))
	
elif home == "N" or home == "n":
        mortgage = 0
        prop_tax = 0

## annual household income 
annual_income_input = input("What is your annual household income in USD? ")
annual_income = int(annual_income_input)
        
if spouse == "Y" or spouse == "y":
        emergency_cash = ((annual_income * 0.65)/12)*3
else:   emergency_cash = ((annual_income * 0.65)/12)*6        

        
monthly_income = annual_income/12
after_tax_monthly = monthly_income*0.65
monthly_discretionary = after_tax_monthly - mortgage - (prop_tax/12)

print "your average monthly after tax income is", int(after_tax_monthly), "USD"
print "*"*50
print "your average discretionary income is", int(monthly_discretionary), "USD"
print "*"*50
print "you should always have an emergency savings (in cash) of ", int(emergency_cash) , " USD"
print "*"*50

def retirement(employer_plan,max_employer_plan,ira_plan,annual_income):
        if max_employer_plan == 'Y' or max_employer_plan == 'y':
                print ("you are maxing out your 401k, good work, please keep it up.")
                if (annual_income < 110000) and (single == "Y" or single == "y") :
                        print("you may be eligible for IRA or Roth IRA plans")
                        print("http://www.irs.gov/Retirement-Plans/Plan-Sponsor/Types-of-Retirement-Plans-1")
                if (annual_income < 173000) and (single == "N" or single == "n") :
                        print("you may be eligible for IRA or Roth IRA plans")
                        print("http://www.irs.gov/Retirement-Plans/Plan-Sponsor/Types-of-Retirement-Plans-1")
                        
                
        if (employer_plan == 'Y' or employer_plan == 'y') and (max_employer_plan == 'N' or max_employer_plan == 'n'):
                print ("This is your best shot at a good Retirement!!. Please consider maxing out your 401k contributions.")
        




def allocation(age):
        stock = (110 - age)
        bonds = 100.0 - stock
        large_cap = stock*0.5
        mid_cap = stock*0.3
        small_cap = stock*0.15
        international_stocks = stock - large_cap - mid_cap - small_cap

        print "With the rest of the rest of your savings"
        print "*"*50
        print ("invest", int(bonds), " % of your assets in bonds")
        print()
        print ("invest", int(large_cap), " % of your assets in large cap stocks")
        print()
        print ("invest", int(mid_cap), " % of your assets in mid cap stocks")
        print()
        print ("invest", int(small_cap), " % of your assets in small cap stocks")
        print()
        print ("invest", int(international_stocks), " % of your assets in intl stocks")

allocation(age)

retirement(employer_plan,max_employer_plan,ira_plan,annual_income)


##-----old code ------------------
##stock = (110 - age)
##bonds = 100.0 - stock

##if age <= 40:
##        large_cap = (0.3)*stock
##        mid_cap = (0.25)*stock
##        small_cap = (0.15)*stock
##        international_stocks = (0.3)*stock
##        
##if 40 < age <= 50: 
##        large_cap = (0.35)*stock
##        mid_cap = (0.3)*stock
##        small_cap = (0.15)*stock
##        international_stocks = (0.2)*stock
##
##if 50 < age <= 60:
##        large_cap = (0.45)*stock
##        mid_cap = (0.3)*stock
##        small_cap = (0.1)*stock
##        international_stocks = (0.15)*stock
##
##if age > 60:
##        large_cap = (0.65)*stock
##        mid_cap = (0.2)*stock
##        small_cap = (0.1)*stock
##        international_stocks = (0.05)*stock
##-----end of old code -------------        
