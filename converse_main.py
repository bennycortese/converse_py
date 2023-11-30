import speech_recognition as sr
import openai

# https://www.analyticsvidhya.com/blog/2021/12/guide-for-speech-recognition/ -- example tutorial

# obtain audio from the microphone
r = sr.Recognizer()


chatting = True

language = language_setter()
validLanguage = False
while not validLanguage:
    try:
        check_if_valid(language)
        validLanguage = True
    except:
	#todo, put a verbal print "error occured, need to redo what language you're using"
        language = language_setter()

print("Talk with the bot!")
#todo, this print should be a verbal statement, and make it the desired language
while chatting:
	with sr.Microphone() as source:
    	audio = r.listen(source)
    	response = openai.ChatCompletion.create(
        	model="gpt-3.5-turbo",
        	messages=[
            	{"role": "system", "content": "You are having a conversation and will respond as though you are in the middle of whatever conversation the user starts asking you about"},
            	{"role": "system", "content": "If the user asks me a personal question I will respond as though I was a regular person because that will help them learn the language they are speaking better"},
                {"role": "user", "content": audio},
        	]
    	)
    	print(response)
	#todo, this print should be a verbal statement as well


# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

def language_setter():
	with sr.Microphone() as source:
    	print("What language are you speaking?")
	#todo, this print should be a verbal statement
    	audio = r.listen(source)
        response = openai.ChatCompletion.create(
        	model="gpt-3.5-turbo",
        	messages=[
            	{"role": "system", "content": "You will tell the user what language they are speaking"},
            	{"role": "user", "content": audio},
        	]
    	)
	response2 = openai.ChatCompletion.create(
        	model="gpt-3.5-turbo",
        	messages=[
            	{"role": "system", "content": "convert this language to an abbreviation that works with python code: " + response},
        	]
    	)
    language = response
    return language
