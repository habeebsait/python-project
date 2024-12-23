from gtts import gTTS
import os


# Set the text you want to pronounce
text = "shinchaun"

# Initialize gTTS object with text and language
tts = gTTS(text=text, lang='en')

# Save the audio to a file
tts.save("hello_world.mp3")

# Play the audio (macOS example)
os.system("afplay hello_world.mp3")

