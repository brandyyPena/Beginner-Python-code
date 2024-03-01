print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the quiz ? (yes/no) : ')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: What is your Favorite programming language? ')
    if answer.lower()== 'python' :
        score +=1
        print(' correct ')
    else:
        print('wrong Answer :( ')

answer=input(' Question 2: who is your favorite Professor? ')
if answer.lower()=='armel' :
    score += 1
    print('correct')
else:
    print('wrong Answer :( ')

answer=input('Question 3: What is your favorite course? ')
if answer.lower()=='bus472' :
    score +=1
    print('correct')
else:
    print('wrong Anwser :( ')

print('Thank you for playing this small quiz game, you attemted', score, "question correctly!")
mark=(score/total_questions)*100
print('Marks obtained: ',mark)

#added random for prize of 100
if mark== 100:

    import random
    possible_action=["10 points ex credit","HW pass","high five"]
    computer_action = random.choice(possible_action)
    print("your winning prize is "+ computer_action +" Congrats! ")

else:
    print( 'You lose no prize for you!' )