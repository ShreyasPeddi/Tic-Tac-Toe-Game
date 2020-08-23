#Programmer: Shreyas Peddi
#Date:
#Program Description:
#Input:
#Processing:
#Output:

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random as r

#All the global variables used
global player1Mark, player2Mark, gamesWonPlayer1, gamesWonPlayer2
global currentGame, numOfGames, k, numberOfGames
global b1, b2, b3, b4,b5, b6, b7, b8,b9
global gamesWonPlayer, gamesWonComputer, computerTurn, nameTextfield
global firstRow, secondRow, thirdRow
global firstColumn, secondColumn, thirdColumn

#All the variable initailised
b1=""
b2=""
b3=""
b4=""
b5=""
b6=""
b7=""
b8=""
b9=""
k=0
player1Mark=""
player2Mark=""
gamesWonPlayer1=0
gamesWonPlayer2=0
currentGame=1
gamesWonPlayer=0
gamesWonComputer=0
computerTurn=0
firstRow=''
secondRow=''
thirdRow=''
firstColumn=''
secondColumn=''
thirdColumn=''
gamesLeft=1
numberOfGames=0

#Checks turn by comparing with playerMarks and then calling another function which highlights the player name in the game to indicate turn.
def checkTurn(text):
    global player1Mark, player2Mark

    if len(player1Mark)>0:
        

        if text=="x" :
            if player1Mark=='x':
                highlightTurns2()
            else:
                highlightTurns1()
        elif text=="o":
            if player1Mark=='x':
                highlightTurns1()
            else:
                highlightTurns2()

#Displays 1 on the same location as the button
def displayButton1(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=25,y=100, width=50, height=50)
    checkTurn(textDis)
    
#Displays 2 on the same location as the button
def displayButton2(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=100,y=100, width=50, height=50)
    checkTurn(textDis)

#Displays 3 on the same location as the button
def displayButton3(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=175,y=100, width=50, height=50)
    checkTurn(textDis)

#Displays 4 on the same location as the button
def displayButton4(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=25,y=200, width=50, height=50)
    checkTurn(textDis)

#Displays 5 on the same location as the button
def displayButton5(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=100,y=200, width=50, height=50)
    checkTurn(textDis)

#Displays 6 on the same location as the button
def displayButton6(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=175,y=200, width=50, height=50)
    checkTurn(textDis)

#Displays 7 on the same location as the button
def displayButton7(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=25,y=300, width=50, height=50)
    checkTurn(textDis)

#Displays 8 on the same location as the button
def displayButton8(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=100,y=300, width=50, height=50)
    checkTurn(textDis)

#Displays 9 on the same location as the button
def displayButton9(textDis):

    label=tk.Label(gameFrame, text=textDis, fg="black", bg="white",font="Arial 22 bold")
    label.place(x=175,y=300, width=50, height=50)
    checkTurn(textDis)


def highlightTurns1():
    global player1Mark, player2Mark, playerName1, playerName2
    
    string1=playerName1+"-"+player1Mark
    player1NameLabel=tk.Label(gameFrame, text=string1,fg="black",bg="red",font="Arial 15 bold")
    player1NameLabel.place(x=25,y=400)

    string2=playerName2+"-"+player2Mark
    player2NameLabel=tk.Label(gameFrame,text=string2,fg="black",font="Arial 15 bold")
    player2NameLabel.place(x=25,y=425)

def highlightTurns2():
    global player1Mark, player2Mark, playerName1, playerName2
    
    string1=playerName1+"-"+player1Mark
    player1NameLabel=tk.Label(gameFrame, text=string1,fg="black",font="Arial 15 bold")
    player1NameLabel.place(x=25,y=400)

    string2=playerName2+"-"+player2Mark
    player2NameLabel=tk.Label(gameFrame,text=string2,fg="black",bg="red",font="Arial 15 bold")
    player2NameLabel.place(x=25,y=425)
    
def button1Function():
    global k
    global b1
    global computerTurn, player1Mark
    global firstRow, firstColumn
    gridLocation="b1"

    
    print("THE Value of k is",k)
    if k<0:
        
        if k==-1:
            firstRow=firstRow+"x"
            firstColumn+="x"
            b1="x"# Player's Move
            displayButton1(b1)
            checkWinO()
            

            playComputer(gridLocation)
            
            

        elif k==-3:
            firstRow=firstRow+"o"
            firstColumn+="o"
            b1="o"# Player's Move
            displayButton1(b1)
            checkWinO()
            
            playComputer(gridLocation)
            
    if k>=0:
        
##        
        if k%2==0:
            string1=playerName1+"-"+player1Mark
    
                
            b1="x"
            checkWinO()
            
            
        elif k%2==1:
            b1="o"
            checkWinO()
    
    if len(b1)>=1 and k>=0:
        displayButton1(b1)
        k+=1


