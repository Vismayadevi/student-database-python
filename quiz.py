print("Welcome to the Quiz Game!")
play = input("Do you want to play? (yes/no): ")

if play.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's start the quiz 😊")

score = 0

# CPU
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# RAM
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# GPU
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# HTML
answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# SQL
answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# OS
answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# IP
answer = input("What does IP stand for? ")
if answer.lower() == "internet protocol":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# URL
answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

total_questions = 8
percentage = (score / total_questions) * 100

print("You got", score, "out of", total_questions, "questions correct.")
print("Your score is", percentage, "%")
if percentage >= 80:
    print("Excellent! 🎉")
elif percentage >= 50:
    print("Good job 👍")
else:
    print("You can do better 💪")