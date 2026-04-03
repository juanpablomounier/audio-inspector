"""
Signal framing utilities.

Splits audio into overlapping frames for feature extraction.
"""
from __future__ import annotations
import numpy as np
import librosa


def frame_signal(
    signal: np.ndarray,
    sample_rate: int,
    frame_size: int = 2048,
    hop_size: int = 512
) -> tuple[np.ndarray, np.ndarray]:
    """
    Frame audio signal.

    Parameters
    ----------
    signal : np.ndarray
        Audio signal.

    sample_rate : int
        Sampling rate.

    frame_size : int
        Frame length.

    hop_size : int
        Hop size.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]

        Frames matrix and time vector.
    """

    frames = librosa.util.frame(
        signal,
        frame_length=frame_size,
        hop_length=hop_size
    )

    times = librosa.frames_to_time(
        range(frames.shape[1]),
        sr=sample_rate,
        hop_length=hop_size
    )

    return frames, times