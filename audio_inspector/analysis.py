"""
analysis.py receives audio_signal and audio_sample_rate from loader.py and performs basic audio analysis.

The analysis includes:
a) audio duration
b) global RMS value

The RMS (Root Mean Square) is a measure of the signal's average power. It is computed by squaring all
signal values, calculating their mean, and finally taking the square root of that mean.
"""
from loader import load_audio
import numpy as np
import librosa

def get_audio_duration(audio_signal, audio_sample_rate):
    duration = len(audio_signal) / audio_sample_rate
    return duration

def get_audio_rms(audio_signal):
    rms = librosa.feature.rms(y=audio_signal)
    global_rms = np.mean(rms)
    return global_rms



if __name__ == "__main__":
    audio_path = "C:/Users/juanp/Downloads/Audiocity.wav"
    signal, sample_rate = load_audio(audio_path)
    duration = get_audio_duration(signal, sample_rate)
    print(f"Audio duration: {duration:.2f} seconds")
    rms = get_audio_rms(signal)
    print(f"Global RMS: {rms:.4f}")