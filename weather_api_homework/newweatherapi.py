#1. I am choosing Tommorow over Open Meto because I like how I can find data separetly for "Realtime Weather," "Weather Forecast," and "Weather Recent History." The Open Meto also has it seprately but I didn't like how they categorized it. 
#2. The url for this documentation is 'https://api.tomorrow.io/v4/weather/forecast?location=new%20york&apikey=kLyyt3sPWY6ERem3QAVEBwWGy1jS3BiR'

import os 
from dotenv import load_dotenv

load_dotenv() 

API_key= os.getenv("API_key")

load_dotenv()  # take environment variables


#Tommorow does the import requests a little differently than the other WeatherAPI website! 
import requests

url = f"https://api.tomorrow.io/v4/weather/forecast?location=new%20york&apikey=kLyyt3sPWY6ERem3QAVEBwWGy1jS3BiR={API_key}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

#4. Print out the country this location is in.

data.keys()