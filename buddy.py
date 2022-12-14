import os, myKey
import openai, pyttsx3
import speech_recognition as sr

class assistant():
  api = myKey.key("myKey")
  openai.api_key = api

  def __init__(self):
    self.engine = pyttsx3.init()
    self.engine.setProperty('rate', 150)
    self.engine.setProperty('volume', 0.9)
    self.engine.setProperty('voice', 'english_rp+f4')
    self.recognizer = sr.Recognizer()

  def speak(self, text):
    self.engine.say(text)
    self.engine.runAndWait()

  def listen(self):

    with sr.Microphone(1) as source:
      print("Speak: ")
      audio = self.recognizer.listen(source)
      try:
        text = self.recognizer.recognize_google(audio)
        print("You said: {}".format(text))
        return text
      except:
        print("Sorry could not recognize what you said")

  def run(self):
    text = self.listen()
    # text = input("Enter text: ")

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=text,
      temperature=0.7,
      max_tokens=4000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    self.speak(response.choices[0].text)
    print(response.choices[0].text)

if __name__ == "__main__":
  assistant = assistant()
  assistant.run()

