class Bill:
    """ This is a class that holds data about the bills
    """

    def __init__(self, amount, period):
        self.amount=amount
        self.period=period

class Flatmate:
    """ create a flatmate person who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name=name
        self.days_in_house=days_in_house

    def pay(self, bill, flatmate):
        weight= self.days_in_house/(self.days_in_house+ flatmate.days_in_house)
        to_pay=bill.amount*weight
        return to_pay
