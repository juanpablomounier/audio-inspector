"""
validation.py validates audio data before analysis.

Validation includes:
1) Audio signal must be a non-empty array with finite values.
2) Audio sample rate must be int or float and greater than 8000 Hz.
"""
import numpy as np

def validate_signal(audio_signal):
    if not isinstance(audio_signal,np.ndarray):
        raise ValueError("Audio signal must be a numpy array.")
    if audio_signal.size == 0:
        raise ValueError("Audio signal is empty.") 
    if not np.all(np.isfinite(audio_signal)):
        raise ValueError("Audio signal contains non-finite values.")
    return True

def validate_sample_rate(audio_sample_rate):
    if not isinstance(audio_sample_rate,(int,float)):
        raise ValueError("Sample rate must be an int or float.")
    if audio_sample_rate <= 8000:
        raise ValueError("Sample rate must be greater than 8000 Hz.")
    return True