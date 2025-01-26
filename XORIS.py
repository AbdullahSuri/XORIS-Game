#importing modules
import random
import os

#setting board dimensions
YSIZE=11
XSIZE=11

#creating empty list for board
board=[]

#defining alphabets for column headings
alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#defining checkers 
Checkers=["X","O","R","I","S"]

#defining empty positions on the board(will be used later to check for a draw)
emptypositions=YSIZE*XSIZE

#creating a function to print the board
def printboard():
    os.system("clear")
    print(" ", end="")
    for columns in range(XSIZE):
        print("   "+alphabets[columns], end="")


    print("\n  +" + "---+" * XSIZE)    

    for rows in range(YSIZE):
        if (rows < 10):
            print(" " + str(rows)+'|', end="")
        else:
            print(str(rows)+'|', end="")

        for columns in range(XSIZE):
            print(" " + board[rows][columns] + ' |', end="")
        print("\n  +"+"---+"*XSIZE)

#creating function that checks after every move if the player connects 4 and wins
def checkconnect4(row_cord, col_cord):  
    global win
    if (col_cord+4) <= XSIZE:
        if board[row_cord][col_cord+1]== i and board[row_cord][col_cord+2]== i and board[row_cord][col_cord+3]== i:
                win=True
    if (col_cord+3)<=XSIZE and col_cord-1>=0:
        if board[row_cord][col_cord-1]== i and board[row_cord][col_cord+1]== i and board[row_cord][col_cord+2]== i:
                win=True
    if (col_cord+2)<=XSIZE and col_cord-2>=0 :
        if board[row_cord][col_cord-2]== i and board[row_cord][col_cord-1]== i and board[row_cord][col_cord+1]== i:
                win=True
    if (col_cord)+1<=XSIZE and col_cord-3>=0:
        if board[row_cord][col_cord-3]== i and board[row_cord][col_cord-2]== i and board[row_cord][col_cord-1]== i:
                win=True
                            
                            
    if (row_cord+4) <= YSIZE:
        if board[row_cord+1][col_cord]== i and board[row_cord+2][col_cord]== i and board[row_cord+3][col_cord]== i:
                win=True
    if (row_cord+3)<=YSIZE and row_cord-1>=0:
        if board[row_cord-1][col_cord]== i and board[row_cord+1][col_cord]== i and board[row_cord+2][col_cord]== i:
                win=True
    if (row_cord+2)<=YSIZE and row_cord-2>=0 :
        if board[row_cord-2][col_cord]== i and board[row_cord-1][col_cord]== i and board[row_cord+1][col_cord]== i:
                win=True
    if (row_cord+1)<=YSIZE and row_cord-3>=0:
        if board[row_cord-3][col_cord]== i and board[row_cord-2][col_cord]== i and board[row_cord-1][col_cord]== i:
                win=True
                            
                            
    if 3<=row_cord<=YSIZE-1 and 0<=col_cord<=XSIZE-4:
        if board[row_cord-1][col_cord+1]== i and board[row_cord-2][col_cord+2]== i and board[row_cord-3][col_cord+3]== i:
                win=True
    if 2<=row_cord<=YSIZE-2 and 1<=col_cord<=XSIZE-3:
        if board[row_cord+1][col_cord-1]== i and board[row_cord-1][col_cord+1]== i and board[row_cord-2][col_cord+2]== i:
                win=True        
    if 1<=row_cord<=YSIZE-3 and 2<=col_cord<=XSIZE-2:
        if board[row_cord+2][col_cord-2]== i and board[row_cord+1][col_cord-1]== i and board[row_cord-1][col_cord+1]== i:
                win=True        
    if 0<=row_cord<=YSIZE-4 and 3<=col_cord<=XSIZE-1:
        if board[row_cord+3][col_cord-3]== i and board[row_cord+2][col_cord-2]== i and board[row_cord+1][col_cord-1]== i:
                win=True                  

                            
    if 0<=row_cord<=YSIZE-4 and 0<=col_cord<=XSIZE-4:
        if board[row_cord+1][col_cord+1]== i and board[row_cord+2][col_cord+2]== i and board[row_cord+3][col_cord+3]== i:
                win=True
    if 1<=row_cord<=YSIZE-3 and 1<=col_cord<=XSIZE-3:
        if board[row_cord-1][col_cord-1]== i and board[row_cord+1][col_cord+1]== i and board[row_cord+2][col_cord+2]== i:
                win=True        
    if 2<=row_cord<=YSIZE-2 and 2<=col_cord<=XSIZE-2:
        if board[row_cord-2][col_cord-2]== i and board[row_cord-1][col_cord-1]== i and board[row_cord+1][col_cord+1]== i:
                win=True 
    if 3<=row_cord<=YSIZE-1 and 3<=col_cord<=XSIZE-1:
        if board[row_cord-3][col_cord-3]== i and board[row_cord-2][col_cord-2]== i and board[row_cord-1][col_cord-1]== i:
                win=True 