def button2Function():
    global b2
    global k
    gridLocation="b2"
    global firstRow, secondColumn

    if k<0:
        if k==-1:
            firstRow=firstRow+"x"
            secondColumn+="x"
            b2="x"
            displayButton2(b2)
            checkWinO()
            
            playComputer(gridLocation)
            

        elif k==-3:
            firstRow=firstRow+"o"
            secondColumn+="o"
            b2="o"# Player's Move
            displayButton2(b2)
            checkWinO()
            
            playComputer(gridLocation)
            
    if k>=0:

        if k%2==0:
            b2="x"
            checkWinO()
        

        elif k%2==1:
            b2="o"
            checkWinO()
    
    if len(b2)>=1 and k>=0:
        displayButton2(b2)
        k+=1

def button3Function():
    global b3
    global k
    gridLocation="b3"
    global firstRow, thirdColumn
    if k<0:
        
        if k==-1:
            firstRow=firstRow+"x"
            thirdColumn+="x"
            b3="x"
            displayButton3(b3)
            checkWinO()
            
            playComputer(gridLocation)
            

        elif k==-3:
            firstRow=firstRow+"o"
            thirdColumn+="x"
            b3="o"# Player's Move
            displayButton3(b3)
            checkWinO()
            
            playComputer(gridLocation)
            
    if k>=0:
        
        if k%2==0:
            b3="x"
            checkWinO()
            

        elif k%2==1:
            b3="o"
            checkWinO()


    if len(b3)>=1 and k>=0:
        displayButton3(b3)
        k+=1

def button4Function():
    global k
    global b4
    text=""
    gridLocation="b4"
    global secondRow
    global firstColumn

    if k<0:
        
        if k==-1:
            secondRow=secondRow+"x"
            firstColumn+="x"
            b4="x"
            displayButton4(b4)
            checkWinO()
            
            playComputer(gridLocation)
            

        elif k==-3:
            secondRow=secondRow+"o"
            firstColumn+="o"
            b4="o"# Player's Move
            displayButton4(b4)
            checkWinO()
            
            playComputer(gridLocation)
            

    if k>=0:
        
        if k%2==0:
            b4='x'
            checkWinO()

            
        elif k%2==1:
            b4="o"
            checkWinO()


    if len(b4)>=1 and k>=0:
        displayButton4(b4)
        k+=1


def button5Function():
    global k
    global b5
    text=""
    gridLocation="b5"
    global secondRow, secondColumn
    if k<0:
        
        if k==-1:
            b5="x"
            secondRow=secondRow+"x"
            secondColumn+="x"
            print("Player's turn first")
            
            displayButton5(b5)
            
            playComputer(gridLocation)
            

        elif k==-3:
            b5="o"
            secondRow=secondRow+"o"
            secondColumn+="o"
            # Player's Move
            displayButton5(b5)
            
            playComputer(gridLocation)
            
        
    if k>=0:
        
        if k%2==1:
            b5='o'
            checkWinO()
            

        elif k%2==0:
            b5='x'
            checkWinO()
        


    if len(b5)>=1 and k>=0:
        displayButton5(b5)
        k+=1

def button6Function():
    global k
    global b6
    text=""
    gridLocation="b6"
    global secondRow, thirdColumn
    

    if k<0:
        
        if k==-1:
            secondRow=secondRow+"x"
            thirdColumn+="x"
            b6="x"
            displayButton6(b6)
            checkWinO()
            
            print(secondRow)
            playComputer(gridLocation)
            

        elif k==-3:
            secondRow=secondRow+"o"
            thirdColumn+="x"
            b6="o"# Player's Move
            displayButton6(b6)
            checkWinO()
            
            playComputer(gridLocation)
            
    if k>=0:
        
        if k%2==0:
            b6='x'
            checkWinO()


        elif k%2==1:
            b6='o'
            checkWinO()

        
    if len(b6)>=1 and k>=0:
        displayButton6(b6)
        k+=1


def button7Function():
    global k
    global b7
    text=""
    gridLocation="b7"
    global thirdRow
    global firstColumn

    if k<0:
        
        if k==-1:
            thirdRow+='x'
            firstColumn+="x"
            b7="x"
            displayButton7(b7)
            checkWinO()
            
            playComputer(gridLocation)
            

        elif k==-3:
            thirdRow+='x'
            firstColumn+="o"
            b7="o"# Player's Move
            displayButton7(b7)
            checkWinO()
            
            playComputer(gridLocation)
            

    if k>=0:
        
        if k%2==0:
            b7='x'
            checkWinO()
            
        elif k%2==1:
            b7="o"
            checkWinO()


    if len(b7)>=1 and k>=0:
        displayButton7(b7)
        k+=1


def button8Function():
    global k
    text=""
    global b8
    global thirdRow, secondColumn
    
    gridLocation="b8"
    if k<0:
        
        if k==-1:
            thirdRow+='x'
            secondColumn+="x"
            b8="x"
            displayButton8(b8)
            checkWinO()
            
            playComputer(gridLocation)
            

        elif k==-3:
            thirdRow+='o'
            secondColumn+="o"
            b8="o"# Player's Move
            displayButton8(b8)
            checkWinO()
            
            playComputer(gridLocation)
            
    if k>=0:
        
        if k%2==0:
            b8="x"
            checkWinO()


        elif k%2==1:
            b8='o'
            checkWinO()


    if len(b8)>=1 and k>=0:
        displayButton8(b8)
        k+=1

