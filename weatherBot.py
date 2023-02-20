import requests, json, math, discord

token = "Discord Token"
api_key = "API Key from OpenWeatherMap"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def weatherPrinter(city_name):
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                z = x["weather"]
                weather_description = z[0]["description"]
                output = ("Current conditions in " + city_name + ",\nTemperature           : " + str(math.ceil((((current_temperature - 273.15) * 9)/5) + 32)) + " F" + "\nCurrent Conditions: " + str(' '.join(elem.capitalize() for elem in weather_description.split())))
                return output
        else:
                return "City name not found"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith("!"):
        city = message.content
        city = city[1 : ]
        myOut = weatherPrinter(city)
        await message.channel.send(myOut)

client.run(token)
