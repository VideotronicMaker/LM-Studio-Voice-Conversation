# Step 1: Import necessary libraries and modules
import warnings
import pyaudio
import wave
import whisper
import openai
import keyboard
import os
import pyttsx3
import tkinter as tk
from tkinter import simpledialog

# Step 2: Initialize Text-to-Speech engine (Windows users only)
engine = pyttsx3.init()
hazel_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
engine.setProperty('voice', hazel_voice_id)
engine.say("Hello Videotronic Maker, How can I assist you today sir?")
engine.runAndWait()

# Step 3: Define ANSI escape sequences for text color
colors = {
    "blue": "\033[94m",
    "bright_blue": "\033[96m",
    "orange": "\033[93m",
    "yellow": "\033[93m",
    "white": "\033[97m",
    "red": "\033[91m",
    "magenta": "\033[35m",
    "bright_magenta": "\033[95m",
    "cyan": "\033[36m",
    "bright_cyan": "\033[96m",
    "green": "\033[32m",
    "bright_green": "\033[92m",
    "reset": "\033[0m"
}

# Step 4: Ignore FP16 warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

# Step 5: Point to LM Studio Local Inference Server
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

# Step 6: Load the Whisper model
whisper_model = whisper.load_model("tiny")  # orig=base

# Step 7: Define audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000  # orig = 16000
CHUNK = 1024
audio = pyaudio.PyAudio()

# Step 8: Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Step 9: Define function to record audio
def record_audio():
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print(f"{colors['green']}Start speaking... (Press 'N' to stop){colors['reset']}")
    frames = []

    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('n'):
            print(f"{colors['red']}Stopping recording.{colors['reset']}")
            break

    stream.stop_stream()
    stream.close()

    wf = wave.open("temp_audio.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return "temp_audio.wav"

# Step 10: Define function to get user input via GUI dialog
def get_user_input():
    ROOT = tk.Tk()
    ROOT.withdraw()  # Hide the main Tkinter window
    user_input = simpledialog.askstring(title="Text Input", prompt="Type your input:")
    return user_input

# Step 11: Define function to process user input and generate response
def process_input(input_text):
    conversation = [
        {"role": "system", "content": "You are KITT, the assistant chatbot. My name is VideotronicMaker, the human and user. Your role is to assist the human, who is known as VideotronicMaker. Respond concisely and accurately, maintaining a friendly, respectful, and professional tone. Emphasize honesty, candor, and precision in your responses."},
        {"role": "user", "content": input_text}
    ]

    completion = openai.ChatCompletion.create(
        model="local-model",
        messages=conversation,
        temperature=0.7,
        top_p=0.9,  
        top_k=40    
    )

    assistant_reply = completion.choices[0].message.content
    print(f"{colors['magenta']}KITT:{colors['reset']} {assistant_reply}")
    speak(assistant_reply)

# Step 12: Main loop to continuously monitor for user input
print(f"{colors['yellow']}Ready to record. (Press 'B' to start, 'M' to type){colors['reset']}")
while True:
    try:
        if keyboard.is_pressed('b'):  # Start recording when 'B' is pressed
            audio_file = record_audio()
            transcribe_result = whisper_model.transcribe(audio_file)
            transcribed_text = transcribe_result["text"]
            print(f"{colors['blue']}VTM:{colors['reset']} {transcribed_text}")
            process_input(transcribed_text)
            os.remove(audio_file)  # Cleanup

        elif keyboard.is_pressed('m'):  # Use the GUI for input when 'M' is pressed
            typed_input = get_user_input()
            if typed_input:  # Ensure input is not None or empty
                print(f"{colors['blue']}VTM typed:{colors['reset']} {typed_input}")  # Print the typed input in the terminal
                process_input(typed_input)

    except KeyboardInterrupt:
        print("\nExiting...")
        break  # Correctly placed to exit the loop upon a KeyboardInterrupt

# Step 13: Cleanup audio resources
audio.terminate()
