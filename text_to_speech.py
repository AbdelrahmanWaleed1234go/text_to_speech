from streamlit import *
from gtts import gTTS





write("Welcome in text to speech app")

t=text_input("Enter your text")

if button("genrate"):
   gTTS(t)


    
