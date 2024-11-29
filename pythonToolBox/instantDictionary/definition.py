
import pandas
class Definition:

    def __init__(self,term):
        self.term=term

    def get(self):
        # read the content of data file into a pandas dataframe
        df=pandas.read_csv('data.csv')
        #search through the dataframe for records with the term value in the words column and get the
        #value of their definition column
        result=df.loc[df['word']==self.term]['definition']
        return result

"""
if __name__=='main':
        query_item=Definition(term="acid")
        print(query_item.get())
"""