#Button9Function: is the command when the 9th button is clicked. When the button is clicked there are various scnarios when it can be clicked. -1 is alloted
# to a global variable 'k' when the computer is playing against the player and the player is 'x'. -3 is alloted to the global variable when the player is 'o'
#in the same case. After the user pressed the button, computer plays it's turn automatically by calling another function Computer vs Player and Player vs Player
#is differentiated by negative and positive allocations to the global vriable. When playing Player vs Player
# the global accumulator 'k' is checked if it is odd or even and 'x' and 'o' is alloted to variables based on that.
def button9Function():
    global k,gamesWonPlayer1, gamesWonPlayer2, thirdRow, thirdColumn,  b9
    gridLocation="b9"
    
    
    if k<0:
        
        if k==-1:
            thirdRow+='x'
            thirdColumn+="x"
            b9="x"
            displayButton9(b9)
            checkWinO()
            playComputer(gridLocation)

        elif k==-3:
            thirdRow+='o'
            thirdColumn+="x"
            b9="o"# Player's Move
            displayButton9(b9)
            checkWinO()
            playComputer(gridLocation)
            
    if k>=0:
        if k%2==0:
            b9='x'
            checkWinO()
        
        elif k%2==1:
            b9='o'
            checkWinO()
            
    if len(b9)>=1 and k>=0:
        displayButton9(b9)
        k+=1



