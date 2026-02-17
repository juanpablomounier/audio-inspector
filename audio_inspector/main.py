"""
This audio analyzer takes an audio file in wav/mp3 format and analyses several features of it.
"""

from loader import load_audio
from validation import validate_signal, validate_sample_rate
from analysis import get_audio_duration, get_audio_rms

audio_path = "C:/Users/juanp/Downloads/Audiocity.wav"

signal, sample_rate = load_audio(audio_path)
valid_signal = validate_signal(signal)
valid_sample_rate = validate_sample_rate(sample_rate)
audio_duration = get_audio_duration(signal, sample_rate)
audio_rms = get_audio_rms(signal)

print(f"For the file {audio_path} the duration is {audio_duration} and the RMS level is {audio_rms}\b")
