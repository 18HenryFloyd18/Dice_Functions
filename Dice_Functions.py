import random #Import The Random Function
import math #Import The Math Function

diceList = [1,2,3,4,5,6] # Create A List 
comp_Wins = 0 #Create A List For The Wins To Be Stored In For The Player And The Computer
player_Wins = 0
def diceRoller():
  random.choice(diceList)

def score():
  if(randomComp > randomPlayer):# If The Computer Won Add 1 To The Overall Score For The Computer's Variable
        comp_Wins = comp_Wins + 1
        print("Computer Score:",comp_Wins)# Print The Computer's Score And Also The Player's Score
        print("Player's Score:",player_Wins)
      elif(randomComp == randomPlayer):#IIf It Is Equal To Both Numbers Then Don't Do Anything But Display The Score
        print("Computer's Score:",comp_Wins)
        print("Player's Score:",player_Wins)
      else: # If The Player Won The Round Add One To Their Score And Then Display The Current Score
       player_Wins = player_Wins + 1
        print("Computer's Score:",comp_Wins)
        print("Player's Score:",player_Wins)
    if(player_Wins > comp_Wins):# if The Player Won Then Give Them Kudos OtherWise Tell Them Better Luck Next Time
      print("You Won Congrats!")
      else:
      print("The Computer Won This Game, Better Luck Next Game") 



print("Welcome To Dice Game!") #Welcome The Player
print("Game Rules: You And The Computer Roll A Dice, Whoever Has The Highest Dice Number Wins The Round. First To Three Wins Takes The Victory!") # Explain The Rules

trynaGame = input("If You Would Like To Play, Type The Word 'Enter':") #Ask If They Would Like To Play The Game

if(trynaGame != "Enter" and trynaGame != "enter"):
  print("To Begin The Game Please Type The Word 'Enter', If You Don't Want To Play Have A Nice Day!") # If The Input Is Fine, Begin The Game. If It Is Not Then Tell Them How To Play
  trynaGame = False # If You Don't Enter 'Enter' Then The Game Will Ask You To Type Enter
else:
  trynaGame = True # Else Then Continue With The Code



while trynaGame: # While Either Of The Players Do Not Have 3 Wins Iterate The Loop
    while(player_Wins < 3 and comp_Wins < 3):
      
      randomComp = diceRoller() # Get A Random Number For The Dice
      print("The Number That The Computer Rolled Was",randomComp) # Tell The User What The Number Is For The Computer

      wannaPlay = str(input("Type 'Roll' To Roll The Dice:")) # Ask The User To Roll Their Dice
      if(wannaPlay == "Roll" or wannaPlay == "roll"): # If The Answer Is Correct let Them Play Else  Then Tell Them How To Play It
        None
      else:
        print("If You Want To Play Please Enter 'Enter'")# Tell Them How To Play
        trynaGame = False
        break# Break Out Of The Loop

      randomPlayer = diceRoller() # Get A Random Number For The User
      print("The Number That You Rolled Was",randomPlayer) #Print Their Number

      if(randomComp > randomPlayer): #If The Computer's Number Is Higher Than The Players Display That The Computer Won The Round
        print("The Computer Won This Round!")
      elif(randomComp == randomPlayer):#If The Computer's Number Is Equal To The Player's Redo The Round
        print("You And The Computer Got The Same Numbers, Let's Redo The Round")
      else:# Anything Else Means That The Player Won The Round And Display That
        print("You Won This Round!")
      
      score()
    
    break #Break Out Of The Loop
    
    