def checkWinO():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, gamesWonPlayer1, gamesWonPlayer2, playerName1, playerName2, player1Mark, player2Mark, currentGame, numOfGames, computerMark,k
    global gamesWonPlayer, gamesWonComputer , numberOfGames
    if (((b1=="o") and (b2=="o") and (b3=="o"))or ((b1=="o" and b4=="o" and b7=="o")) or ((b4=="o") and (b5=="o") and (b6=="o")) or ((b7=="o") and (b8=="o") and (b9=="o")) or ((b1=="o") and (b5=="o") and (b9=="o")) or ((b3=="o") and (b5=="o") and (b7=="o")) or ((b2=="o") and (b5=="o") and (b8=="o")) or ((b3=="o") and (b6=="o") and (b9=="o"))) :
        print("HELLO WORLD, WINN")
        print("Number of games to be played",numOfGames)
        currentGame+=1
        print("Current Game Number",currentGame)
        if  player1Mark=="o":
            congratsPlayer1()
            gamesWonPlayer1=gamesWonPlayer1+1
            if currentGame<=numOfGames :
                newGame()
            if currentGame>numOfGames:
                if gamesWonPlayer1>gamesWonPlayer2:
                    winMatchPlayer1()
                elif gamesWonPlayer1<gamesWonPlayer2:
                    winMatchPlayer2()
                elif gamesWonPlayer1==gamesWonPlayer2:
                    tieMatch
                newMatch()
                
        elif  player2Mark=="o":
            print("WINN by",playerName2)
            congratsPlayer2()
            gamesWonPlayer2=gamesWonPlayer2+1
            
            if currentGame<=numOfGames :
                newGame()
            elif currentGame>numOfGames:
                
                if gamesWonPlayer1>gamesWonPlayer2:
                    winMatchPlayer1()
                elif gamesWonPlayer1<gamesWonPlayer2:
                    winMatchPlayer2()
                elif gamesWonPlayer1==gamesWonPlayer2:
                    tieMatch()
                    
                newMatch()

        elif computerMark=="o":
            congratsComputer()
            gamesWonComputer=gamesWonComputer+1
            
            if currentGame<=numOfGames :
                newGameC()
            elif currentGame>numOfGames:
                
                if gamesWonComputer>gamesWonPlayer:
                    winMatchComputer()
                elif gamesWonComputer<gamesWonPlayer:
                    winMatchPlayer()
                elif gamesWonComputer<gamesWonPlayer:
                    tieMatch()
                newMatch()

        elif playerMark=="o":
            congratsPlayer()
            gamesWonPlayer=gamesWonPlayer+1
            
            if currentGame<=numOfGames :
                newGameC()
            elif currentGame>numOfGames:
                
                if gamesWonComputer>gamesWonPlayer:
                    winMatchComputer()
                elif gamesWonComputer<gamesWonPlayer:
                    winMatchPlayer()
                elif gamesWonComputer<gamesWonPlayer:
                    tieMatch()
                    
                newMatch()

            
        
            
    
    elif (((b1=="x") and (b2=="x") and (b3=="x"))or ((b1=="x" and b4=="x" and b7=="x")) or ((b4=="x") and (b5=="x") and (b6=="x")) or ((b7=="x") and (b8=="x") and (b9=="x")) or ((b1=="x") and (b5=="x") and (b9=="x")) or ((b3=="x") and (b5=="x") and (b7=="x")) or ((b2=="x") and (b5=="x") and (b8=="x")) or ((b3=="x") and (b6=="x") and (b9=="x"))) :
        print("HELLO WORLD, WINN")
        currentGame+=1
        print("current game:",currentGame)
        if  player1Mark=="x":
            congratsPlayer1()
            gamesWonPlayer1=gamesWonPlayer1+1
            if currentGame<=numOfGames :
                newGame()
            elif currentGame>numOfGames:
                
                if gamesWonPlayer1>gamesWonPlayer2:
                    winMatchPlayer1()
                elif gamesWonPlayer1<gamesWonPlayer2:
                    winMatchPlayer2()
                elif gamesWonPlayer1==gamesWonPlayer2:
                    tieMatch()
                newMatch()
            

        elif player2Mark=="x":
            print("WINN by",playerName2)
            congratsPlayer2()
            gamesWonPlayer2=gamesWonPlayer2+1
            
            if currentGame<=numOfGames :
                newGame()
            if currentGame>numOfGames:
                
                if gamesWonPlayer1>gamesWonPlayer2:
                    winMatchPlayer1()
                    
                elif gamesWonPlayer1<gamesWonPlayer2:
                    winMatchPlayer2()
                elif gamesWonPlayer1==gamesWonPlayer2:
                    tieMatch
                newMatch()

        elif computerMark=="x":
            congratsComputer()
            gamesWonComputer=gamesWonComputer+1
            
            if currentGame<=numOfGames :
                newGameC()
            elif currentGame>numOfGames:
                
                if gamesWonComputer>gamesWonPlayer:
                    winMatchComputer()
                elif gamesWonComputer<gamesWonPlayer:
                    winMatchPlayer()
                elif gamesWonComputer<gamesWonPlayer:
                    tieMatch()
                    
                newMatch()

        elif playerMark=="x":
            congratsPlayer()
            
            gamesWonPlayer=gamesWonPlayer+1
            
            if currentGame<=numOfGames :
                newGameC()
            elif currentGame>numOfGames:
                
                if gamesWonComputer>gamesWonPlayer:
                    winMatchComputer()
                elif gamesWonComputer<gamesWonPlayer:
                    winMatchPlayer()
                elif gamesWonComputer<gamesWonPlayer:
                    tieMatch()
                    
                newMatch()
    
    elif (b1=='x' or b1=='o') and (b2=='x' or b2=='o') and (b3=='x' or b3=='o') and (b4=='x' or b4=='o') and (b5=='x' or b5=='o') and (b6=='x' or b6=='o') and (b7=='x' or b7=='o') and (b8=='x' or b8=='o') and (b9=='x' or b9=='o') and (k>0):
        string="player"
        tieGame(string)
        currentGame+=1
        if currentGame<=numOfGames :
            newGame()
        elif currentGame>numOfGames:
                
            if gamesWonPlayer1>gamesWonPlayer2:
                winMatchPlayer1()
                
            elif gamesWonPlayer1<gamesWonPlayer2:
                winMatchPlayer2()
            elif gamesWonPlayer1==gamesWonPlayer2:
                tieMatch()
            newMatch()
        


    elif ((len(b1)>0) and (len(b2)>0) and (len(b3)>0) and (len(b4)>0) and (len(b5)>0) and (len(b6)>0) and (len(b7)>0) and (len(b8)>0) and (len(b9)>0)) and (k<0):
        string="computer"
        tieGame(string)
        currentGame+=1
        if currentGame<=numOfGames :
            newGameC()
        elif currentGame>numOfGames:
                
            if gamesWonComputer>gamesWonPlayer:
                winMatchComputer()
            elif gamesWonComputer<gamesWonPlayer:
                winMatchPlayer2()
            elif gamesWonComputer<gamesWonPlayer:
                tieMatch()
                
            newMatch()

    elif (currentGame>numberOfGames) and k<0:
        
        if gamesWonComputer>gamesWonPlayer:
            winMatchComputer()
        elif gamesWonComputer<gamesWonPlayer:
            winMatchPlayer2()
        elif gamesWonComputer==gamesWonPlayer:
            tieMatch()
        newMatch()

    
        
    else:
        print(b1,b2,b3)
        print("OH NO")
#----------------------------------------------------------------------------------------------------------------------------


def parody(location):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    if len(b1)<=0:
        displayButton1(location)
        b1=location
        checkWinO()
        
    elif len(b3)<=0:
        displayButton3(location)
        b3=location
        checkWinO()
        
    elif len(b7)<=0:
        displayButton7(location)
        b7=location
        checkWinO()
        
    elif len(b9)<=0:
        displayButton9(location)
        b9=location
        checkWinO()
        

    elif len(b5)<=0:
        displayButton5(location)
        b5=location
        checkWinO()
        
        
    elif len(b2)<=0:
        
        displayButton2(location)
        b2=location
        checkWinO()
        
    elif len(b4)<=0:
         print("computer's move is b4")

         
         displayButton4(location)
         b4=location
         checkWinO()
    elif len(b6)<=0 :
        
        
        displayButton6(location)
        b6=location
        checkWinO()

    elif len(b8)<=0 :
        displayButton8(location)
        b8=location
        checkWinO()
        
    
