import pyowm
from secrets import OWM_TOKEN

owm = pyowm.OWM(OWM_TOKEN)


def get_forecast(place):
	observation = owm.weather_at_place(place)
	weather = observation.get_weather()
	temperature = weather.get_temperature('celsius')["temp"]
	wind = weather.get_wind()['speed']
	clouds = weather.get_clouds()
	humidity = weather.get_humidity()
	forecast = "🏙 In " + place + " is currently " + weather.get_detailed_status() + "\n🌡️  " + str(
		 temperature) + " °C" + "\n💨  " + str(wind) + " m/s" + "\n🌫️  " + str(clouds) + " %" + "\n💦  " + str(
		 humidity) + " %"
	return forecast
