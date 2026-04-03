"""
Temporal feature extraction.

Provides novelty detection functions.
"""
from __future__ import annotations
import numpy as np


def temporal_novelty(
    energy: np.ndarray
) -> np.ndarray:
    """
    Compute novelty curve.

    Parameters
    ----------
    energy : np.ndarray
        Smoothed energy envelope.

    Returns
    -------
    np.ndarray
        Novelty function.
    """

    novelty = np.diff(energy)

    novelty = np.maximum(
        novelty,
        0
    )

    return np.concatenate(
        ([0], novelty)
    )


def normalize_novelty(
    novelty: np.ndarray
) -> np.ndarray:
    """
    Normalize novelty curve.

    Parameters
    ----------
    novelty : np.ndarray
        Novelty function.

    Returns
    -------
    np.ndarray
        Normalized novelty.
    """

    max_val = np.max(novelty)

    if max_val == 0:

        return novelty

    return novelty / max_val