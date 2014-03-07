print "this program asks for your birthday and tells you the day of the\nweek when you were born"

import calendar
birthdate=raw_input("enter your birthdate in dd-mm-yyyy format:")
#raw_input assumes the input is a string

date_of_birth=birthdate.split('-')

day_of_birth=int(date_of_birth[0])
month_of_birth=int(date_of_birth[1])
year_of_birth=int(date_of_birth[2])

#print day_of_birth
#print month_of_birth
#print year_of_birth

day_of_week = calendar.weekday(year_of_birth,month_of_birth,day_of_birth)

day_mapping_dict = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
print "you were born on a ",day_mapping_dict[day_of_week]

##print "****************************"
##if day_of_week == 0:
##    print "you were born on a Monday"
##elif day_of_week == 1:
##    print "you were born on a Tuesday"
##elif day_of_week ==2:
##    print "you were born on a Wednesday"
##elif day_of_week == 3:
##    print "you were born on a Thursday"
##elif day_of_week == 4:
##    print "you were born on a Friday"
##elif day_of_week == 5:
##    print "you were born on a Saturday"
##elif day_of_week == 6:
##    print "you were born on a Sunday"
##print "****************************"
