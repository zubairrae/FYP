import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

# Streamlit app layout
st.title("Text-to-Speech App")
st.write("Enter the text you want to convert to speech:")

# Input text box
text = st.text_area("Text Input")

# File uploader for text file
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    text = st.text_area("Text Input", value=text)

# Convert text to speech
if st.button("Convert to Speech"):
    engine.save_to_file(text, "speech.mp3")
    engine.runAndWait()

    # Read the generated audio file
    audio_file = open("speech.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

    # Create a download link for the audio file
    b64 = base64.b64encode(audio_bytes).decode()
    href = f'<a href="data:file/mp3;base64,{b64}" download="speech.mp3">Download Audio</a>'
    st.markdown(
        f'<div style="text-align:center">{href}</div>',
        unsafe_allow_html=True
    )
