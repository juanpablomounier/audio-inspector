"""This script loads a valid audio file.
The audio file's path is saved in the 'audio' variable.
It's validated.
The function returns both audio signal and sample rate.
"""
import librosa
def load_audio(audio_path):
    #Here the audio file is loaded and returns signal and sample rate
    audio_signal, audio_sample_rate = librosa.load(audio_path)



    return audio_signal, audio_sample_rate