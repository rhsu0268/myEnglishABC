#import pyttsx
#engine = pyttsx.init()
#engine.setProperty('rate', 70)

# voices = engine.getProperty('voices')
# for voice in voices:
# 	print("Using voice:", repr(voice))
# 	engine.setProperty('voice', voice.id)
# 	engine.say('Hi there, how are you?')
# 	engine.say('My name is Richard Hsu')
# engine.runANdWait()

from gtts import gTTS
from tempfile import TemporaryFile
tts = gTTS(text='Hello', lang='en')
tts.save("hello-1.mp3")

# f = TemporaryFile()
# tts.write_to_fp(f)
# f.close()


#tts2 = gTTS(text='Hello, my name is Richard Hsu. The red fox jumped over the red cow and sstx.', lang='en')
#tts2.save("hello-2.mp3")

# tts3 = gTTS(text='Hello, my name is Richard Hsu. I am a graduate student at GW.', lang='zh')
# tts3.save("hello-3.mp3")

# tts4 = gTTS(text='Hello, my name is Richard Hsu. I am a graduate student at GW.', lang='zh-cn')
# tts4.save("hello-4.mp3")

#import os

#os.system("espeak. 'The quick brown fox'")
