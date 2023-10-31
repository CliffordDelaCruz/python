# Magic 8-ball
question =  "Should I train Jiujitsu today?"
answer = ""
# import random library
import random
random_number = random.randint(1, 10)
#print(random_number)
if question != "":
  if random_number == 1:
    answer="Yes - definitely"
  elif random_number == 2:
    answer="It is decidedly so"
  elif random_number == 3:
    answer="Without a doubt"
  elif random_number == 4:
    answer="Reply Hazy, try again"
  elif random_number == 5:
    answer="Ask again later"
  elif random_number == 6:
    answer="Better not to tell you now"
  elif random_number == 7:
    answer="My sources say no"
  elif random_number == 8:
    answer="Outlook not so good"
  elif random_number == 9:
    answer="Very doubtful"
  elif random_number == 10:
    answer="Not adviseable"
  else:
    answer="Error"
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print("Question should not be blank!")