import os
from openai import OpenAI
client = OpenAI()

audio_file= open(os.path.join("..", os.environ["AUDIO_FILE"]), "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    language="fr",
    response_format="text"
)

print(transcription)