#New Game Function: After a game is finished, this function creates another game for Player vs Player Mode
def newGame():
    text='gameOver'
    gameFrame.place_forget() 
    gameFrame.place(x=0, y=0)
    clearVariables(text)    #Clears variables before heading to the game.
    gamePlayerVsPlayer()    #Gameplay function is called

#New Game Function: After a game is finished, this function creates another game for Player vs Computer Mode
def newGameC():
    text=''
    gameFrame.place_forget() 
    gameFrame.place(x=0, y=0)
    clearVariables(text)
    playerVsComputer()

#Clears the varibles based on the function called. This is necessary beacuse it might interfere with the new game values.
def clearVariables(text):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, k, gamesWonPlayer1, gamesWonPlayer2, gamesWonComputer, gamesWonPlayer
    
    k=0
    b1=''
    b2=''
    b3=''
    b4=''
    b5=''
    b6=''
    b7=''
    b8=''
    b9=''
    if text=="gameOver":
        print("GREAT")

    elif text=="cgameOver":
        gamesWonPlayer=0
        gamesWonComputer=0
    else:
        gamesWonPlayer1=0
        gamesWonPlayer2=0
        
    
    
#playComputer Function: This the computer's move(AI) based on the player's move. There are various possiblities.
def playComputer(moveLocation):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, computerTurn, k
    global firstRow,secondRow,thirdRow
    global firstColumn, secondColumn, thirdColumn
    
    print("COMPUTER TURN",computerTurn)
    if computerTurn%2==0:
        computerMove="x"
    else:
        computerMove="o"
    print("computer move is ",computerMove)
    print(" Move Location is",moveLocation)

    if len(b5)<=0:
        print()
        print("Computer plays B5")
        label=tk.Label(gameFrame, text=computerMove, fg="black", bg="white",font="Arial 22 bold")
        label.place(x=100,y=200, width=50, height=50)
        b5=computerMove
        checkWinO()
        #b5="done"

    elif len(firstRow)>=2:
        if len(b1)<=0:
            displayButton1(computerMove)
            b1=computerMove
            checkWinO()
            #b1="done"
            firstRow=""
            
        elif len(b2)<=0:
            displayButton2(computerMove)
            b2=computerMove
            checkWinO()
            #b2="done"
            firstRow=""
            
        elif len(b3)<=0:
            displayButton3(computerMove)
            b3=computerMove
            checkWinO()
            #b3="done"
            firstRow=""
            
        else:
            print()
            print("sorry sir nothing to do")
            parody(computerMove)

    elif len(secondRow)>=2:
        if len(b4)<=0:
            displayButton4(computerMove)
            b4=computerMove
            checkWinO()
            b4="done"
            secondRow=""

        elif len(b5)<=0:
            displayButton5(computerMove)
            b5=computerMove
            checkWinO()
            #b5="done"
            secondRow=""
        elif len(b6)<=0:
            displayButton6(computerMove)
            b6=computerMove
            checkWinO()
            #b6="done"
            secondRow=""
        
        else:
            print()
            print("sorry sir nothing to do")
            parody(computerMove)

    elif len(thirdRow)>=2:
        if len(b7)<=0:
            displayButton7(computerMove)
            b7=computerMove
            checkWinO()
            #b7="done"
            thirdRow=""
        elif len(b8)<=0:
            displayButton8(computerMove)
            b8=computerMove
            checkWinO()
            #b8="done"
            thirdRow=""
        elif len(b9)<=0:
            displayButton9(computerMove)
            b9=computerMove
            checkWinO()
            #b9="done"
            thirdRow=""

        else:
            print()
            print("sorry sir nothing to do")
            parody(computerMove)

    elif len(firstColumn)>=2:
        if len(b1)<=0:
            displayButton1(computerMove)
            b1=computerMove
            checkWinO()
            #b1="done"
            firstColumn=""
        
        elif len(b4)<=0:
            displayButton4(computerMove)
            b4=computerMove
            checkWinO()
            #b4="done"
            firstColumn=""

        elif len(b7)<=0:
            displayButton7(computerMove)
            b7=computerMove
            checkWinO()
            #b7="done"
            firstColumn=""
        else:
            print()
            print("sorry sir nothing to do")
            parody(computerMove)

    elif len(secondColumn)>=2:
        if len(b2)<=0:
            displayButton2(computerMove)
            b2=computerMove
            checkWinO()
            #b2="done"
            secondColumn=""
        
        elif len(b5)<=0:
            displayButton5(computerMove)
            b5=computerMove
            checkWinO()
            #b5="done"
            secondColumn=""

        elif len(b8)<=0:
            displayButton8(computerMove)
            b8=computerMove
            checkWinO()
            secondColumn=""

        else:
            print()
            print("sorry sir nothing to do")
            parody(computerMove)

    elif len(thirdColumn)>=2:
        if len(b3)<=0:
            displayButton3(computerMove)
            b3=computerMove
            checkWinO()
            thirdColumn=""
        
        elif len(b6)<=0:
            displayButton5(computerMove)
            b6=computerMove
            checkWinO()
            thirdColumn=""

        elif len(b9)<=0:
            displayButton9(computerMove)
            b9=computerMove
            checkWinO()
            thirdColumn=""

        else:
            print()
            print("sorry sir nothing to do")
            parody(computerMove)
             
    elif moveLocation=="b1" or moveLocation=="b3" or moveLocation=="b7" or moveLocation=="b9":
        if len(b2)<=0 :
            displayButton2(computerMove)
            b2=computerMove
            checkWinO()
            
        elif len(b4)<=0:
             print("computer's move is b4")
             displayButton4(computerMove)
             b4=computerMove
             checkWinO()
             
        elif len(b6)<=0 :
            
            displayButton6(computerMove)
            b6=computerMove
            checkWinO()

        elif len(b8)<=0 :
            displayButton8(computerMove)
            b8=computerMove
            checkWinO()

        else:
            print()
            print("sorry sir nothing to do")
            parody(computerMove)
    

    elif moveLocation=="b2" or moveLocation=="b4" or moveLocation=="b6" or moveLocation=="b8":
        if len(b1)<=0:
            displayButton1(computerMove)
            b1=computerMove
            checkWinO()
            
        elif len(b3)<=0:
            displayButton3(computerMove)
            b3=computerMove
            checkWinO()
            
        elif len(b7)<=0:
            displayButton7(computerMove)
            b7=computerMove
            checkWinO()
            
        elif len(b9)<=0:
            displayButton9(computerMove)
            b9=computerMove
            checkWinO()
            

    elif moveLocation=="computer":
        
            displayButton5(computerMove)
            b5=computerMove
            checkWinO()
            
    

    print("IM BACK")

