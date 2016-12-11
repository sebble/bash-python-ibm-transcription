## Usage

Transcribe a new audio file:

    ./transcribe sample.wav

Preview the transcription:

    cat sample.wav*.json|jq '.results[].alternatives[0].transcript'
