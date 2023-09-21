import speech_recognition as sr

#https://www.analyticsvidhya.com/blog/2021/12/guide-for-speech-recognition/ -- example tutorial

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())