"""
Signal validation utilities.

This module ensures that audio data conforms to expected
types and constraints before analysis.
"""
from __future__ import annotations
import numpy as np


def validate_signal(signal: np.ndarray) -> None:
    """
    Validate audio signal.

    Parameters
    ----------
    signal : np.ndarray
        Audio signal.

    Raises
    ------
    TypeError
        If signal is not numpy array.

    ValueError
        If signal is empty.
    """

    if not isinstance(signal, np.ndarray):

        raise TypeError("Signal must be numpy array.")

    if signal.size == 0:

        raise ValueError("Signal cannot be empty.")


def validate_sample_rate(sample_rate: int) -> None:
    """
    Validate sample rate.

    Parameters
    ----------
    sample_rate : int
        Audio sampling rate.

    Raises
    ------
    ValueError
        If sample rate is invalid.
    """

    if sample_rate <= 0:

        raise ValueError("Sample rate must be positive.")