"""
Visualization utilities.

Provides plotting functions for extracted features.
"""
from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt


def plot_energy(
    times: np.ndarray,
    energy: np.ndarray
) -> None:
    """
    Plot frame energy.

    Parameters
    ----------
    times : np.ndarray
        Time axis.

    energy : np.ndarray
        Frame energy.
    """

    if not isinstance(energy, np.ndarray):

        raise ValueError(
            "Energy must be numpy array."
        )

    plt.figure()

    plt.plot(times, energy)

    plt.title("Frame Energy")

    plt.xlabel("Time (s)")

    plt.ylabel("Energy")

    plt.tight_layout()

    plt.show()


def plot_smooth_energy(
    times: np.ndarray,
    energy: np.ndarray
) -> None:
    """
    Plot smoothed energy.

    Parameters
    ----------
    times : np.ndarray
        Time axis.

    energy : np.ndarray
        Smoothed energy.
    """

    plt.figure()

    plt.plot(times, energy)

    plt.title("Smoothed Energy")

    plt.xlabel("Time (s)")

    plt.ylabel("Energy")

    plt.tight_layout()

    plt.show()


def plot_novelty(
    times: np.ndarray,
    novelty: np.ndarray
) -> None:
    """
    Plot novelty function.

    Parameters
    ----------
    times : np.ndarray
        Time axis.

    novelty : np.ndarray
        Novelty curve.
    """

    if not isinstance(novelty, np.ndarray):

        raise ValueError(
            "Novelty must be numpy array."
        )

    plt.figure()

    plt.plot(times, novelty)

    plt.title("Novelty")

    plt.xlabel("Time (s)")

    plt.ylabel("Novelty")

    plt.tight_layout()

    plt.show()