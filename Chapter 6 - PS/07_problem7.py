# Q7.> Write a program to find out whether a give post is
# talking about "Harry " or not.
# Solution.>

post = input("Enter the post here : ")
import pyttsx3
s = pyttsx3.init()
if("Harry" in post ):
    print("Yes,it is talking about \"harry\" ")
    # s.say(post)
    s.say("Yes,it is talking about \"harry\" ")
    s.runAndWait()
else:
    print("No, it is not talking about \"Harry\" ") 
    s.say("No, it is not talking about \"Harry\" ")
    s.runAndWait()
    
# above code is case sensetive i.e. for
# harry and Harry and HaRry this gives different result
# 
# 
# introducing new comand : .lower()
# using this comand only in case of string datatype it,
# lowers all the characters of the mentioned string 
# i.e. "ArYan".lower() # ouput: aryan
# line = "THis is A LiNE ."
# print(line.lower())# ouput: this is a line
# 
# using it in above question: 

name = "Harry"
post = input("Enter the post here : ")
import pyttsx3
s = pyttsx3.init()
if(name.lower() in post.lower() ):
    print("Yes,it is talking about \"harry\" ")
    # s.say(post)
    s.say("Yes,it is talking about \"harry\" ")
    s.runAndWait ()
else:
    print("No, it is not talking about \"Harry\" ") 
    s.say("No, it is not talking about \"Harry\" ")
    s.runAndWait()
