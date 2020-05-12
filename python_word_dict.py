
import json
from difflib import get_close_matches

def loopagain():

    data = json.load(open('data.json'))

    def meaning(term):
     
        if term in data:
            return data[term]
        elif len(get_close_matches(term, data.keys())) > 0:
            response =  input("Did you mean %s instead ? Enter Y if yes, or N if no: "% get_close_matches(term, data.keys())[0])
            if response == "Y":
                return data[get_close_matches(term, data.keys())[0]] 
            elif response == "N" :
                return "Please double check your word."
            else:
                return "We did't understand your response."
        

        else:
            return "This word does not exsists.Check your word. "

    word = input("Enter the word: ")
    word = word.lower()
    output = meaning(word)
    if type(output) == list:
        for items in output:
            print(items)
    else:
        print(output)
    loopagain()

loopagain()

