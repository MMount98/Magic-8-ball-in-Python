# import
import random

# Global Varibles
name = "Michael"
question = "Will I learn Python 3?"
answer = ""
random_number = random.randint(1, 11)


# logiv for 8-ball
if random_number == 1:
    answer = "Yes"
elif random_number == 2:
    answer = "No"
elif random_number == 3:
    answer = "Yes - Definitely"
elif random_number == 4:
    answer = "It is devidely so"
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
print(name + " asks: " + question)
print("Magic 8-ball's answer: " + answer)

