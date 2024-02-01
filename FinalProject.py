import random


class ConnectFour(object):

   
   #empty constructor
   def __init__(self):
      self.gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]
      

   def instructions(self):
      print("Welcome to Connect Four")
      print(" O = BLUE CHIP ")
      print(" X = RED CHIP ")
      
      print("***********************************************************")
      print("Instructions...\n")
      print("Try to build a row of four chips either vertically, horizontally,")
      print("or diagonally either left to right or right to left. The challenge is to")
      print("do this before your opponent does the same.")
      print("To pick a space, you have to pick a coordinate using the")
      print("following format...")
      print("[column][row] EX: A5 or B5")
      print("***********************************************************")
      print("GOOD LUCK PLAYING!!")

   '''   
   Prints the game board -> a 6 x 7 table
   Prints the letters corresponding to each column
   Prints the numbers corresponding to each row
   '''  
   def printGameBoard(self):
      rows = 6
      columns = 7
      print("\n     A    B    C    D    E    F    G  ", end="")
      for x in range(rows):
         print("\n   +----+----+----+----+----+----+----+")
         print(x, " |", end="")
         for y in range(columns):
            if(self.gameBoard[x][y] == "O"):
               print("", self.gameBoard[x][y], end=" |")
            elif(self.gameBoard[x][y] == "X"):
               print("", self.gameBoard[x][y], end=" |")
            else:
               print(" ", self.gameBoard[x][y], end="  |")
      print("\n   +----+----+----+----+----+----+-----+")
      
   '''   
   changes the array(gameBoard) to mark the space user chooses
   @param spacePicked is a the space the user chose
   @param turn is the space
   '''        
   def modifyBoard(self, spacePicked, turn,):
      self.gameBoard[spacePicked[0]][spacePicked[1]] = turn
      
      
   '''   
   Checks if the user has won by checking the position of the markers-> checks that the marker 
   is 4 spaces in a row either horizontally, vertically, and diagonally.
   @param marker is a the maker of the user playing the game 
   '''    
   def checkForWinner(self, marker):
      rows = 6 #y
      columns = 7 #x
      
      #Check horizontal spaces
      for y in range(columns - 3):
         for x in range(rows):
            if self.gameBoard[x][y] == marker and self.gameBoard[x][y+1] == marker and self.gameBoard[x][y+2] == marker and self.gameBoard[x][y+3] == marker:
               print("\nGame over!!", marker, "wins! Thanks for playing :)")
               return True

      #Check vertical spaces
      for y in range(columns):
         for x in range(rows - 3):
            if self.gameBoard[x][y] == marker and self.gameBoard[x+1][y] == marker and self.gameBoard[x+2][y] == marker and self.gameBoard[x+3][y] == marker:
               print("\nGame over!!", marker, "wins! Thanks for playing :)")
               return True

      #check diagonally /
      for y in range(columns - 3):
         for x in range(rows - 3):
            if self.gameBoard[x][y] == marker and self.gameBoard[x+1][y+1] == marker and self.gameBoard[x+2][y+2] == marker and self.gameBoard[x+3][y+3] == marker:
               print("\nGame over!!", marker, "wins! Thanks for playing :)")
               return True

      #Check diagonnally \
      for y in range(columns - 3):
         for x in range(3, rows):
            if self.gameBoard[x][y] == marker and self.gameBoard[x-1][y+1] == marker and self.gameBoard[x-2][y+2] == marker and self.gameBoard[x-3][y+3] == marker:
               print("\nGame over!!", marker, "wins! Thanks for playing :)")
               return True
      return False
      
   '''   
   takes in userInput for the coordinate and parses it into an integer 
   @param userInput is a the string the user playing the game inputs for the coordinate 
   ''' 
   def coordinateParser(self, userInput):
      coordinate = [None] * 2
      if(userInput[0] == "A" or userInput[0] == "a" ):
         coordinate[1] = 0
      elif(userInput[0] == "B" or userInput[0] == "b" ):
         coordinate[1] = 1
      elif(userInput[0] == "C" or userInput[0] == "c" ):
         coordinate[1] = 2
      elif(userInput[0] == "D" or userInput[0] == "d" ):
         coordinate[1] = 3
      elif(userInput[0] == "E" or userInput[0] == "e" ):
         coordinate[1] = 4
      elif(userInput[0] == "F" or userInput[0] == "f" ):
         coordinate[1] = 5
      elif(userInput[0] == "G" or userInput[0] == "g" ):
         coordinate[1] = 6
      else:
         print("Invalid")
      coordinate[0] = int(userInput[1])
      return coordinate

   '''   
   Determines if the position the user chose is taken or not
   @param coordinatePicked is the coordinate the user chose. 
   '''    
   def isSpaceAvailable(self, coordinatePicked):
      if(self.gameBoard[coordinatePicked[0]][coordinatePicked[1]] == "X"):
         return False
      elif(self.gameBoard[coordinatePicked[0]][coordinatePicked[1]] == "O"):
         return False
      else:
         return True

   '''   
   Determines if the position the user chose is works or not by checking the space below.
   (Cannot place the connect 4 chip mid-air) 
   @param coordinatePicked is the coordinate the user chose. 
   ''' 
   def gravityChecker(self, coordinatePicked):
      #Calculate space below
      spaceBelow = [None] * 2
      spaceBelow[0] = coordinatePicked[0] + 1
      spaceBelow[1] = coordinatePicked[1]
      #coordinate at ground level
      if(spaceBelow[0] == 6):
         return True
      #Check if there's a marker below
      if(self.isSpaceAvailable(spaceBelow) == False):
         return True
      return False

   '''
   Uses all the methods within the connectFour() class so that it allows a user to play
   a connect four game with a the "computer" using random.
   '''
   def playGame(self):
      leaveLoop = False
      turnCounter = 0
      while(leaveLoop == False):
         if(turnCounter % 2 == 0):
            self.printGameBoard()
            while True:
               spacePicked = input("\nChoose a space: ")
               coordinate = self.coordinateParser(spacePicked)
               try:
                  #Check if the space is available
                  if(self.isSpaceAvailable(coordinate) and self.gravityChecker(coordinate)):
                     self.modifyBoard(coordinate, "O")
                     break
                  else:
                     print("Not a valid coordinate")
               except:
                  print("Error occured. Please try again.")
            winner = self.checkForWinner("O")
            turnCounter += 1
         #computers turn
         else:
            while True:
               possibleLetters = ["A","B","C","D","E","F","G"]
               computerChoice = [random.choice(possibleLetters), random.randint(0,5)]
               computerCoordinate = self.coordinateParser(computerChoice)
               if(self.isSpaceAvailable(computerCoordinate) and self.gravityChecker(computerCoordinate)):
                  self.modifyBoard(computerCoordinate, "X")
                  break
            turnCounter += 1
            winner = self.checkForWinner("X")

         if(winner):
            self.printGameBoard()
            print("Thank you. :) Goodbye!")
            break
            
            


