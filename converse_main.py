import speech_recognition as sr
import openai

# https://www.analyticsvidhya.com/blog/2021/12/guide-for-speech-recognition/ -- example tutorial

# obtain audio from the microphone
r = sr.Recognizer()


chatting = True

language = language_setter()
print(language)

while chatting:
	with sr.Microphone() as source:
    	print("Talk with the bot!")
    	audio = r.listen(source)
    	response = openai.ChatCompletion.create(
        	model="gpt-3.5-turbo",
        	messages=[
            	{"role": "system", "content": "You are having a conversation and will respond as though you are in the middle of whatever conversation the user starts asking you about"},
            	{"role": "user", "content": audio},
        	]
    	)
    	print(response)


# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

def language_setter():
	with sr.Microphone() as source:
    	print("What language are you speaking?")
    	audio = r.listen(source)
        response = openai.ChatCompletion.create(
        	model="gpt-3.5-turbo",
        	messages=[
            	{"role": "system", "content": "You will tell the user what language they are speaking"},
            	{"role": "user", "content": audio},
        	]
    	)
    language = response
    return language
