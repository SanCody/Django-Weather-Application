from django.shortcuts import render
import requests

# Create your views here.
def home(req):
    # print(req.POST)

    city = req.POST['city'] if req.POST.get('city') else 'chennai'

    key = '1f3cefdddb282fd103870aadcb9a4f9a'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}';
    
    w = requests.get(url).json()
    
    weather = {
        'city' : city,
        'temperature' : w['main']['temp'],
        'description' : w['weather'][0]['description'],
        'icon' : w['weather'][0]['icon'],
        'wind_speed': w['wind']['speed'],
        'humidity': w['main']['humidity'],
    }


    return render(req,'index.html', {'weather':weather})