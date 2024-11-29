
class CalerieCalculator:
    """
    Calculates the required calerie for a person according the following formula:
    BMR=10*weight + 6.25*height - 5* age + 5 - 10*temprature
    """

    def __init__(self, weight, height, age, temprature):
        self.weight=weight
        self.height=height
        self.age= age
        self. temprature=temprature


    def calculate(self):
        result= self.weight* 10+ 6.25 * self.height - 5* self.age + 5 - 10*self.temprature
        return  result
