# How to run audio files transcriptions ?
## OpenAI
```
export OPENAI_API_KEY=...

# Audio file must be present in repo's root directory
export AUDIO_FILE=ralf_vie_mort_couple_20241224.mp3

cd openai
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 ./transcribe_audio.py
```

# Audio files size
- ~30 min audio file in mp3 @192kbps is 40 MB
- ~4 min audio file in mp3 @192kbps is 6 MB

# Transcription services review
## OpenAI Audio API (Whisper)
- max input file size is 25 MB only (~15min audio files)
- 4 min mp3 file of 6 MB takes ~15 sec to get transcribed
- Cost (USD): $0.006 / min
    - $0.024 for 4 min audio file
    - $0.360 for 60 min audio file
    - $1 gives you ~ 3 hours of transcription

## OpenAI ChatGPT
- audio file can be submitted as an attachment directly in ChatGPT and get transcripted ?

## Amazon Transcribe
- audio file has to be uploaded to an S3 bucket
- max audio file size is 2 GB
- max audio file length is 14400 seconds = 4 hours
- 4 min mp3 file of 6 MB takes ~1 min to get transcribed
- 29 min mp3 file of 40 MB takes ~3 min to get transcribed
- Cost (USD):
    - $0.02400 / min when < 250k min
    - $0.01500 / min up to 1M min
    - $0.01020 / min up to 5M min
    - much more expensive than OpenAI Audio API! 4 times more expensive! But offers more capabilities.
    - $1 gives you ~ 40 min of transcription
