#app_pass=csbq skfe bwpv ozxn

import yagmail
import pandas
from news import NewsFeed
import datetime

def send_email():
    nf = NewsFeed(interest=row['interests'], from_date=yesterday, to_date=today)
    email = yagmail.SMTP(user="abcd@gmail.com", password="get-the-passcode-of-your-account-from-google")
    email.send(to=f"{row['email']}",
               subject=f"Your {row['interests']} news today!",
               contents=f"Hi {row['name']}! \n See what's on about {row['interests']} today. {nf.get()}\n Maryam",
               )


while True:
    if datetime.datetime.now().hour==10 and datetime.datetime.now().minute==0:
            #extracting data from an excel file
            df= pandas.read_excel('people.xlsx')
            today=datetime.datetime.today().strftime('%Y-%m-%d')
            yesterday= datetime.datetime.today()- datetime.timedelta(days=1)
            yesterday=yesterday.strftime('%Y-%m-%d')
            #iterate in the df rows:
            for index, row in df.iterrows():
                send_email()
            break  # or you can do time.sleep(60) so that the time changes and the condition gets false

