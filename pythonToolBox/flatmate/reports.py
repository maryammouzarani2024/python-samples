

from fpdf import FPDF
import webbrowser
import os

class PdfReport:
    """ Creates pdf reports about various objects
        For example, creates pdf report about the flatmates and the amount of bill they must
        pay
        """
    
    def __init__(self, filename):
        self.filename=filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf=FPDF(orientation='p',unit='pt', format='A4' )
        #create a pdf file without pages
        #portrait orientation, units in milimeter by default
        # and we want points insteads, the format of the pages as A4
        pdf.add_page()
        
        #add an image which is in the file home.png
        pdf.image(name="files/home.png", w=30, h=40)
        
        #add some text

        pdf.set_font(family='Times', size=24, style='B')

        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1) # at the very top we draw a cell with weight 100 and height 80
        #ln=1 so the cell is in one line and the next cell is in the next line
        #w=0 so that it takes the whole line
        pdf.set_font(family="Times", size=22, style='B')
        pdf.cell(w=150, h=40, txt="Period:", border=1)
        pdf.cell(w=0, h=40, txt=str(bill.amount), border=1, align="C", ln=1)
        #border=0 not to see a rectangle around the cell

        pdf.set_font(family="Times", size=20)
        pdf.cell(w=150, h=20, txt=flatmate1.name, border=1)
        pdf.cell(w=0, h=20, txt=str(flatmate1.pay(bill, flatmate2)), border=1, align="C", ln=1 )

        pdf.cell(w=150, h=20, txt=flatmate2.name, border=1)
        pdf.cell(w=0, h=20, txt=str(flatmate2.pay(bill, flatmate1)), border=1, align="C", ln=1 )
        
        
        #change the current directory to files 
        os.chdir("files")
        pdf.output(self.filename)
        #to automatically open the pdf file
        #webbrowser.open('file:\\' + os.path.realpath(self.filename))
        webbrowser.open(self.filename)
