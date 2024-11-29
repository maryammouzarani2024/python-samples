from cProfile import label

from flask.views import  MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

from pythonProjects.flatmatesWeb.flatmateBill.flat import Flatmate
from pythonProjects.flatmatesWeb.flatmateBill.flat import Bill
from flatmateBill.reports import PdfReport

app=Flask(__name__)# flask obj presents the whole web application

class Homepage(MethodView):
    def get(self):
        return  render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form=BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        billform = BillForm(request.form)

        the_bill = Bill(amount=float(billform.amount.data), period=billform.period.data)
        flatmate1 = Flatmate(name=billform.name1.data,
                             days_in_house=int(billform.days_in_house1.data)
                             )
        flatmate2 = Flatmate(name=billform.name2.data,
                             days_in_house=int(billform.days_in_house2.data))

        share1 = flatmate1.pay(bill=the_bill, flatmate=flatmate2)
        share2 = flatmate2.pay(bill=the_bill, flatmate=flatmate1)
        # pdf can also be generated
        # pdf_report = PdfReport(f"{the_bill.period}.pdf")
        # pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

        return render_template('bill_form_page.html',
                               billform=billform,
                               result=1,
                               name1=flatmate1.name, name2=flatmate2.name,
                               part1=share1, part2=share2)


class ResultPage(MethodView):
    def post(self):
        billform=BillForm(request.form)

        the_bill = Bill(amount=float(billform.amount.data), period=billform.period.data)
        flatmate1 = Flatmate(name=billform.name1.data,
                             days_in_house=int(billform.days_in_house1.data)
)
        flatmate2 = Flatmate(name= billform.name2.data,
                             days_in_house=int(billform.days_in_house2.data))

        share1=flatmate1.pay(bill=the_bill, flatmate=flatmate2)
        share2= flatmate2.pay(bill=the_bill, flatmate=flatmate1)
        #pdf can also be generated
        # pdf_report = PdfReport(f"{the_bill.period}.pdf")
        #pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

        return  render_template('results.html',
                                name1=flatmate1.name, name2=flatmate2.name,
                                part1=share1, part2=share2 )
class BillForm(Form):
    amount=StringField(label="Bill Amount: ", default=120)
    period=StringField(label="Bill Period: ", default="March 2024")

    #first flatmate
    name1=StringField(label="Name: ", default="John")
    days_in_house1=StringField(label= "Days is house: ", default=21)

    #Second flatmate
    name2=StringField(label="Name: ", default="Marry")
    days_in_house2=StringField(label= "Days is house: ", default=20)

    button=SubmitField(label="Calculate")


app.add_url_rule('/',view_func= Homepage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page')) #'bill_form_page' is the view class name for BillFormPage class
app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))

app.run(debug=True)#to run the app in the debug mode

