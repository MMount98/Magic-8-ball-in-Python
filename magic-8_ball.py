# import
import random

# Global Varibles
name = "Michael"
question = "Will I learn Python 3?"
answer = ""
random_number = random.randint(1, 11)

# logic for 8-ball
#Checks the vaule randomly set to "random_number" and sets ansert value accordingly
if random_number == 1:
    answer = "Yes"
elif random_number == 2:
    answer = "No"
elif random_number == 3:
    answer = "Yes - Definitely"
elif random_number == 4:
    answer = "It is decidely so"
elif random_number == 5:
    answer = "Without a doubt"
elif random_number == 6:
    answer = "Reply hazy, try again"
elif random_number == 7:
    answer = "Ask again later"
elif random_number == 8:
    answer = "Better Not tell you now"
elif random_number == 9:
    answer = "My sources say no"
elif random_number == 10:
    answer = "Outlook not so good"
elif random_number == 11:
    answer = "Very doubful"
else:
    answer = "The sprits are busy"

# Prints Statement and question
# Logic in place if promtps are added later on
if name == "":
    print("Question: " + question)
else:
    print(name + " asks: " + question)
if question == "":
    print("Magic 8-ball can not forsee your question, please enter in a question to ask the magic 8-ball!")
else:
    print("Magic 8-ball's answer: " + answer)
