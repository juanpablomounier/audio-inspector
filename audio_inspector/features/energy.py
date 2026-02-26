import numpy as np


def frame_energy(frames):
    """
    Compute energy for each frame.

    Parameters
    ----------
    frames : np.ndarray
        Shape (num_frames, frame_length)

    Returns
    -------
    energy : np.ndarray
        Energy per frame
    """
    # Energía = suma de cuadrados
    energy = np.sum(frames ** 2, axis=1)

    return np.array(energy)

def smooth_energy(energy, hop_size_ms=25, smooth_ms=200):

    if not isinstance(energy, np.ndarray):
        raise ValueError("energy must be a np array.")
    
    windows_frames = int(smooth_ms / hop_size_ms)    
    if windows_frames < 1:
        raise ValueError("windows_frames must be above or equal to 1.")

    kernel = np.ones(windows_frames) / windows_frames
    
    smoothed_energy = np.convolve(energy, kernel, 'same')
    return smoothed_energy
