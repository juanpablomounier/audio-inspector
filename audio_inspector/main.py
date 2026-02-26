"""
This audio analyzer takes an audio file in wav/mp3 format and analyses several features of it.
"""

from core.loader import load_audio
from core.validation import validate_signal, validate_sample_rate
from core.analysis import get_audio_duration, get_audio_rms, get_audio_rms_db, get_audio_peak, get_audio_crest_factor, get_audio_cf_db
from core.framing import frame_signal
from features.energy import frame_energy, smooth_energy
from visualization.plotting import plot_energy, plot_smooth_energy

audio_path = "C:/Users/juanp/Downloads/Audiocity.wav"

signal, sample_rate = load_audio(audio_path)
valid_signal = validate_signal(signal)
valid_sample_rate = validate_sample_rate(sample_rate)
audio_duration = get_audio_duration(signal, sample_rate)
audio_rms = get_audio_rms(signal)
audio_dbfs = get_audio_rms_db(audio_rms)
audio_peak = get_audio_peak(signal)
audio_crest_factor = get_audio_crest_factor(audio_peak, audio_rms)
audio_cf_db = get_audio_cf_db(audio_crest_factor)
frames, times = frame_signal(signal, sample_rate)
energy = frame_energy(frames)
smoothed_energy = smooth_energy(energy)


print(f"""For the file {audio_path} 
    the duration is {audio_duration},
    the RMS level is {audio_rms}, the RMS in dB is {audio_dbfs},
    the peak is {audio_peak},
    the linear crest factor is {audio_crest_factor}
    and the CF in dB is {audio_cf_db}.
    Energy shape is {energy}.
    Smoothed energy is {smoothed_energy}\n""")

plot_energy(times, energy)
plot_smooth_energy(times, smoothed_energy)

print(frames.shape)
print(times[0], times[-1])