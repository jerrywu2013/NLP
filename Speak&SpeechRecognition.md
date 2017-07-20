```
#Speak
from gtts import gTTS
import tempfile
from pygame import mixer

tts = gTTS(text='早安您好', lang='zh')
tts.save("hello.mp3")

mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()

def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang='zh')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

speak('裕隆早安你好，最近如何')

#SpeechRecognition
import speech_recognition

r = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    audio = r.listen(source)

r.recognize_google(audio, language=‘zh-TW’)

```
