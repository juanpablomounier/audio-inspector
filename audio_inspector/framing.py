"""
framing.py generates time windows by dividing an audio signal into several frames.
"""
import numpy as np
from validation import validate_sample_rate, validate_signal

def frame_signal(audio_signal, sample_rate, window_size_ms=50, hop_size_ms=25):
    window_size_samples = int(sample_rate * window_size_ms / 1000)
    hop_size_samples    = int(sample_rate * hop_size_ms / 1000)
    frames = []
    times = []
    validate_signal(audio_signal)
    validate_sample_rate(sample_rate)

    for start in range(0, len(audio_signal)-window_size_samples+1, hop_size_samples):
        frame = audio_signal[start : start + window_size_samples]
        time = start / sample_rate
        frames.append(frame)
        times.append(time)

    return np.array(frames), np.array(times)