#This function is the command when the computerButton is clicked. Textfields for names and number of games are created. Then the inputValidation is called to validate the values entered
def computerButton():
    global nameTextfield, numberOfGamesTextfield2
    nameLabel=tk.Label(frame1, text="Player Name:")
    nameLabel.place(x=25, y=100, width=100, height=30)
    nameTextfield=tk.Entry(frame1, width=15)
    nameTextfield.place(x=135, y=100)
    numOfGamesLabel=tk.Label(frame1,text="Number of Games(1,3,5)")
    numOfGamesLabel.place(x=0,y=160)
    numberOfGamesTextfield2=tk.Entry(frame1, width=7)
    numberOfGamesTextfield2.place(x=135, y=160)
    okButton=tk.Button(frame1, text='ok', command=inputValidationButtonC)
    okButton.place(x=25, y=250)
    

def inputValidationButtonC():
    global nameTextfield, playerName, numberOfGamesTextfield2, numberOfGames
    if len(str(numberOfGamesTextfield2.get()))<1:
        displayError()
    playerName=str(nameTextfield.get())
    numberOfGames=int(numberOfGamesTextfield2.get())
    AI="computer"
    if ((numberOfGames==1) or (numberOfGames==3) or (numberOfGames==5))and (len(playerName)>1) :
        print(playerName)
        print(AI)
        frame1.place_forget() # Hide the first frame
        gameFrame.place(x=0, y=0)
        playerVsComputer()
    else:
        displayError()
        


def inputValidation():
    global nameTextfield1, nameTextfield2, playerName1, playerName2, numberOfGamesTextfield, numOfGames
    if len(str(numberOfGamesTextfield.get()))<1:
        displayError()
    numOfGames=int(numberOfGamesTextfield.get())
    playerName1=str(nameTextfield1.get())
    playerName2=str(nameTextfield2.get())
    if ((numOfGames==1) or (numOfGames==3) or (numOfGames==5)) and ((len(playerName1)>=1 and len(playerName2)>=1)):
        print(playerName1)
        print(playerName2)
        print("Number of games to be played",numOfGames)
        frame1.place_forget() 
        gameFrame.place(x=0, y=0)
        gamePlayerVsPlayer()
        
    else:
        displayError()

#This function is the command when the playerButton is clicked. Textfields for names and number of games are created. Then the inputValidation is called to validate the values entered
def playerButton():
    global nameTextfield1, nameTextfield2,numberOfGamesTextfield
    nameLabel1=tk.Label(frame1, text="Player 1 Name:")
    nameLabel1.place(x=25, y=100, width=100, height=30)
    
    nameTextfield1=tk.Entry(frame1, width=15)
    nameTextfield1.place(x=135, y=100)
    
    numberOfGamesTextfield=tk.Entry(frame1, width=7)
    numberOfGamesTextfield.place(x=135, y=200)
    
    numOfGamesLabel=tk.Label(frame1,text="Number of Games(1,3,5)")
    numOfGamesLabel.place(x=0,y=200)
    
    nameLabel2=tk.Label(frame1, text="Player 2 Name:")
    nameLabel2.place(x=25, y=150, width=100, height=30)

    
    nameTextfield2=tk.Entry(frame1, width=15)
    nameTextfield2.place(x=135, y=150)
    
    okButton=tk.Button(frame1, text='ok', command=inputValidation)
    okButton.place(x=25, y=250)

