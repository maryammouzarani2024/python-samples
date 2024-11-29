from importlib import reload

import requests
from selectorlib import Extractor

class TemperatureCalculator:

    """
    Represents the temperature value extracted from timeanddate.com/weather website.
    """
    def __init__(self, city, country):
        self.city=city
        self.country=country

    def get(self):
        #first get the web page
        #we can also add a header to the request to make it more like a normal browser request
        # header is a dictionary of header parameters and is the second argument of the get function

        resp= requests.get(f"https://www.timeanddate.com/weather/{self.country}/{self.city}")
        content=resp.text
        #to extract a specific value from content we need an extractor
        #to build an extractor we need a yaml file that contains the path in the
        #text to the specific value

        e= Extractor.from_yaml_file('temperature.yaml')
        #the xpath can be copied from the browser inspect element interface
        result=e.extract(content)
        #result is a dictionary of the values with paths defined in the yaml file
        temp=result['temp']
        if temp:
            temp=temp.replace("\xa0°C", "")
            print(f"the temprature at {self.city} is currently: {temp}")
            return float(temp)
        else:
            return None
"""
to test the class and avoid running this code when importing the python file
if __name__=="__main__":
    temperature=TemperatureCalculator("berlin", "germany")
    print(temperature.get())
    
"""