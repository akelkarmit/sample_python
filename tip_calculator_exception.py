import sys

flag = True

while flag  == True:
    try:
        meal_base = float(sys.argv[1])
        break
    except ValueError:
        meal_base = raw_input("please enter a numerical dollar value for meal cost: ")
        meal_base = float(meal_base)
        flag = False    

tip_rate = (float(sys.argv[2]) / 100)
tax_rate = (float(sys.argv[3]) / 100)

def main():
    total_meal = meal_base *(1 + (tip_rate + tax_rate))
    print "the total cost of meal was", total_meal

if __name__ == '__main__':
    main()

