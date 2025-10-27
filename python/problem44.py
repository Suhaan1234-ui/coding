import random
def game():
    print("welcome to the game")
    print("your lucky number is :")
    score=random.randint(1,100)
    print(score)
    #fetching the file
    with open("p44soln.txt") as a:
        highscore=a.read()
        if(highscore!=''):
            highscore=int(highscore)
        else:
            highscore=0
    #writing in the file
    if(score>highscore or highscore==''):
        with open("p44soln.txt","w") as a:
            a.write(str(score))
          
           
    return score
game()