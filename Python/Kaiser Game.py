#IMPORTING NECESSARY LIBRARIES

from time import sleep

#READING DATABASE FILE

file = open('database.txt', 'r')
scan = file.read()
exec(scan)

#PRE-DEFINED MESSAGES

welcome_text = "This is the Kaiser Game©\nAn Simple Quiz game to restablish the Prussia\nMade by Pratham Kalgutkar\n"

instructions = "Input to answer the Questions and Press Enter\nInput 'Close' to end the game\n"

notice = "!!!PLEASE ENTER VALID INPUTS ONLY!!!\n"

thank_you = "Thank You for Playing the game\nKaiser Game© Made by Pratham Kalgutkar\n"

S = "YOU SKIPPED THE QUESTION"

R = "CORRECT ANSWER!"

N = "NEXT QUESTION\n"

W = "WRONG ANSWER 🙁\nCORRECT ANSWER IS"

score = 0 

run = True

Max_Score = len(database)

#QUIZ FUNCTION 

def quiz(que,ans):
    '''Check User Input and Execute Operations
    Question and its Ansswer is feeded from Dictionary
    The user input is requested and input is Checked with Answer for True or False
    If True, Increment in Score is returned, False, Skip returns None and moves to next codeblock
    if "Close" is inputted Run is returned as False
    '''
    global score
    global run
    
    print(que)
    a = input().lower().replace(" ","")
    if a == "close":
        run = False
        return run
    elif a == "skip":
        print(S)
        print(N)
    elif a == ans:
        print(R)
        print(N)
        score=score+1
    else:
        print(W,ans)
        print(N)

#LOOP FUNCTION

def loop(que,ans):
    '''Check for Run Value
    If Run is True, the quiz function is runned
    The Function checks for Run Value returned by Quiz Function
    The Default Run Value is True, If Run value is False then Loop is skipped
    '''
    while run == True:
        quiz(que,ans)
        break

#RESTART FUNCTION

def restart():
    pass

#START

sleep(2)
print(welcome_text)
sleep(3)
print(instructions)
sleep(2)
print(notice)
sleep(3)
print("Game starting in 5 seconds")
sleep(5)

#LOOP

for que, ans in database.items():
    loop(que,ans)

#END

sleep(2)
print("ooo...That Marks the end of Game\n")
sleep(3)
print("Your Score : ",score)
sleep(2)
if score == Max_Score:
    print("\nYou Successfully Re-established Prussia\nKaiser is Proud of you\n")
else:
    print("\nYou failed to Re-establish Prussia\nKaiser is Proud of you attempt\n")
sleep(3)

while True:
    print("Do you want to play again? (Y/N)")
    replay = input().lower().replace(" ","")
    if replay == "y":
        restart()
    elif replay == "n":
        print(thank_you)
        print("Game will close in 10 seconds")
        break
sleep(10)
