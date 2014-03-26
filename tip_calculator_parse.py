from optparse import OptionParser

parser = OptionParser()

#create an instance of OptionParser that we can use.

parser.add_option("-meal","--meal",dest = "meal", 
	help ="first argument")

parser.add_option("-tip","--tip",dest = "tip",
	help="sec arg", default = 15)

parser.add_option("-tax","--tax",dest = "tax",
	help="third arg", default = 8.25)

#we are adding 2 slots in our parser so we pass 2 named arguments
#from the command line. At command line run command:
# python tip_calculator_parse.py -f "type first arg" -s 
#"type sec arg"


(options,args) = parser.parse_args()

#this calls the parser args method on our parser, which will assign
#user inputs to the two destinations in line 7 and 8

#if not (options.first_arg and options.second_arg):
#	parser.error("You need to supply an argument for -s")

#raises error 

# tax_value = meal * tax/100
# meal_with_tax = meal + tax_value
# tip_value = meal_with_tax * tip/100

# total = meal_with_tax + tip_value

# print " the base cost of your meal is :  $",("%.2f" % meal)
# print " the tax on your meal is       :  $",("%.2f" %tax_value)
# print " the tip on this meal is       :  $",("%.2f" %tip_value)
# print " the total cost of your meal is:  $",("%.2f" %total)
print "the meal cost is '{}'.".format(options.meal)
print "the tip is '{}'.".format(options.tip)
print "the tax is '{}.".format(options.tax)
