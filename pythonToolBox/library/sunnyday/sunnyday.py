
import requests


class Weather:
    """ Creates a Weather object letting an apikey as input and the lat and
    lon of a location.
    package use example:
    >> weather1= Weather(apikey="2345678900987654", lat=42, lon=43)

    #Get complete weather data for the next 12 hours:

    >> weather1.next_12h()
    #simplified data for the next 12 hours:
    >> weather1.next_12h_simplified()
    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        if lat and lon:
            url=f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r=requests.get(url)
            self.data=r.json()
        else:
            raise TypeError("provide valid lat and lon arguments")
        # if self.data['cod']!=200:
        #     raise  ValueError(self.data['message'])
    def next_12h(self):
            """Get complete weather data for the next 12 hours:
            """
            return self.data['list'][:4]

    def next_12h_simplified(self):
        """Returns the 3-hour data for the next 12 hours as a dict.

        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'],
                dicty['weather'][0]['description']))
        return  simple_data
