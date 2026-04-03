"""
Basic audio analysis functions.

Provides fundamental DSP measurements such as RMS,
peak level and crest factor.
"""
from __future__ import annotations
import numpy as np


def get_audio_duration(
    signal: np.ndarray,
    sample_rate: int
) -> float:
    """
    Compute audio duration.

    Parameters
    ----------
    signal : np.ndarray
        Audio signal.

    sample_rate : int
        Sampling rate.

    Returns
    -------
    float
        Duration in seconds.
    """

    return len(signal) / sample_rate


def get_audio_rms(signal: np.ndarray) -> float:
    """
    Compute RMS level.

    Parameters
    ----------
    signal : np.ndarray
        Audio signal.

    Returns
    -------
    float
        RMS value.
    """

    return np.sqrt(np.mean(signal**2))


def get_audio_rms_db(rms: float) -> float:
    """
    Convert RMS to dBFS.

    Parameters
    ----------
    rms : float
        RMS level.

    Returns
    -------
    float
        RMS in decibels.
    """

    return 20 * np.log10(rms)


def get_audio_peak(signal: np.ndarray) -> float:
    """
    Compute peak amplitude.

    Parameters
    ----------
    signal : np.ndarray
        Audio signal.

    Returns
    -------
    float
        Peak amplitude.
    """

    return np.max(np.abs(signal))


def get_audio_crest_factor(
    peak: float,
    rms: float
) -> float:
    """
    Compute crest factor.

    Parameters
    ----------
    peak : float
        Peak level.

    rms : float
        RMS level.

    Returns
    -------
    float
        Crest factor.
    """

    return peak / rms


def get_audio_cf_db(crest_factor: float) -> float:
    """
    Convert crest factor to dB.

    Parameters
    ----------
    crest_factor : float
        Crest factor.

    Returns
    -------
    float
        Crest factor in decibels.
    """

    return 20 * np.log10(crest_factor)