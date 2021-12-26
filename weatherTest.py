import requests, json, math

api_key = "524091aadf92df586bfe941f3a1c9ffa"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

	y = x["main"]

	current_temperature = y["temp"]

	z = x["weather"]

	weather_description = z[0]["description"]

	print("Temperature: " + str(math.ceil((((current_temperature - 273.15) * 9)/5) + 32)) + " F" + "\nCurrent Conditions: " + str(' '.join(elem.capitalize() for elem in weather_description.split())))

else:
	print(" City Not Found ")
