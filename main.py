#GREETING
print("Welcome to the Rock, Paper, Scissors game!")
choices= ["Rock", "Paper", "Scissors"]
#COMPUTER'S CHOICE
import random
computer_choice = random.choice(choices)
#THE RULES
rules=input("Press enter to continue or type 'rules' to see the rules: ")
if rules == "rules".lower():
    print("""              *****RULES*****\n1)You choose and the computer chooses\n2)Rock smashes Scissors-> Rock wins\n3)Scissors cuts Paper-> Scissors win\n4)Paper covers Rock-> Paper wins""")
else:
    print("Let's play!")
#THE ASCII ART
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#YOUR CHOICE
your_choice=input("Choose Rock, Paper or Scissors: ").capitalize()
#THE GAME
#ROCK'S CONDITIONS
if your_choice ==choices[0]and computer_choice==choices[0]:
  print(f"Your choice:\n{rock}\nComputer's choice:\n{rock}\nIt's a tie!")
elif your_choice ==choices[0]and computer_choice==choices[1]:
  print(f"Your choice:\n{rock}\nComputer's choice:\n{paper}\nYou lose!")
elif your_choice ==choices[0]and computer_choice==choices[2]:  
 print(f"Your choice:\n{rock}\nComputer's choice:\n{scissors}\nYou win!")
  #PAPER'S CONDITIONS
elif your_choice ==choices[1]and computer_choice==choices[0]:
  print(f"Your choice:\n{paper}\nComputer's choice:\n{rock}\nYou win!")
elif your_choice ==choices[1]and computer_choice==choices[1]:
  print(f"Your choice:\n{paper}\nComputer's choice:\n{paper}\nIt's a tie!")
elif your_choice ==choices[1]and computer_choice==choices[2]:
  print(f"Your choice:\n{paper}\nComputer's choice:\n{scissors}\nYou lose!")
  #SCISSORS' CONDITIONS
elif your_choice ==choices[2]and computer_choice==choices[0]:
  print(f"Your choice:\n{scissors}\nComputer's choice:\n{rock}\nYou lose!")
elif your_choice ==choices[2]and computer_choice==choices[1]:
   print(f"Your choice:\n{scissors}\nComputer's choice:\n{paper}\nYou win!")
elif your_choice ==choices[2]and computer_choice==choices[2]:
   print(f"Your choice:\n{scissors}\nComputer's choice:\n{scissors}\nIt's a tie!")
#INVALID CONDITION
else  :
   print("Invalid choice. Please choose Rock, Paper, or Scissors.")
