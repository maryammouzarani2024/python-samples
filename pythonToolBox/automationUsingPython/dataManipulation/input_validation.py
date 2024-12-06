#input validation using pyinputplus


import pyinputplus as Pyip

result=Pyip.inputInt("Enter a positive number or zero:",min=0 )

print("You entered:" , result)


result=Pyip.inputMenu(["red","blue", "green"], lettered=True, numbered=False)

print("You have selected color ", result)

result=Pyip.inputEmail("Enter your email address: ")

print("Your email address: ", result)



#also some input validation through error handling

try:
    number=int(input("Enter a positive number: "))
    result=number/10
    print("The result is ", number)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot enter zero.")



#or using assertion:
years=[1720, 2012, 1894, 2023,2021]
years.reverse()
print(years)
assert years[0]<=years[-1], "First element is greater than the last one"