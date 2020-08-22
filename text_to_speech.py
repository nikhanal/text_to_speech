import pyttsx3
text = 'hello i am nishan. how are you doing?'
engine = pyttsx3.init()
voices = engine.getProperty('voices')
en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK'
engine.setProperty('voice', en_voice_id)
engine.say(text)
engine.runAndWait()
