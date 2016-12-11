## Usage

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
