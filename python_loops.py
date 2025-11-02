'''spam = 0
while spam < 5:
    print("hello world")
    spam = spam + 1

if spam < 5:
    print('hello world')
    spam = spam + 1

while True:
    print("what is your name")
    name=input('>')
    if name == 'your name':
        break
print('thank you')

while True:
    print("who are you ")
    name = input(">")
    if name != 'joe':
        continue
    print("hello, joe what is the password")
    password = input('>')
    if password == 'swordfish':
        break

print("access granted")'''

'''print("hello world")
for i in range(5):
    print('hello world')


total = 0

for i in range(101):
    total = total+i

print(total)'''
'''
import random
secret = random.randint(1,20)
print(secret)

for i in range(1,7):
    print("enter a number between 1,20")
    num = int(input('>'))

    if num < secret:
        print("your guess is too low")

    elif num > secret:
        print("your guess is too high")
    else:
        break

if num == secret:
    print("good job the number is right")
else:
    print("1too many chances ",f"the number is {secret}")
'''
import random,sys
print("ROCK, PAPER , SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print("Enter your move: r(rocks) s(scissors) p(paper) or q for quit")

    while True:
               player_move = input(">")
               if player_move == 'q':
                       sys.exit()
               else:
                       break
               
    if player_move == 's':
            print("Scissor versus...")
    elif player_move == 'r':
            print("Rock versu...")
    elif player_move == 'p':
            print("paper versus .....")


    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')


    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1           


    