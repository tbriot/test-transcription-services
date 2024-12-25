# How to run audio files transcriptions ?
## OpenAI
```
export OPENAI_API_KEY=...

# Audio file must be present in repo's root directory
export AUDIO_FILE=ralf_vie_mort_couple_20241224.mp3

cd openai
. ./.venv/bin/activate
pip install -r requirements.txt
python3 ./transcribe_audio.py
```
