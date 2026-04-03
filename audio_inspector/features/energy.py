"""
Energy feature extraction.

Provides frame energy and smoothed energy envelopes.
"""
from __future__ import annotations
import numpy as np


def frame_energy(frames: np.ndarray) -> np.ndarray:
    """
    Compute frame energy.

    Parameters
    ----------
    frames : np.ndarray
        Framed signal.

    Returns
    -------
    np.ndarray
        Energy per frame.
    """

    return np.sum(frames**2, axis=0)


def smooth_energy(
    energy: np.ndarray,
    window: int = 10
) -> np.ndarray:
    """
    Smooth energy curve.

    Parameters
    ----------
    energy : np.ndarray
        Frame energy.

    window : int
        Smoothing window size.

    Returns
    -------
    np.ndarray
        Smoothed energy.
    """

    kernel = np.ones(window) / window

    return np.convolve(
        energy,
        kernel,
        mode="same"
    )