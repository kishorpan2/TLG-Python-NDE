#idea is to list holiday of every month
#user will be prompted to enter a number between 1 and 12
month =0
print("please enter a number between 1 and 12:")
month= int(input())
if month ==1:
    print("Its a new year")
elif month ==2:
    print("it's a President's day")
elif month==3:
    print("its a St.Patrick's day")
elif month ==4:
    print("its a April fool's day")
elif month ==5:
    print("its a Cinco de Mayo")
elif month ==6:
    print("it's Army birtday")
elif month ==7:
    print("its an Independence day")
elif month ==8:
    print("Would be nice to get a holiday")
elif month==9:
    print("its a lobor day")
elif month==10:
    print("its a Colombus day")
elif month ==11:
    print("its a Veteran's day")
elif month ==12:
    print("It's Christmas!")
else:
     print("Invalid input")
try:
    if int(month) > 12:
        raise ValueError ('Invalid month')
except ValueError as msg:
    print('The program found an ',msg, "error")
