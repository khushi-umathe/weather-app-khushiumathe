import streamlit as st 
import requests 
from dotenv import load_dotenv
import os
load_dotenv()



st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #89CFF0,
            #4682B4,
            #191970
        );
    }
    </style>
    """,
    unsafe_allow_html=True
)


API_KEY=os.getenv('WEATHER_API_KEY')

st.set_page_config(page_title='Weather App',page_icon='🌞')

st.title('Weather App 🌞')

st.write('enter the city name and click the button to fetch the weather data ')

city=st.text_input('enter city name')   

if(st.button('fetch weather')):
    response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if(response.status_code==200):
        st.success('weather data fetched successfully')
        data=response.json()
        # print(data)
        
        # Extract Weather Information
        temperature=data['main']['temp']
        humidity=data['main']['humidity']
        wind_speed=data['wind']['speed']
        weather_condition=data['weather'][0]['description']
        name=data['name']
        country=data['sys']['country']

        st.subheader(f'{name},{country}')
        # create 4 columns
        col1,col2=st.columns(2)
        col3,col4=st.columns(2)
        col1.metric('temperature 🌡️',f'{temperature}°C')
        col2.metric('humidity 💦',f'{humidity}%')
        col3.metric('wind speed 🍃',f'{wind_speed}m/s')
        col4.metric('weather condition🌥️',f'{weather_condition}')
    else:
        st.error('city not found')