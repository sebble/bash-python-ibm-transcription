#!/usr/bin/env python3

import speech_recognition as sr
import json
from os import path, environ
from sys import argv, exit

IBM_USERNAME = environ.get('IBM_USERNAME', None)
IBM_PASSWORD = environ.get('IBM_PASSWORD', None)

if IBM_USERNAME is None:
    raise ValueError("IBM_USERNAME is not set")
if IBM_PASSWORD is None:
    raise ValueError("IBM_PASSWORD is not set")
if len(argv) < 2:
    raise ValueError("Usage: %s <audio_file>"%argv[0])

FILENAME = argv[1]
JSONFILE = FILENAME+'.json'

if path.isfile(JSONFILE):
    print("Transcription already exists. Skipping.")
    exit(0)

r = sr.Recognizer()
with sr.AudioFile(FILENAME) as source:
    audio = r.record(source)

try:
    print("Processing...")
    output = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, show_all=True)
    with open(JSONFILE,'w+') as f:
        json.dump(output, f)
    print("IBM Speech to Text thinks you said:")
    print(json.dumps(output))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

