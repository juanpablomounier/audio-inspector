This is a audio inspector/analyzer. This is it's architecture:

audio-inspector/
│
├── audio_inspector/
│   ├── __init__.py
│   └── loader.py   
│
├── README.md
├── .gitignore
└── main.py

Next, a brief explanation of each script's module:

loader.py:
    It's a valid audio file loader. It has no other task that verify if the audio file is ok and load it.