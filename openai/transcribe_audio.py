from openai import OpenAI
client = OpenAI()

audio_file= open("../ralf_vie_mort_couple_20241224.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)

print(transcription.text)
