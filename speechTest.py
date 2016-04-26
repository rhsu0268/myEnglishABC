import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')
for voice in voices:
	print("Using voice:", repr(voide))
	engine.setProperty('voice', voice.id)
	engine.say('Hi there, how are you?')
	engine.say('My name is Richard Hsu')
engine.runANdWait()