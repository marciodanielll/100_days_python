import random

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

hash_human_choice = {
  "pedra": 1,
  "papel": 2,
  "tesoura": 3, 
}

hash_print_choice = {
  "1": rock,
  "2": paper,
  "3": scissors, 
}

human_option = (input('Pedra, Papel ou Tesoura?\n')).lower()

human_choice = hash_human_choice[human_option]

print("Seu lance", hash_print_choice[f"{human_choice}"], '\n')

machine_choice = random.randint(1, 3)

print("Lance da máquina", hash_print_choice[f"{machine_choice}"])


if(human_choice == machine_choice):
  print('Houve Empate')
else: 
  if human_choice == 1:
    if(machine_choice == 3):
      print("Você venceu")
    else: 
      print("A máquina venceu")
  if human_choice == 2:
    if(machine_choice == 1):
      print("Você venceu")
    else: 
      print("A máquina venceu")
  if human_choice == 3:
    if(machine_choice == 2):
      print("Você venceu")
    else: 
      print("A máquina venceu")