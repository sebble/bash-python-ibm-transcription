## Usage

> **Notes:** This relies on https://pypi.python.org/pypi/SpeechRecognition/. There are better ways to do this. I have not tested sending a full file without splitting. I am not using the asynchronous endpoints. I do not capture the timestamps, nor speaker identity. I do not set the language model. I use WAV when I could use OPUS (to reduce disk usage). But... it works, and I didn't have to write much code.

Set IBM variables:

    $ vi .env
    IBM_USERNAME="asdfghjkl-asdfghjkl"
    IBM_PASSWORD="12345678"

Set environment variables:

    eval $(cat .env|grep -v ^#|sed 's/^/export /')

Transcribe a new audio file:

    ./transcribe sample.wav

Preview the transcription:

    ./markdown.sh sample.wav > sample.wav.md