#This is the main gameplay(which controls the flow of the game) for the AI mode. 
def playerVsComputer():
    global playerName,nameTextfield, playerMark, computerMark, computerTurn, numberOfGames
    global currentGame
    global gamesWonPlayer
    global gamesWonComputer
    global k
    
    player=r.randint(0,1)

    if player==1:
        
        playerMark="x"
        computerMark="o"
        computerTurn=1
        print(playerName," Mark is",playerMark)
        print("Computer Mark is",computerMark)
    elif player==0:
        
        playerMark="o"
        computerMark="x"
        computerTurn=0
        print(playerName," Mark is",playerMark)
        print("Computer Mark is",computerMark)

    text='computer'


    
    if computerTurn%2==0: #Computer is x
        checkWinO()
        k=-3
        createButtons()
        playComputer(text)
        k=-3

    elif computerTurn%2==1: #Computer is o
        checkWinO()
        k=-1
        createButtons()
        k=-1

    
    string="Game:"+str(currentGame)
    gameNumberLabel=tk.Label(gameFrame,text=string, fg="black", font="Arial 10")
    gameNumberLabel.place(x=25,y=70)

    gamesLeft2=numberOfGames-currentGame
    print(gamesLeft2," GAMES ARE LEFT")
    string="Games Left: "+str(gamesLeft2)
    gamesLeftLabel=tk.Label(gameFrame, text=string,fg="black",font="Arial 15 bold")
    gamesLeftLabel.place(x=25,y=600)


    string="Games won by "+playerName+":"+str(gamesWonPlayer)
    gamesWonPlayerLabel=tk.Label(gameFrame,text=string,fg="black",font="Arial 10")
    gamesWonPlayerLabel.place(x=25,y=525)

    string="Games won by "+"computer"+":"+str(gamesWonComputer)
    gamesWonComputerLabel=tk.Label(gameFrame,text=string,fg="black",font="Arial 10")
    gamesWonComputerLabel.place(x=25,y=550)

    string1=playerName+"- "+playerMark
    string2="Computer- "+computerMark
    playerNameLabel=tk.Label(gameFrame, text=string1,fg="black",font="Arial 15 bold")
    playerNameLabel.place(x=25,y=400)

    computerNameLabel=tk.Label(gameFrame,text=string2,fg="black",font="Arial 15 bold")
    computerNameLabel.place(x=25,y=425)

#This is the main gameplay(which controls the flow of the game) for the playerVsPlayer mode. 
def gamePlayerVsPlayer():
    global playerName1, playerName2, player1Mark, player2Mark, currentGame, gamesWonPlayer1, gamesWonPlayer2, gamesLeft, numOfGames
    
    player1=r.randint(0,1)

    if player1==1:
        
        player1Mark="x"
        player2Mark="o"
        print(playerName1," Mark is",player1Mark)
        print(playerName2," Mark is",player2Mark)
    elif player1==0:
        
        player1Mark="o"
        player2Mark="x"
        print(playerName1," mark is",player1Mark)
        print(playerName2," mark is",player2Mark)

    

    if player1Mark=="x" :
        player1MarkLabel=tk.Label(gameFrame, text="  -  x",fg="black",font="Arial 13 bold")
        player1MarkLabel.place(x=75,y=400)

        player2MarkLabel=tk.Label(gameFrame, text="  -  o",fg="black",font="Arial 13 bold")
        player2MarkLabel.place(x=75,y=430)
    elif player1Mark=="o":
        player1MarkLabel=tk.Label(gameFrame, text="  -  o",fg="black",font="Arial 13 bold")
        player1MarkLabel.place(x=75,y=400)

        player2MarkLabel=tk.Label(gameFrame, text="  -  x",fg="black",font="Arial 13 bold")
        player2MarkLabel.place(x=75,y=430)

    createButtons()

    gamesLeft=numOfGames-currentGame
    print(gamesLeft," GAMES ARE LEFT")
    string="Games Left: "+str(gamesLeft)
    gamesLeftLabel=tk.Label(gameFrame, text=string,fg="black",font="Arial 15 bold")
    gamesLeftLabel.place(x=25,y=600)
    string1=playerName1+"-"+player1Mark
    string2=playerName2+"-"+player2Mark
    player1NameLabel=tk.Label(gameFrame, text=string1,fg="black",font="Arial 15 bold")
    player1NameLabel.place(x=25,y=400)

    player2NameLabel=tk.Label(gameFrame,text=string2,fg="black",font="Arial 15 bold")
    player2NameLabel.place(x=25,y=425)

    print("Current Game in GUI function:",currentGame)
    string="Game:"+str(currentGame)
    gameNumberLabel2=tk.Label(gameFrame,text=string, fg="black", font="Arial 10")
    gameNumberLabel2.place(x=25,y=70)

    string="Games won by "+playerName1+":"+str(gamesWonPlayer1)
    gamesWonPlayer1Label=tk.Label(gameFrame,text=string,fg="black",font="Arial 10")
    gamesWonPlayer1Label.place(x=25,y=525)

    string="Games Won by "+playerName2+":"+str(gamesWonPlayer2)
    gamesWonPlayer2Label=tk.Label(gameFrame,text=string,fg="black",font="Arial 10 ")
    gamesWonPlayer2Label.place(x=25,y=550)


    #createGUI()

