import random
from urllib.request import urlopen
import sys
WORD_URL = "http://learncodinghardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%)":
        "Make a calls named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)" :
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(sel, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attributes and set it to '***'."
}

# do othey want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%")) ]
    other_names = random.sample(WORDS, snippet("***"))
    results =[]
    param_names =[]
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', ' .join(random.sample(WORDS,param_count)))

    for sentence in snippet,phrase:
        result = sentence[:]

    #fake class name 
    for word in class_names:
        result = result.replace("%%%",word,1)
    
    for word in other_names:
        result = result.replace("***",word,1)
    
    for word in param_names:
        result = result.replace("@@@",word,1)

        result.append(result)

    return result

#keep going until they hit CTRL+D
try:
    while True:
        snippet = list(PHRASES.keys())
        random.shuffle(snippet)

        for snippet in snippet:
            phrase = PHRASES[snippet]
            question ,answer = convert (snippet,phrase)
            if PHRASES_FIRST:
                question,answer = answer,question

            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")

except EOFError:
    print("\nBye")


