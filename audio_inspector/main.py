"""
This audio analyzer takes an audio file in wav/mp3 format and analyses several features of it.
"""

from loader import load_audio
from validation import validate_signal, validate_sample_rate
from analysis import get_audio_duration, get_audio_rms, get_audio_rms_db, get_audio_peak, get_audio_crest_factor, get_audio_cf_db
from framing import frame_signal

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

print(f"""For the file {audio_path} 
    the duration is {audio_duration},
    the RMS level is {audio_rms}, the RMS in dB is {audio_dbfs},
    the peak is {audio_peak},
    the linear crest factor is {audio_crest_factor}
    and the CF in dB is {audio_cf_db}.\n""")

print(frames.shape)
print(times[0], times[-1])