#explaining game to players
print("WELCOME TO THE GAME XORIS!!!")
print(" ")
print("-This game can have 2,3,4 or 5 players")
print("-Players take turns and place their checker into a cell of choice")
print("-The form of the input is: A9, C2, K10, etc")
print("-A player wins when they have successfully managed to place 4 checkers in horizontal, vertical or diagonal sequence before all other players")
print(" ")

while True:
    numofplayers1=input("enter the number of players: ")      #taking input of number of players
    if (numofplayers1.isdigit()) == False:
        print("please enter an integer")
    else:
        numofplayers=int(numofplayers1)
        if numofplayers<=1 or numofplayers>5:
            print('This game can have 2,3,4 or 5 players')
        else:
            newcheckers=Checkers[0:numofplayers]             #creating a list corresponding with the number of players
            break

#setting board dimensions to 11X11 if 2 players and setting to board dimensions to 15X15 if more than 2 players
if numofplayers==2:
    XSIZE+=0 
    YSIZE+=0
else:
    XSIZE+=4
    YSIZE+=4

#randomizing the order of players 
random.shuffle(newcheckers)

#Assigning players their numbers and checkers
for i in range(numofplayers):
    print('Player',i+1,'your checker is', newcheckers[i])

#creating board
for rows in range(YSIZE):
    rowlist=[]
    for columns in range (XSIZE):
        rowlist.append(' ')
    board.append(rowlist)    

#invoking function to print the board 
printboard()


#setting game states
draw = False
win = False


while draw==False and win==False:           #loop runs while condition is not met 
    for i in newcheckers:                   #loop repeats for every checker being used in the game
        if win==False and draw==False:      #ensures game ends as soon as their is a draw or a win
                while True:                 #loop runs until valid input is given
                    input_cord = input("Player "+str(newcheckers.index(i)+1)+' please enter the box where you want to place your checker '+ i+':')   #creating prompt to take input 
                    input_cord = input_cord.capitalize()
                    input_cord_copy = input_cord[1:]
                        
                
                    #input validation (done in if and elif statements)
                    if (len(input_cord) < 2 or len(input_cord) > 3 or (input_cord[0].isdigit()) or not(input_cord_copy.isdigit()) or not(int(input_cord_copy) < YSIZE) or not(ord("A") <= ord(input_cord[0])) or not(ord(input_cord[0]) <= ((ord("A")) + XSIZE - 1))):
                        print("Invalid Input. Please try again.")
                    elif (board[int(input_cord_copy)][int(ord(input_cord[0]) - 65)] != " "):
                        print("Go again! This box is already taken")
                    else:   
                        row_cord = int(input_cord_copy)           #Taking input of rows and columns and placing the checker on the board
                        col_cord = int(ord(input_cord[0]) - 65)
                        board[row_cord][col_cord] = i
                        emptypositions-=1  
                        
                        printboard()

                        #invoking function that checks after every move if the player connects 4 and wins
                        checkconnect4(row_cord, col_cord)
                        
                        #checking after every move if the players draw
                        if emptypositions==0:
                            draw=True    
                        
                        #Prints respective message for win or draw
                        if win==True:
                            print("PLAYER", str(newcheckers.index(i)+1), "WINS!!")
                        if draw==True:
                            print("THE GAME ENDS AS A DRAW!!!")

                        break;