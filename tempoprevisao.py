from pyowm import owm

owm = pyowm.OWM('sua chave qui')

observation = owm.weather_at_place('Brasília,BR')

w = observation.get_weather()
w.get_wind()
w.get_humidity()
w.get_temperature('celsius')
w
