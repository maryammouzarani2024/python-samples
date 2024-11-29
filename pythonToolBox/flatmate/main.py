
import os
from flat import Bill, Flatmate

from reports import PdfReport
#recieve data from CLI

bill_amount=float(input("Type the bill amount: "))
print("This is the bill amount", bill_amount)

bill_period=input("What is the bill period? E.g. December 2023 ")

name1=input("What is your name? ")
days_in_house1=float(input(f"How many days did {name1} stay during the bill period? "))


name2=input("What is the name of your flatmate? ")
days_in_house2=float(input(f"How many days did {name2} stay during the bill period? "))

the_bill=Bill(amount=bill_amount, period=bill_period)
flatmate1=Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2=Flatmate(name=name2, days_in_house=days_in_house2)


print(f"{flatmate1.name} pays: ", flatmate1.pay(bill=the_bill, flatmate=flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pay(bill=the_bill, flatmate=flatmate1))


pdf_report=PdfReport(f"{bill_period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)