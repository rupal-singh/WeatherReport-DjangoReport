from datetime import datetime

import requests
from django.shortcuts import render
from geopy.geocoders import Nominatim

from weatherapp.models import WeatherReport

# Create your views here.
url = "https://api.weather.gov/points/"
geolocator = Nominatim(user_agent="geoapiExercises")


# render index.html webpage
def index(request):
    if request.method == "POST":     # if post
        try:
            lati = request.POST.get('lati')         # get latitude
            longi = request.POST.get('longi')       # get longitude
            weather_data = requests.get(f'{url}{lati},{longi}').json()  # get json data of specific location
            forecast = requests.get(weather_data['properties']["forecast"]).json()  # get weather forecast data of the location
            location = geolocator.reverse(lati + "," + longi)   # get name of the location using latitude and longitude
            temp = forecast["properties"]['periods'][0]['temperature']  # get temperature
            unit = forecast["properties"]['periods'][0]['temperatureUnit']  # get unit of temperature
            windSpeed = forecast["properties"]['periods'][0]['windSpeed']   # get wind speed
            direction = forecast["properties"]['periods'][0]['windDirection']   # get direction of wind
            desc = forecast["properties"]['periods'][0]['detailedForecast'] # get small summary
            con = WeatherReport(city_name=location, latitude=lati, longitude=longi, temperature=temp,
                                date_of_entry=datetime.today()) # commit to database
            con.save()
            context = {
                'city': location,
                'temp': f"{temp} {unit}",
                'windSpeed': windSpeed,
                'direction': direction,
                'desc': desc
            }
            return render(request, "index.html", context)   # render index.html with weather info
        except Exception as e:      # if data not found then except the Exception
            context = {
                'Error': "Data not found"
            }
            return render(request, "index.html", context)

    return render(request, 'index.html')    # render index.html page
