import requests

def kelvin_to_fahrenheit(kelvin_temp):
    fahrenheit = round((kelvin_temp - 273.15) * 9/5 + 32)
    return fahrenheit

# Define api-key and city
api_key = "e1e16445330cb681259519293a01ea58"
city    = "Austin"

# Weather API url
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key

## Send GET request to the weather API
response = requests.get(url)


#Gather city name, temperature, weather description, and wind speed
if response.status_code == 200: # Check if the request was successful
    data = response.json() # Parse the JSON response

    city = data.get("name", "key not found")

    current_temp = kelvin_to_fahrenheit(data.get("main", {}).get("temp", "Key not found"))
    temp_min   = kelvin_to_fahrenheit(data.get("main", {}).get("temp_min", "Key not found"))
    temp_max   = kelvin_to_fahrenheit(data.get("main", {}).get("temp_max", "Key not found"))
    
    description = data.get("weather", [{}])[0].get("description", "Key not found") 
    wind_speed = round(data.get("wind", {}).get("speed", "Key not found"))   
    
    print(f"Greetings! Currently in {city} it is {current_temp} degrees and {description}")
    print(f"Today, the forecast will be a high of {temp_max} and a low of {temp_min} with a wind speed of {wind_speed} miles per hour")
else:
    if response.status_code == 400:
        print("Bad Request")
    elif response.status_code == 401:
        print("Unauthorized access: Invalid API key.")
    elif response.status_code == 404:
        print("City not found. Please check the city name.")
    elif response.status_code == 429:
        print("Too Many requests Try again later.")
    else:
        print(f"Failed to fetch data")