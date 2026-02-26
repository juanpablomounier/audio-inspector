"""This script loads a valid audio file.
The audio file's path is saved in the 'audio' variable.
The audio is loaded as mono and it's amplitud is normalized (-1 to +1).
The function returns both audio signal and sample rate.
"""
import librosa
def load_audio(audio_path):
    #Load audio file as mono waveform and sampling rate
    audio_signal, audio_sample_rate = librosa.load(audio_path, mono=True)
    return audio_signal, audio_sample_rate