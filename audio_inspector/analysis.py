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
    """
    Computes the duration of an audio signal in seconds.

    Parameters
    ----------
    audio_signal : np.ndarray
        One-dimensional audio signal (mono).
    audio_sample_rate : int or float
        Sampling rate in Hz. Must be a positive value.

    Returns
    -------
    float
        Duration of the audio signal in seconds.

    Raises
    ------
    ValueError
        If the audio signal is empty or the sample rate is not positive.
    """
    if len(audio_signal) == 0:
        raise ValueError("audio_signal is empty.")

    if audio_sample_rate <= 0:
        raise ValueError("audio_sample_rate must be positive.")

    duration = len(audio_signal) / audio_sample_rate
    return duration

def get_audio_rms(audio_signal):
    """
    Computes the global RMS (Root Mean Square) value of an audio signal.

    The RMS is a measure of the signal's average power. It is computed
    by calculating the RMS over short frames and then averaging those
    values to obtain a single global measure.

    Parameters
    ----------
    audio_signal : np.ndarray
        One-dimensional audio signal (mono), normalized between -1 and 1.

    Returns
    -------
    float
        Global RMS value of the audio signal.

    Raises
    ------
    ValueError
        If the audio signal is empty.
    """
    if len(audio_signal) == 0:
        raise ValueError("audio_signal is empty.")

    rms = librosa.feature.rms(y=audio_signal)
    global_rms = np.mean(rms)
    return global_rms



