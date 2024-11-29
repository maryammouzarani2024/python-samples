import sqlite3

class Accounts:

    def __init__(self, number, cvc):
        self.number=number
        self.cvc=cvc
    
    def check_validity(self):
        connection=sqlite3.connect("banking.db")
        cursor=connection.cursor()
        cursor.execute("""
                        SELECT * from "cards" WHERE "number"=? AND "cvc"=?
                    """, [self.number, self.cvc])
        result=cursor.fetchall()
        if result.__len__()== 0:
            return 0
        self.balance=result[0][4]
        self.holder=result[0][3]
        return result
    
    def update_card(self, price):
        result=self.check_validity()
        if result and result.__len__() >0: 
            if result[0][4]> price:
                    connection=sqlite3.connect("banking.db")
                    connection.execute("""
                            UPDATE "cards" SET "balance"=? WHERE "number"=?
                            """ ,[self.balance-price, self.number])
                    connection.commit()
                    connection.close()
                    print("transaction completed")
                    return 1

            else:
                print("There is not enough balance in this card")
                return 0
        else:
            print("your card is invalid")
            return 0
        