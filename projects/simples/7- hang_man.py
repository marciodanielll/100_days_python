import random
import os

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ['sol', 'lua', 'estrela', 'mar', 'rio', 'montanha', 'floresta', 'cidade', 'pais', 'animal', 'planta', 'carro', 'estrada', 'musica', 'livro', 'filme', 'computador', 'telefone', 'escola', 'trabalho']

word_choice = random.choice(word_list)

word_length = len(word_choice)

word_mask = []
for _ in range(0, word_length):
    word_mask.append('-')

count_asserts = 0
count_error = 0

def print_infos():
    print('\nSeja bem vindo ao jogo da froca...!')
    print(stages[count_error])
    print(word_mask)

print_infos()

def clear_terminal():
    os_system = os.name
    if os_system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    user_letter = input('\nDigite uma letra:\n').lower()
    found_chars = [i for i, char in enumerate(word_choice) if char == user_letter]

    if bool(len(found_chars)):
        count_asserts += len(found_chars)
        for index in found_chars:
            word_mask[index] = user_letter
        clear_terminal()
        print_infos()

        if count_asserts == word_length:
            print('\nFim de jogo, você venceu...\n')
            break 
    else:
        stages[count_error]
        count_error += 1
        clear_terminal()
        print_infos()

        if count_error == 6:
            print('\nVocê morreu......\n')
            break
