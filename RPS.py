#RPS.py
#Name:Nomaan Ahmed 
#Date:2/9/25
#Assignment:Lab 3 
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  choices = ['R', 'P', 'S']

  while True:
        computer_move = random.choice(choices)
        user_move = input("Enter your move (R, P, S) or 'Q' to quit: ").upper()

        if user_move == 'Q':
            break

        if user_move not in choices:
            print("Invalid move. Please try again.")
            continue

        print(f"Computer chose: {computer_move}")
        
        if user_move == computer_move:
            print("It's a tie!")
            ties += 1
        elif (user_move == 'R' and computer_move == 'S') or \
             (user_move == 'P' and computer_move == 'R') or \
             (user_move == 'S' and computer_move == 'P'):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("\nGame Over!")
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
