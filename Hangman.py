#Hangman
from time import sleep
import random
def parts(x):
    if x == 0:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 1:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 2:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 3:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|     ')
        print('------------')
    if x == 4:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|   / \\')
        print('------------')
#Prints a hangman picture
print("Welcome to Hangman")
print('   ',  '------')
print('   ',  '|    |')
print('   ',  '|    O')
print('   ',  '|   -|-')
print('   ',  '|    |')
print('   ',  '|   / \\')
print('------------')


words = ['python','hangman','pattarai','program']

picked = random.choice(words)

print("Okay Ive got it!")

print("The word has", len(picked), "letters")

for i in range(len(picked)):
    print('_',' ', end = "")
    
print()


#Creates a list with _ marks for letters
right = ['_'] * len(picked) 
wrong = []

#Prints letters in right with _'s
def add_letter():
    for i in right:
        print(i, ' ', end = "")
    print()

#Prints out wrong letters
def wrong_letter():
    print("Wrong letters:", end = "")
    for i in wrong:
        print(i,' ',end = "")
    print()

#Main Loop        
while True:
    print('=====================')
    guess = input("Guess a letter : ")
    if guess in picked:
        print("Let me check")
        
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index = index + 1

        add_letter()
        wrong_letter()
        parts(len(wrong))
        
    elif guess not in picked:
        print("Let me check")
        if guess in wrong:
            print("You already guessed", guess)
            wrong_letter()
        else:
            print(guess, "is not in my word")
            wrong.append(guess)
            add_letter()
            wrong_letter()
            parts(len(wrong))
            
    if len(wrong) > 4:
        print("Game Over!")
        print("I picked", picked)
        break
    
    if '_' not in right:
        print("You guessed it!")
        print("I picked", picked)
        break