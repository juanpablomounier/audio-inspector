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

def get_audio_rms_db(global_rms):
    """ 
    Converts a linear RMS value (0–1) into decibels relative to full scale (dBFS).
    Raises ValueError if RMS is non-positive.
    """

    if isinstance(global_rms,(int,float, np.floating)) and global_rms > 0:
        rms_db = 20 * np.log10(global_rms)
    else:
        raise ValueError("Global RMS variable is not number type or is not above 0.")
    return rms_db


def get_audio_peak(audio_signal):
    """
    Assuming a valid signal, it computes absolute amplitude peak in range [0,1]. Float value returned.
    """
    peak = np.max(np.abs(audio_signal))
    return peak

def get_audio_crest_factor(peak, global_rms):
    """
    After basic validation, it computes Crest Factor dividing Peak by RMS. Float value returned.
    """
    if global_rms != 0 and peak > global_rms:
        crest_factor = peak/global_rms
    else:
        raise ValueError("RMS must be above 0 and peak must be > RMS.")
    return crest_factor

def get_audio_cf_db(crest_factor):
    """
    Converts a linear Crest Factor value into decibels.
    Raises ValueError if CF is non-positive.
    """
    if crest_factor > 0:
        cf_db = 20 * np.log10(crest_factor)
    else:
        raise ValueError("Crest Factor must be above 0.")
    
    return cf_db