'''        
def main():
   
   playGame()

if __name__ == "__main__":
   main()
   
###check for winner  
   
      rows = 6 #y
      columns = 7 #x
      #Check horizontal spaces
      for y in range(rows):
         for x in range(columns - 3):
            if self.gameBoard[x][y] == marker and self.gameBoard[x+1][y] == marker and self.gameBoard[x+2][y] == marker and self.gameBoard[x+3][y] == marker:
               print("\nGame over", marker, "wins! Thanks for playing :)")
               return True

      #Check vertical spaces
      for x in range(rows):
         for y in range(columns - 3):
            if self.gameBoard[x][y] == marker and self.gameBoard[x][y+1] == marker and self.gameBoard[x][y+2] == marker and self.gameBoard[x][y+3] == marker:
               print("\nGame over", marker, "wins! Thanks for playing :)")
               return True

      #check diagonally /
      for x in range(rows - 3):
         for y in range(3, columns):
            if self.gameBoard[x][y] == marker and self.gameBoard[x+1][y-1] == marker and self.gameBoard[x+2][y-2] == marker and self.gameBoard[x+3][y-3] == marker:
               print("\nGame over", marker, "wins! Thanks for playing :)")
               return True

      #Check diagonnally \
      for x in range(rows - 3):
         for y in range(columns - 3):
            if self.gameBoard[x][y] == marker and self.gameBoard[x+1][y+1] == marker and self.gameBoard[x+2][y+2] == marker and self.gameBoard[x+3][y+3] == marker:
               print("\nGame over", marker, "wins! Thanks for playing :)")
               return True
      return False
   
   
   
    
'''  