import random
myName = input("Hello! What is your name?")
number = random.randint(1, 10)
print("Well. " + myName + "I am thinking of a number between 1 and 10")
guess = int(input("Take a Guess:"))
if guess == number:
    print("Good job" + myName + "! You guessed my number")
else:
    print("Wrong, better luck next time")
import random
myName = input("Hi, What is your name?")
number = random.randint(1, 100)
print("Tell me your favourite number and I'll tell you a joke")
guess = int(input("favourite number?"))
if guess <= 24:
    print("What's a dog's favourite detective..... Sherlock Bones")
elif guess <= 50:
    print("What do you get if you cross a vampire and a snowman? ... frostbite")
elif guess <= 75:
    print("What is brown, hairy and wears sunglasses? ,,, a coconut")
elif guess > 76:
    print("What do you call a bear with no teeth? ,,,,A gummy bear")
