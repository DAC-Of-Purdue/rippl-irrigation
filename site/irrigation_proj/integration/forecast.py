import requests
import datetime

# Replace with your OpenWeatherMap API key
API_KEY = '4658759a600288c8b0ae3e48cab0d38c'

# Define the endpoint for the One Call API
BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall'

# Function to get weather forecast data
def get_weather_forecast(lat, lon):
    # Define parameters
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'imperial',  # Use 'imperial' for Fahrenheit
        'exclude': 'minutely,hourly'  # Exclude minutely and hourly data if not needed
    }
    
    # Make a GET request to the OpenWeatherMap API
    response = requests.get(BASE_URL, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        return data
    else:
        # Print the error message
        print(f"Error: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# Function to print the weather forecast
def print_weather_forecast(forecast_data):
    weatherForecastSet = []
    if forecast_data:
        for day in forecast_data['daily'][:4]:  # Limit to 4 days
            dt = day['dt']
            date = datetime.datetime.fromtimestamp(dt).strftime('%m/%d/%Y')
            temp_day = day['temp']['day']
            weather_description = day['weather'][0]['description']
            precipitation = day.get('rain', 0)  # Get precipitation if available, otherwise 0
            wind_speed = day['wind_speed']
            print(f"Date: {date}, Temperature: {temp_day}°F, Weather: {weather_description}, Precipitation: {precipitation} mm, Wind Speed: {wind_speed} mph")
            dayForecast = {"date":date, "temp":temp_day, "weather":weather_description}
            weatherForecastSet.append(dayForecast)
        return weatherForecastSet
    else:
        print("No data to display.")
# Coordinates for the two field locations
field_locations = [
    {'name': 'Field 1', 'lat': 32.3962427, 'lon': -85.762204},  # Example coordinates
    #{'name': 'Field 2', 'lat': 32.4036418, 'lon': -86.8916694}  # Example coordinates
]

for field in field_locations:
    print(f"\nGetting weather forecast for {field['name']} (Lat: {field['lat']}, Lon: {field['lon']}):")
    forecast_data = get_weather_forecast(field['lat'], field['lon'])

def integratedFunction():
    return print_weather_forecast(forecast_data)


print(integratedFunction())