import requests
from datetime import datetime
import os


APP_ID = os.environ.get("EV-APP-ID")
API_KEY = os.environ.get("EV-API-KEY")
SHEETY_USERNAME = os.environ.get("EV-SHEETY-USERNAME")
SHEETY_PASSWORD = os.environ.get("EV-SHEETY-PASSWORD")
SHEETY_AUHTORIZATION_HEADER = os.environ.get("SHEETY_AUHTORIZATION_HEADER")
print(API_KEY)


excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
excercise_text = input("What exercises did you do?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": excercise_text
}


response = requests.post(url= excercise_endpoint, headers=headers, json=parameters)
response.raise_for_status()
data = response.json()
print(data)
print(data["exercises"])
exercise_type = data["exercises"][0]["user_input"].title()
exercise_duration = data["exercises"][0]["duration_min"]
calories_burnt = data["exercises"][0]["nf_calories"]
print(f"Exercise: {exercise_type}\nDuration: {exercise_duration}\nCalories: {calories_burnt}")

#adding new columns to sheets
endpoint_sheety_URL = os.environ.get("endpoint_sheety_URL")

today = datetime.now()
current_date = f"{today.strftime("%d")}/{today.strftime("%m")}/{today.strftime("%Y")}"
print(f"Current Date: {current_date}")

current_time = f"{today.strftime("%H")}:{today.strftime("%M")}:{today.strftime("%S")}"
print(f"Current time: {current_time}")

values = {
    "workout": {
        "date": current_date,
        "time": current_time,
        "exercise": exercise_type,
        "duration": exercise_duration,
        "calories": calories_burnt,
    }
}


Authorization = (SHEETY_USERNAME, SHEETY_PASSWORD)

response2 = requests.post(url= endpoint_sheety_URL, json= values, auth= Authorization)
response2.raise_for_status()
print(response2.json())

























