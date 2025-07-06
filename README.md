# 🎙️ Voice-Powered Chatbot

A real-time **speech-based chatbot** that listens to user queries, processes them using **OpenAI GPT-4-turbo**, and responds using **Text-to-Speech (TTS)**. Built with **Streamlit**, this application enhances accessibility and interaction, supporting multiple languages like **English** and **Malayalam**.

---

## 🧠 Features

- 🗣️ **Speech-to-Text** using `speech_recognition` with Google API
- 🧾 **Conversational Responses** from **GPT-4-turbo**
- 🔊 **Text-to-Speech (TTS)** using `pyttsx3` with adjustable volume
- 🌐 **Multilingual Support**: English and Malayalam
- 💬 **Conversation History** with optional download
- 💡 **Threaded TTS** to keep UI responsive
- 🎛️ **Streamlit UI** with real-time controls and settings

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – for frontend UI
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) – for speech-to-text
- [pyttsx3](https://pypi.org/project/pyttsx3/) – for text-to-speech
- [OpenAI API](https://platform.openai.com/) – for GPT-4-turbo responses
- Python threading – for asynchronous TTS

---

## 🚀 How It Works

1. **User clicks "Start Listening"**
2. Voice is captured via mic → transcribed with Google Speech Recognition
3. Transcription sent to **GPT-4-turbo** → response generated
4. Response shown on screen + spoken aloud using **pyttsx3**
5. Interaction is saved in **session-based history**, viewable and downloadable

---


![UI Preview](https://wallpapers.com/images/high/sacramento-green-plain-color-whzworfhwbm50ehr.webp)

---

## 📂 Project Structure

