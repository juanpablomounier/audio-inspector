"""
Audio Inspector CLI

Command line tool for basic audio analysis and MIR feature extraction.

Features
--------
- RMS measurement
- Peak detection
- Crest factor
- Frame energy
- Smoothed energy
- Novelty detection

Usage
-----
python -m audio_inspector.main file.wav

Author
------
Juan Pablo Mounier
"""
from __future__ import annotations
import argparse
from core.loader import load_audio
from core.validation import validate_signal, validate_sample_rate
from core.analysis import (
    get_audio_duration,
    get_audio_rms,
    get_audio_rms_db,
    get_audio_peak,
    get_audio_crest_factor,
    get_audio_cf_db
)

from core.framing import frame_signal

from features.energy import frame_energy, smooth_energy
from features.temporal import temporal_novelty, normalize_novelty

from visualization.plotting import (
    plot_energy,
    plot_smooth_energy,
    plot_novelty
)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Audio Inspector - basic MIR analysis tool"
    )

    parser.add_argument(
        "audio_file",
        help="Path to audio file (wav/mp3)"
    )

    parser.add_argument(
        "--no-plots",
        action="store_true",
        help="Disable plots"
    )

    return parser.parse_args()


def main():

    args = parse_arguments()

    audio_path = args.audio_file

    signal, sample_rate = load_audio(audio_path)

    validate_signal(signal)
    validate_sample_rate(sample_rate)

    duration = get_audio_duration(signal, sample_rate)

    rms = get_audio_rms(signal)
    rms_db = get_audio_rms_db(rms)

    peak = get_audio_peak(signal)

    crest = get_audio_crest_factor(peak, rms)
    crest_db = get_audio_cf_db(crest)

    frames, times = frame_signal(signal, sample_rate)

    energy = frame_energy(frames)

    smoothed = smooth_energy(energy)

    novelty = temporal_novelty(smoothed)

    novelty_norm = normalize_novelty(novelty)

    print("\nAudio analysis results")
    print("----------------------")

    print(f"File: {audio_path}")

    print(f"Duration: {duration:.2f} s")

    print(f"RMS: {rms:.6f}")
    print(f"RMS dBFS: {rms_db:.2f}")

    print(f"Peak: {peak:.6f}")

    print(f"Crest factor: {crest:.2f}")
    print(f"Crest factor dB: {crest_db:.2f}")

    print(f"Frames: {frames.shape}")
    print(f"Energy frames: {len(energy)}")

    print(f"Novelty frames: {len(novelty)}")

    if not args.no_plots:

        plot_energy(times, energy)

        plot_smooth_energy(times, smoothed)

        plot_novelty(times, novelty_norm)


if __name__ == "__main__":

    main()