def newMatch():
    text=""
    global currentGame
    clearVariables(text)
    gameFrame.place_forget() # Hide the first frame
    frame1.place(x=0, y=0)
    currentGame=1

#9 buttons are created thereby creating a grid for the game. When clicked it's command(another function) is called. Other GUI such as title, restart  button, exit button
# are also created as they are common for both the modes.
def createButtons():

    global currentGame, gamesWonPlayer, gamesWonComputer, computerTurn, k
    
    titleLabel=tk.Label(gameFrame, text="TIC TAC TOE", fg="black",bg="blue", font="Arial 19 bold")
    titleLabel.place(x=25,y=25)
    
    button1=tk.Button(gameFrame, text="", command=button1Function)
    button1.place(x=25, y=100, width=50, height=50)

    button2=tk.Button(gameFrame, text="", command=button2Function)
    button2.place(x=100, y=100, width=50, height=50)

    button3=tk.Button(gameFrame, text="", command=button3Function)
    button3.place(x=175, y=100, width=50, height=50)

    button4=tk.Button(gameFrame, text="", command=button4Function)
    button4.place(x=25, y=200, width=50, height=50)

    button5=tk.Button(gameFrame, text="", command=button5Function)
    button5.place(x=100, y=200, width=50, height=50)

    button6=tk.Button(gameFrame, text="", command=button6Function)
    button6.place(x=175, y=200, width=50, height=50)

    button7=tk.Button(gameFrame, text="", command=button7Function)
    button7.place(x=25, y=300, width=50, height=50)

    button8=tk.Button(gameFrame, text="", command=button8Function)
    button8.place(x=100, y=300, width=50, height=50)

    button9=tk.Button(gameFrame, text="", command=button9Function)
    button9.place(x=175, y=300, width=50, height=50)

    dividerLabel=tk.Label(gameFrame, text="---------------------", fg='black', font='Arial 22 bold')
    dividerLabel.place(x=25, y=155)

    dividerLabel=tk.Label(gameFrame, text="---------------------", fg='black', font='Arial 22 bold')
    dividerLabel.place(x=25, y=255)

    quitButton=tk.Button(gameFrame, text="x", fg="black", bg="red", font="Arial 10 bold", command=quitApp)
    quitButton.place(x=275, y=25, width=25, height=25)


    endGameButton=tk.Button(gameFrame,text="END CURRENT GAME",fg="black",font="Arial 8 ",command=newGame)
    endGameButton.place(x=25,y=650)

    restartGameButton=tk.Button(gameFrame,text="RESTART MATCH", fg="black",font="Arial 8 ",command=newMatch)
    restartGameButton.place(x=150,y=650)
        

def tieGame(text):
    message=tk.messagebox.showinfo('TIE','Its a tie game')
    if text=="player":
        newGame()
    else:
        newGameC()

def tieMatch():
    message=tk.messagebox.showinfo('TIE','Its a tie match')

def winMatchPlayer1():
    message=tk.messagebox.showinfo('Congratulations','Player 1 has won the match')

def winMatchPlayer2():
    message=tk.messagebox.showinfo('Congratulations','Player 2 has won the match')

def winMatchComputer():
    message=tk.messagebox.showinfo('Congratulations','Computer has won match. Computer can do this all day')

def winMatchPlayer():
    message=tk.messagebox.showinfo('Congratulations','Player has won match')
    
def displayError():
    message=tk.messagebox.showerror('ERROR 404','ERROR')

def congratsPlayer1():
    
    message=tk.messagebox.showinfo('Congratulations','Player 1 has won the current game')

def congratsPlayer2():
    
    message=tk.messagebox.showinfo('Congratulations','Player 2 has won the current game')

def congratsComputer():
    
    message=tk.messagebox.showinfo('Congratulations','Computer has won the current game. Computer can do this all day')

def congratsPlayer():
    
    message=tk.messagebox.showinfo('Congratulations','Player has won the current game')


def quitApp():
    window2.destroy()

#--------------------------
numOfGames=5
counter=0
width=300
height=675
player1=0
player2=0
xy=''

global window2

    
window2= tk.Tk()
window2.title(" TIC TAC TOE")
window2.minsize(width,height)

gameFrame=tk.Frame(window2, width=width, height=height)

frame1=tk.Frame(window2, width=width, height=height)
frame1.place(x=0, y=0)

buttonComputer=tk.Button(frame1, text="Player vs Computer", command=computerButton)
buttonPlayer=tk.Button(frame1, text="Player vs Player", command=playerButton)

buttonComputer.place(x=25, y=25, width=110, height=30)
buttonPlayer.place(x=155, y=25,width=110, height=30)







