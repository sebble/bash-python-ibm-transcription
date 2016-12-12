## Requirements

- SpeechRecognition (pip)
- Python3 (for SpeechRecognition)
- libav-tools (for avprobe, avconv)
- jq (for JSON->MD)

## Usage

> **Notes:** This relies on https://pypi.python.org/pypi/SpeechRecognition/. There are better ways to do this. I have not tested sending a full file without splitting. I am not using the asynchronous endpoints. I do not capture the timestamps, nor speaker identity. I do not set the language model. I use WAV when I could use OPUS (to reduce disk usage). But... it works, and I didn't have to write much code.

Set environment variables for speech-to-text service:

    $ vi .env
    IBM_USERNAME="asdfghjkl-asdfghjkl"
    IBM_PASSWORD="12345678"
    
    $ eval $(cat .env|grep -v ^#|sed 's/^/export /')

or

    export IBM_USERNAME="asdfghjkl-asdfghjkl"
    export IBM_PASSWORD="12345678"

Transcribe a new audio file:

    ./transcribe.sh sample.wav

Preview the transcription:

    ./markdown.sh sample.wav > sample.wav.md
