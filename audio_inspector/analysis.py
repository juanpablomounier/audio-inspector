"""
analysis.py gets both audio_signal and audio_sample_rate from loader.py and analyses the audio file.
"""
from loader import load_audio

def get_audio_duration(audio_signal, audio_sample_rate):
    duration = len(audio_signal) / audio_sample_rate
    return duration


if __name__ == "__main__":
    audio_path = "C:/Users/juanp/Downloads/Audiocity.wav"
    signal, sample_rate = load_audio(audio_path)
    duration = get_audio_duration(signal, sample_rate)
    print(f"Audio duration: {duration:.2f} seconds")