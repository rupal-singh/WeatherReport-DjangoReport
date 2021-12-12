from django.shortcuts import redirect, render
from geopy.geocoders import Nominatim
import requests
from weatherapp.models import WeatherReport
from datetime import datetime

# Create your views here.
url = "https://api.weather.gov/points/"
geolocator = Nominatim(user_agent="geoapiExercises")

def index(request):
    if request.method == "POST":
        try:
            lati = request.POST.get('lati')
            longi = request.POST.get('longi')
            weather_data = requests.get(f'{url}{lati},{longi}').json()
            forecast = requests.get(weather_data['properties']["forecast"]).json()
            location = geolocator.reverse(lati+","+longi)
            temp = forecast["properties"]['periods'][0]['temperature']
            unit = forecast["properties"]['periods'][0]['temperatureUnit']
            windSpeed = forecast["properties"]['periods'][0]['windSpeed']
            direction = forecast["properties"]['periods'][0]['windDirection']
            desc = forecast["properties"]['periods'][0]['detailedForecast']
            con = WeatherReport(city_name=location, latitude=lati, longitude=longi, temperature=temp, date_of_entry=datetime.today())
            con.save()
            context = {
                        'city': location,
                        'temp': f"{temp} {unit}",
                        'windSpeed' : windSpeed,
                        'direction' : direction,
                        'desc' : desc
                    }
            return render(request, "index.html", context)
        except Exception as e:
            context = {
                            'Error' : "Data not found"
                        }
            return render(request, "index.html", context)
    
    return render(request, 'index.html')