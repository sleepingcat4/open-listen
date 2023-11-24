from gtts import gTTS
import os
import time

def text_toaudio(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        tts = gTTS(content, lang='en')

        audio_output_path = os.path.splitext(file_path)[0] + ".mp3"
        tts.save(audio_output_path)

        time.sleep(5)

        os.system("start " + audio_output_path)

        print(f"Audio file saved as {audio_output_path}")

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
