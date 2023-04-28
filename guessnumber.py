import random

print("wwelcome to guess the number!")
print("The rule a simple, i will think a number , and you will guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
   guess = input("Guess a number between 1 and 10: ")
   if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
   else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

