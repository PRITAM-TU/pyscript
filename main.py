from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Mock API key - in a real app, use a real API key from a weather service
API_KEY = "8173cb99d432bf6d17f4ceeffd8342ca"

# Mock weather data generator
def generate_weather_data(location):
    # In a real app, you would call a weather API here
    # This is just for demonstration purposes
    
    base_temp = random.randint(15, 30)
    conditions = ["Sunny", "Cloudy", "Rainy", "Thunderstorm", "Partly Cloudy"]
    condition = random.choice(conditions)
    
    weather_data = {
        "location": location,
        "temperature": base_temp,
        "description": condition,
        "humidity": f"{random.randint(40, 90)}%",
        "wind": f"{random.randint(5, 25)} km/h",
        "pressure": f"{random.randint(990, 1030)} hPa",
        "visibility": f"{random.randint(5, 15)} km",
        "forecast": []
    }
    
    # Generate 5-day forecast
    for i in range(1, 6):
        day_temp = base_temp + random.randint(-3, 3)
        night_temp = day_temp - random.randint(5, 10)
        day_condition = random.choice(conditions)
        
        # Determine icon based on condition
        icon_map = {
            "Sunny": "sun",
            "Cloudy": "cloud",
            "Rainy": "cloud-rain",
            "Thunderstorm": "bolt",
            "Partly Cloudy": "cloud-sun"
        }
        
        weather_data["forecast"].append({
            "day": (datetime.now() + timedelta(days=i)).strftime("%a"),
            "icon": icon_map.get(day_condition, "sun"),
            "high": day_temp,
            "low": night_temp,
            "desc": day_condition
        })
    
    return weather_data

@app.route('/api/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location', 'New York')
    data = generate_weather_data(location)
    return jsonify(data)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)