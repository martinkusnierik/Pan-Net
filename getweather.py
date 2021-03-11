# import statements
import pyowm
import os

# get environment variables from the CLI
API_KEY=os.environ.get('OPENWEATHER_API_KEY')
CITY_NAME=os.environ.get('CITY_NAME')

if __name__=='__main__':
    try:
        my_weather=pyowm.OWM(API_KEY)

    except:
        print("Check your API KEY")
        exit(1)

    mgr = my_weather.weather_manager()
    observation = mgr.weather_at_place(CITY_NAME)  # the observation object is a box containing a weather object
    weather = observation.weather
    temperature = weather.temperature("celsius")

    print("source=openweathermap," + " city=" + CITY_NAME + "," " description=" + weather.detailed_status + "," +
    " temp=" + str(temperature['temp']) + "," + " humidity=" + str(weather.humidity) )
