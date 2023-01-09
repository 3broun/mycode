#!/usr/bin/env python3

import random


name= input("What is your name?")
print("Hi", name, "Do you wanna play a game?")

answer= input(" Yes or No")

if answer.lower == "yes":
	print("Good. Inside this quiz there are 10 questions.  You have to gain a minimum of 6 questions correct to pass.")

question1= {"question": "What was the monster in 1954's 'Them'?",
    "Koala": False,
    "Ants": True,
    "Blob": False,
    "Zombies": False,
    }

print(question1)
qanswer= input("What is the answer?")
	
if qanswer == True:
	print ("Correct")

else:
    print ("Incorect")
