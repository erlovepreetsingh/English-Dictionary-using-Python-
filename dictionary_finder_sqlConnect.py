import mysql.connector
from difflib import get_close_matches

def loopagain():
    con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database",
    )

    cursor = con.cursor()

    def get_expressions():
        cursor.execute("SELECT * FROM Dictionary")
        results = cursor.fetchall()

        exprs = []

        for items in results:
            expression = items[0]
            exprs.append(expression)
        return exprs

    def meaning(term):
     
        if term in list_of_expressions:
            cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % term)
            return cursor.fetchall()



        elif len(get_close_matches(term, list_of_expressions)) > 0:
            response =  input("Did you mean %s instead ? Enter Y if yes, or N if no: "% get_close_matches(term, list_of_expressions)[0])
            if response == "Y":
                word_to_find = get_close_matches(term, list_of_expressions)[0]
                cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word_to_find)
                return cursor.fetchall()
             
            elif response == "N" :
                return "Please double check your word."
            else:
                return "We did't understand your response."
        

        elif len(get_close_matches(term, list_of_expressions)) == 0:
            return "This word does not exsists.Check your word. "



    word = input("Enter the word: ")
    list_of_expressions = get_expressions()
    word = word.lower()
    output = meaning(word)
    if type(output) == list:
        for item in output:
            print("Meaning - " + item[1])
    else:
        print(output)
        
    loopagain()

loopagain()