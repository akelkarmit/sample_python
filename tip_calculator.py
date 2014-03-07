meal = 44.56
tax = 8.35/100
tip = 15.0/100

tax_value = meal * tax
meal_with_tax = meal + tax_value
tip_value = meal_with_tax * tip

total = meal_with_tax + tip_value

print " the base cost of your meal is $",("%.2f" % meal)
print " the tax on your meal is $",("%.2f" %tax_value)
print " the tip on this meal is $",("%.2f" %tip_value)
print " the total cost of your meal is $",("%.2f" %total)
