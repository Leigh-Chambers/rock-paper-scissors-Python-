rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

while player_choice>=0 and player_choice<=2:
  cpu_choice = random.randint(0,2)
  
  game_list=[rock, paper, scissors]
  player_choice = game_list[player_choice]
  cpu_choice = game_list[cpu_choice]
    
  if (player_choice == rock and cpu_choice==scissors) or (player_choice == paper and cpu_choice == rock) or player_choice == scissors and cpu_choice == paper:
    print(player_choice,"Player",  cpu_choice, "Cpu", "\n\n Congratulations!!! You win!")
    break
  elif player_choice == cpu_choice:
    print(player_choice,"Player",  cpu_choice, "Cpu", "\n\nWell would you look at that!! Its a Draw!")
    break
  
  else:
    print( player_choice,"Player",  cpu_choice, "Cpu", "\n\n Unlucky!!! You lose!")
    break
else:
  print("You chose an invalid input, You lose!")