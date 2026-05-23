import pyjokes

# print("printing jokes...")

# this prints a random joke
joke = pyjokes.get_joke()
print(joke)


import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate',200)
engine.setProperty('volume',0.90)

voices = engine.getProperty('voices') #to change the voice
engine.setProperty('voice',voices[1].id)

engine.say(joke)
engine.runAndWait()



# so thanks 
# # that was my programm
# # another line 
# # yet another line 

"""hello lets go
more line .."""

'''lets try this 
the end'''