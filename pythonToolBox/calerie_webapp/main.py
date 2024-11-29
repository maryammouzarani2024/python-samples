from cProfile import label

from flask.views import  MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request


from temperaturecalculator import  TemperatureCalculator
from caleriecalculator import CalerieCalculator

app=Flask(__name__)
class Homepage(MethodView):
    #we can omit the homepage, it is just for more practice
    def get(self):
        return  render_template('index.html')

class Calculate(MethodView):
    def get(self):
        calculate_form=CalculateForm()

        return  render_template('calculate.html', calc_form=calculate_form)
    def post(self):
        calculate_form=CalculateForm(request.form)
        t=TemperatureCalculator(city=calculate_form.city.data, country=calculate_form.country.data)
        if t.get():
            calerie=CalerieCalculator(weight=float(calculate_form.weight.data),
                                      height= float(calculate_form.height.data),
                                      temprature=float(t.get()),
                                      age=int(calculate_form.age.data))
            required_caleries=calerie.calculate()
            return render_template('calculate.html',
                                   calc_form=calculate_form,
                                   result=1,
                                   caleries=required_caleries
                                   )


class CalculateForm(Form):
        weight=StringField(label="Weight", default=100)
        height=StringField(label="Height", default=185)
        age=StringField(label="Age", default=34)
        city=StringField(label="City", default="Tehran")
        country=StringField(label="Country", default="Iran")
        calculate_button=SubmitField(label="Calculate")


app.add_url_rule("/", view_func=Homepage.as_view('home_page'))
app.add_url_rule("/caleries", view_func=Calculate.as_view('caleries_form_page'))

app.run(debug=True)#to run the app in the debug mode
