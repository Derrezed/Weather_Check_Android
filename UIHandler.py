from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from ApiHandler import ApiHandler
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
import gc
from kivymd.uix import MDAdaptiveWidget
from datetime import date

degree_sign = u"\N{DEGREE SIGN}"
maincity = "Krakow"


class LocalizationManager(FloatLayout, MDAdaptiveWidget):
    actualcity = maincity

    def clicked(self):
        self.city = self.input.text
        self.actualcity2.text = self.city
        objects = gc.get_objects()
        for object in objects:
            if type(object) == FutureWeather:
                object.update(self.city)

        for object2 in objects:
            if type(object2) == DailyWeather:
                object2.update(self.city)


class FutureWeather(FloatLayout, MDAdaptiveWidget):
    apiHandler = ApiHandler(maincity)
    apiHandler.request_5days()

    temp1day = f'{str(round(apiHandler.temp1day - 273))} C{degree_sign}'
    temp1day_data = apiHandler.temp1day_data
    temp1day_weather = apiHandler.temp1day_weather

    temp2day = f'{str(round(apiHandler.temp2day - 273))} C{degree_sign}'
    temp2day_data = apiHandler.temp2day_data
    temp2day_weather = apiHandler.temp2day_weather

    temp3day = f'{str(round(apiHandler.temp3day - 273))} C{degree_sign}'
    temp3day_data = apiHandler.temp3day_data
    temp3day_weather = apiHandler.temp3day_weather

    temp4day = f'{str(round(apiHandler.temp4day - 273))} C{degree_sign}'
    temp4day_data = apiHandler.temp4day_data
    temp4day_weather = apiHandler.temp4day_weather

    temp5day = f'{str(round(apiHandler.temp5day - 273))} C{degree_sign}'
    temp5day_data = apiHandler.temp5day_data
    temp5day_weather = apiHandler.temp5day_weather

    def update(self, city):
        apiHandler = ApiHandler(city)
        apiHandler.request_5days()
        print(city)
        self.label1day.text = f'{str(round(apiHandler.temp1day - 273))} C{degree_sign}'
        self.label1day_data = apiHandler.temp1day_data
        self.label1day_weather = apiHandler.temp1day_weather

        self.label2day.text = f'{str(round(apiHandler.temp2day - 273))} C{degree_sign}'
        self.label2day_data = apiHandler.temp2day_data
        self.label2day_weather = apiHandler.temp2day_weather

        self.label3day.text = f'{str(round(apiHandler.temp3day - 273))} C{degree_sign}'
        self.label3day_data = apiHandler.temp3day_data
        self.label3day_weather = apiHandler.temp3day_weather

        self.label4day.text = f'{str(round(apiHandler.temp4day - 273))} C{degree_sign}'
        self.label4day_data = apiHandler.temp4day_data
        self.label4day_weather = apiHandler.temp4day_weather

        self.label5day.text = f'{str(round(apiHandler.temp5day - 273))} C{degree_sign}'
        self.label5day_data = apiHandler.temp5day_data
        self.label5day_weather = apiHandler.temp5day_weather


class ContentNavigationDrawer(BoxLayout):
    pass


class Tab(FloatLayout, MDTabsBase):
    pass


class DailyWeather(FloatLayout, MDAdaptiveWidget):
    apiHandler = ApiHandler(maincity)
    apiHandler.request_daily()

    temp = f'{str(round(apiHandler.temp - 273))} C{degree_sign}'
    temp_min = f'Min: {str(round(apiHandler.tempMin - 273))} C{degree_sign}'
    temp_max = f'Max: {str(round(apiHandler.tempMax - 273))} C{degree_sign}'
    cityName = maincity
    today = str(date.today())
    weather_description = apiHandler.weatherDescription

    def update(self, city):
        apiHandler = ApiHandler(city)
        apiHandler.request_daily()
        print(city)
        self.labeltemp.text = f'{str(round(apiHandler.temp - 273))} C{degree_sign}'
        self.labeltemp_min.text = f'Min: {str(round(apiHandler.tempMin - 273))} C{degree_sign}'
        self.labeltemp_max.text = f'Max: {str(round(apiHandler.tempMax - 273))} C{degree_sign}'
        self.labelcityName.text = city


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
