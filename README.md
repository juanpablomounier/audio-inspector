# Audio Inspector

Python audio analysis toolkit for basic DSP and Music Information Retrieval.

## Features

- RMS level
- Peak level
- Crest factor
- Frame energy
- Smoothed energy
- Temporal novelty detection

## Installation

Clone repo:

git clone https://github.com/juanpablomounier/audio-inspector

cd audio-inspector

Install dependencies:

pip install -r requirements.txt

## Usage

Basic:

python -m audio_inspector.main file.wav

Disable plots:

python -m audio_inspector.main file.wav --no-plots

## Architecture

audio_inspector/

core/
basic DSP operations

features/
MIR feature extraction

visualization/
plots

main.py
CLI entry point

## Example output

Audio analysis results

Duration: 210.49 s

RMS dBFS: -32.13

Crest factor: 11.28

## Future work

Spectral features

Onset detection

Tempo estimation

## Author

Juan Pablo Mounier