#!/usr/bin/env python3

import html

def main():

    #given trivia
    trivia= {
            "category": "Entertainment: Film",
            "type": "multiple",
            "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
            "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
            "incorrect_answers": [
                "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
                "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
                "&quot;Round up the usual suspects.&quot;"
                ]
            }
    
    #inform the user they are playing a trivia game
    print("Welcome to trivia!")

    #the question
    print(html.unescape(trivia["question"]))

    #print the 4 possible answers
    print("A ", html.unescape(trivia["incorrect_answers"][0]))
    print("B ", html.unescape(trivia["incorrect_answers"][1]))
    print("C ", html.unescape(trivia["incorrect_answers"][2]))
    print("D ", html.unescape(trivia["correct_answer"]))

    user_answer = input("Please select answer A, B, C, or D: ")

    if user_answer == "D":
        print("Answer D is correct!")
    else:
        print("Answer", user_answer, "is not correct, sorry :(")



main()