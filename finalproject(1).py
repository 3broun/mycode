from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hi %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I'm available to help. ",]
    ],
     [
        r"(.*) your name ?",
        ["I have no name as of yet.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["No worries.","Its fine, don't pay attention to it.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Howdy",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Richmond, Virginia',]
    ],
    [
        r"(.*)raining in (.*)",
        ["We haven't seen a lot of rain in %2","In %2 it doesn't rain often",]
    ],
    [
        r"how (.*) health (.*)",
        ["Healthy mind, healthy body.  Well, thats what I've heard",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I like action sports",]
    ],
    [
        r"who (.*) (Cricketer|Batman)?",
        ["Doesnt matter.  They can't beat Goku."]
    ],
    [
        r"quit",
        ["It was a pleasure to chat with you","See you another day"]
    ],
    [
        r"(.*)",
        ['That is nice to hear.  I am limited in my responses. Maybe ask something else?']
    ],
]

reflections  = {
'i am': 'you are',
'i was': 'you were',
'i': 'you',
"i'm": 'you are',
"i'd": 'you would',
"i've": 'you have',
"i'll": 'you will',
'my': 'your',
'you are': 'I am',
'you were': 'I was',
"you've": 'I have',
"you'll": 'I will',
'your': 'my',
'yours': 'mine',
'you': 'me',
'me': 'you'}



#greeting at beginning of chat
print("Welcome.  You can ask me questions and I'll do the best to respond\n I can only accept questions in lower case.\n When you are ready to leave.  Just type quit ")
#Create Chat Bot
chat = Chat(pairs, reflections)

#begin
chat.converse()