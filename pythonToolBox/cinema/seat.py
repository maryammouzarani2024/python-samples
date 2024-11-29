import sqlite3
from fpdf import FPDF
import webbrowser
import os


class Seat:
    ticket_id=1
    def __init__(self, id) :
        self.id=id
        
        
    def check_for_available(self, id):
            connection=sqlite3.connect("cinema.db")
            cursor=connection.cursor()
            cursor.execute("""
                SELECT * FROM "seats" WHERE "seat_id"=?

                        """,[id] )
            result=cursor.fetchall()
            if result.__len__()>0:
                self.price=result[0][2]
                self.taken=result[0][1]
                if not self.taken:  
                    return self.price #there will never be a free seat
                else: 
                    return 0 
    def buy(self):
        self.taken=0
        connection=sqlite3.connect("cinema.db")
        connection.execute("""
            UPDATE "seats" SET "taken"=1 WHERE "seat_id"=?
            """ , [self.id])
        connection.commit()
        connection.close()
    def create_pdf(self, username):
        pdf=FPDF(orientation='p',unit='pt', format='A4' )
        #create a pdf file without pages
        #portrait orientation, units in milimeter by default
        # and we want points insteads, the format of the pages as A4
        pdf.add_page()
        
        #add an image which is in the file home.png
        
        #add some text

        pdf.set_font(family='Times', size=24, style='B')

        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, align="C", ln=1) # at the very top we draw a cell with weight 100 and height 80
        #ln=1 so the cell is in one line and the next cell is in the next line
        #w=0 so that it takes the whole line
        pdf.set_font(family="Times", size=22, style='B')
        pdf.cell(w=150, h=40, txt="Name: ", border=1)
        
        pdf.set_font(family="Times", size=20)
        pdf.cell(w=0, h=40, txt=str(username), border=1, align="C", ln=1)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)


        pdf.set_font(family="Times", size=22, style='B')
        pdf.cell(w=150, h=40, txt="Ticket ID:", border=1)

        pdf.set_font(family="Times", size=20)
        pdf.cell(w=0, h=40, txt=str(self.ticket_id), border=1, align="C", ln=1)
        self.ticket_id=self.ticket_id+1
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        pdf.set_font(family="Times", size=22, style='B')
        pdf.cell(w=150, h=40, txt="Price:", border=1)

        pdf.set_font(family="Times", size=20)
        pdf.cell(w=0, h=40, txt=str(self.price), border=1, align="C", ln=1)
        pdf.cell(ln=1, h=5.0, align='L', w=0, txt="", border=0)

        pdf.set_font(family="Times", size=22, style='B')
        pdf.cell(w=150, h=40, txt="Seat Number:", border=1)
        
        pdf.set_font(family="Times", size=20)
        pdf.cell(w=0, h=40, txt=str(self.id), border=1, align="C", ln=1)

        self.filename=f"{username}-{self.ticket_id-1}.pdf"
        #change the current directory to files 
        # os.chdir("files")
        pdf.output(self.filename)
        #to automatically open the pdf file
        # webbrowser.open('file:\\' + os.path.realpath(self.filename))
        #webbrowser.open(self.filename)
