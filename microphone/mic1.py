import ipywidgets as widgets
from IPython.display import display
from queue import Queue
from threading import Thread
import streamlit as st

messages = Queue()
recordings = Queue()


output = widgets.Output()


def start_recording(data):
    messages.put(True)
    with output:
        display("Starting...")
        record = Thread(target=record_microphone)
        record.start()
        transcribe = Thread(target=speech_recognition, args=(output,))
        transcribe.start()


def stop_recording(data):
    with output:
        messages.get()
        display("Stopped.")


st.button('Start Recording', on_click=start_recording)
st.button('Stop Recording', on_click=stop_recording)


# Find audio device index using this code
import pyaudio

CHANNELS = 1
FRAME_RATE = 16000
RECORD_SECONDS = 20
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2


def record_microphone(chunk=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=FRAME_RATE,
                    input=True,
                    input_device_index=1,
                    frames_per_buffer=chunk)

    frames = []

    while not messages.empty():
        data = stream.read(chunk)
        frames.append(data)
        if len(frames) >= (FRAME_RATE * RECORD_SECONDS) / chunk:
            recordings.put(frames.copy())
            frames = []

    stream.stop_stream()
    stream.close()
    p.terminate()


API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
headers = {"Authorization": "Bearer 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"}


def query(frames):
    import requests
    with open(frames, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


def speech_recognition():
    import json
    while not messages.empty():
        frames = recordings.get()
        output = query(frames)
        output = json.dumps(output).replace('[UNK]', ' ')
        return output
