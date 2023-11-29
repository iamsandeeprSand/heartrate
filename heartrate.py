import streamlit as st
import requests
import time

# Function to fetch heart rate
def fetch_heart_rate():
    url = 'https://dev.pulsoid.net/api/v1/data/heart_rate/latest?response_mode=text_plain_only_heart_rate'
    header = {"Authorization": "Bearer 0aad8548-0c7c-46c7-9519-0eba804655c9"}

    try:
        response_API = requests.get(url=url, headers=header)
        if response_API.status_code == 200:
            return int(response_API.text)
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

# Streamlit UI
st.title("Heart Rate App")

# Load and play the sound
sound_file = r'C:\Users\Administrator\Downloads\mixkit-repeating-arcade-beep-1084.wav'  # Update this with your sound file path

if st.button("Evaluate Heart Rate"):
    for i in range(100):  # Consider changing this loop for a more responsive user experience
        heart_rate = fetch_heart_rate()
        if heart_rate is not None:
            st.write(f"Current Heart Rate: {heart_rate}")
            if heart_rate <= 60:
                st.text("Heart Rate Low, emotionally unstable")
                # Here, instead of playing sound, consider using Streamlit's audio functionality
                st.audio(sound_file, format='audio/wav')
            elif heart_rate >= 95:
                st.text("Heart Rate High, emotionally unstable")
                # Same as above, consider Streamlit's audio functionality for sound
            else:
                st.text("Heart Rate normal, emotionally stable")
        time.sleep(1)  # Consider adjusting this for responsiveness
