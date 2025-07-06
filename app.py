import openai
import speech_recognition as sr
import pyttsx3
import streamlit as st
import threading
import base64

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Set your OpenAI API key
openai.api_key = 'secret-key'  # Replace with your actual OpenAI API key

# Supported languages for transcription and TTS
supported_languages = {
    "English": "en",
    "Malayalam": "ml"
}

def transcribe_audio_to_text(language_code):
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=language_code)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            st.write("Sorry, the service is down.")
            return ""

def generate_gpt_response(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",  # or "gpt-4" if you have access
        messages=messages
    )
    return response['choices'][0]['message']['content'].strip()

def speak_text(text):
    def run():
        tts_engine.say(text)
        tts_engine.runAndWait()
    # Ensure each speech runs in a new thread
    threading.Thread(target=run).start()

def download_link(object_to_download, download_filename, download_link_text):
    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

def main():
    st.title("Voice Powered ChatBot🤖")

    # Custom CSS for background image
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://wallpapers.com/images/high/sacramento-green-plain-color-whzworfhwbm50ehr.webp");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True  
    )

    # Initialize session state for conversation history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Customize TTS settings
    st.sidebar.write("### TTS Settings")
    volume = st.sidebar.slider("Volume", 0.0, 1.0, 0.7)
    tts_engine.setProperty('volume', volume)

    # Language selection
    st.sidebar.write("### Language Settings")
    language = st.sidebar.selectbox("Select Language", list(supported_languages.keys()))
    language_code = supported_languages[language]

    if st.button("Start Listening"):
        prompt = transcribe_audio_to_text(language_code)
        if prompt:
            response = generate_gpt_response(prompt)
            st.write(f"GPT-4 says: {response}")
            # Update session history
            st.session_state.history.append({"user": prompt, "bot": response})
            speak_text(response)  # Ensure the AI speaks the response

    if st.button("Clear History"):
        st.session_state.history = []

    # Display conversation history in the sidebar
    st.sidebar.write("### Conversation History")
    for i, entry in enumerate(st.session_state.history):
        st.sidebar.write(f"*You:* {entry['user']}")
        st.sidebar.write(f"*GPT-4:* {entry['bot']}")

    # Download conversation history
    if st.sidebar.button("Download History"):
        history_text = "\n\n".join([f"You: {entry['user']}\nGPT-4: {entry['bot']}" for entry in st.session_state.history])
        st.sidebar.markdown(download_link(history_text, "conversation_history.txt", "Download History"), unsafe_allow_html=True)

if __name__ == "__main__":
    main()