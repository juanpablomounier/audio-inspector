"""
Audio loading utilities.

This module provides functions to load audio files into numpy arrays
using librosa as backend.
"""
from __future__ import annotations
import librosa
import numpy as np


def load_audio(audio_path: str) -> tuple[np.ndarray, int]:
    """
    Load an audio file.

    Parameters
    ----------
    audio_path : str
        Path to audio file (wav, mp3, flac).

    Returns
    -------
    tuple[np.ndarray, int]
        Audio signal as numpy array and sample rate.

    Notes
    -----
    Audio is converted to mono automatically.
    """

    audio_signal, audio_sample_rate = librosa.load(
        audio_path,
        mono=True
    )

    return audio_signal, audio_sample_rate