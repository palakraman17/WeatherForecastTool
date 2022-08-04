from flask import Flask, request, render_template
import string
from controller import ForecastController

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def main():
    if request.method == "POST": 
        data = request.json
        latitude = data['latitude']
        longitude = data['longitude']

        checkTimePeriod = data['time']
        checkTimePeriodCaps = string.capwords(checkTimePeriod)

        forecast = ForecastController()

        pointResponse = forecast.getPointMetadata(latitude, longitude)
        if pointResponse == None:
            return render_template('page.html', latitude = latitude, longitude = longitude)

        city = pointResponse['properties']['relativeLocation']['properties']['city']
        state = pointResponse['properties']['relativeLocation']['properties']['state']

        forecastURL = pointResponse['properties']['forecast']
        forecastResponse = forecast.getForecastData(forecastURL)
        availableForecast = forecastResponse['properties']['periods']
        forecastList = forecast.getForecastPeriodList(availableForecast)

        timePeriod = []
       
        if checkTimePeriodCaps in forecastList:
            for record in range(len(availableForecast)):
                if checkTimePeriodCaps == availableForecast[record]['name']:
                    timePeriod.append(availableForecast[record])
                    return render_template('report.html', city = city, state = state, periodList = timePeriod)  
        else:
            return render_template('page.html', city = city, state = state, time = checkTimePeriod)
    else:   
       return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')   

    

