import requests
from flask import request

class ForecastController:

    def makeGetRequest(self, uri):
        response = requests.get(uri)
        if response.status_code != 200:
            return None
        else:
            return response.json()

    def getPointMetadata(self,latitude, longitude):
        if request.method == "POST": 
            apiURL = "https://api.weather.gov/points/" + latitude + "," + longitude
            response = self.makeGetRequest(apiURL)
            return response

    def getForecastData(self, forecastURL):
        response = self.makeGetRequest(forecastURL)
        return response

    def getForecastPeriodList(self, forecastResponse):
        forecastList = []
        for period in forecastResponse:
            forecastList.append(period['name'])
        return forecastList
