import random
# first version of game where user try to guees computers number
def guess(x,y):
    random_number = random.randint(x,y)
    guess=0
    score=100

    while guess != random_number:
        guess= int(input(f'Guess a number between {x} and {y}:'))
        if guess < random_number:
          print("sorry ,your guess is two low")
          score=score-1
          print(score)
        elif guess > random_number:
          print("sorry. your guess is two high")
          score=score-1
          print (score)
    print(f'yay,congrats you have guess the correct number {random_number} correctly')
    score=score
    print(score)

    # second version of game where the computer  guess our number 
def computer_guess(x,y):
    low = x
    high = y
    feedback=" "
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess =  low
        feedback = input(f'Is {guess} too high (h) ,too low (l), or coreect (c) ??')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f' yay ,computer guess the number,{guess},correctly')
    

z=int(input("enter the number"))
w=int(input("enter the number"))
guess(z,w)
computer_guess(z,w)