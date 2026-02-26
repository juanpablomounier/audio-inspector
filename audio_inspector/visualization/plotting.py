"""
plotting.py handles visualization of audio features.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_energy(times, energy):
    """
    Plots frame energy over time.

    Parameters
    ----------
    times : np.ndarray
        Time positions of frames (seconds).

    energy : np.ndarray
        Energy value per frame.
    """

    # --- basic validation ---
    if not isinstance(times, np.ndarray):
        raise ValueError("times must be a numpy array.")

    if not isinstance(energy, np.ndarray):
        raise ValueError("energy must be a numpy array.")

    if len(times) != len(energy):
        raise ValueError("times and energy must have same length.")

    # --- plotting ---
    plt.figure(figsize=(10, 4))

    plt.plot(times, energy)

    plt.title("Frame Energy Over Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Energy")

    plt.tight_layout()
    plt.show()

def plot_smooth_energy(times, smoothed_energy):
    """
    Plots frame energy over time.

    Parameters
    ----------
    times : np.ndarray
        Time positions of frames (seconds).

    energy : np.ndarray
        Energy value per frame.
    """

    # --- basic validation ---
    if not isinstance(times, np.ndarray):
        raise ValueError("times must be a numpy array.")

    if not isinstance(smoothed_energy, np.ndarray):
        raise ValueError("energy must be a numpy array.")

    if len(times) != len(smoothed_energy):
        raise ValueError("times and energy must have same length.")

    # --- plotting ---
    plt.figure(figsize=(10, 4))

    plt.plot(times, smoothed_energy)

    plt.title("Frame Energy Over Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Smoothed energy")

    plt.tight_layout()
    plt.show()