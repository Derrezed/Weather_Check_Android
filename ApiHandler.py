import requests


class ApiHandler:
    def __init__(self, city):
        self.city = city
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid=d55e4671a5b45e80f03b70a550d7bcde"
        self.url5days = f"http://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid=d55e4671a5b45e80f03b70a550d7bcde"

    def request_daily(self):
        self.json_data = requests.get(self.url).json()
        self.temp = self.json_data['main']['temp']
        self.tempMin = self.json_data['main']['temp_min']
        self.tempMax = self.json_data['main']['temp_max']
        self.weatherDescription = self.json_data['weather'][0]['main']

    def request_5days(self):
        self.json_data = requests.get(self.url5days).json()

        self.temp1day = self.json_data['list'][0]['main']['temp']
        self.temp1day_data = self.json_data['list'][0]['dt_txt']
        self.temp1day_weather = self.json_data['list'][0]['weather'][0]['main']

        self.temp2day = self.json_data['list'][8]['main']['temp']
        self.temp2day_data = self.json_data['list'][8]['dt_txt']
        self.temp2day_weather = self.json_data['list'][8]['weather'][0]['main']

        self.temp3day = self.json_data['list'][16]['main']['temp']
        self.temp3day_data = self.json_data['list'][16]['dt_txt']
        self.temp3day_weather = self.json_data['list'][16]['weather'][0]['main']

        self.temp4day = self.json_data['list'][24]['main']['temp']
        self.temp4day_data = self.json_data['list'][24]['dt_txt']
        self.temp4day_weather = self.json_data['list'][24]['weather'][0]['main']

        self.temp5day = self.json_data['list'][32]['main']['temp']
        self.temp5day_data = self.json_data['list'][32]['dt_txt']
        self.temp5day_weather = self.json_data['list'][32]['weather'][0]['main']


