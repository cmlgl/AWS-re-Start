import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


# Se o usuário não adivinhou a resposta certa, insira o loop.

# Peça ao usuário um palpite.

# O palpite é o número certo?

# Se o palpite estiver certo, diga ao usuário que o palpite estava certo e saia do loop.

# Se o palpite estiver errado, diga ao usuário que o palpite estava errado e mantenha o loop.


print("Count to 10!")


for x in range (0,11):
    print(x)