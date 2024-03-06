import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '`', '~']

print('Boas vindas ao gerador de senha!\n')

quantity_letters = int(input('Quantas letras você deseja que contenha na senha?\n'))
quantity_symbols = int(input('Quantos símbolos?\n'))
quantity_numbers = int(input('Quantos números?\n'))

password_length = quantity_letters + quantity_symbols + quantity_numbers

password_list = []

if quantity_letters > 0:
  initial_range = 1
  final_range = quantity_letters + 1

  for number in range(initial_range, final_range):
    choice = random.randint(0, len(alphabet) -1)
    letter = alphabet[choice]

    isLower = bool(random.randint(0,1))
    if bool(isLower):
       letter = letter.upper()
    password_list.append(letter)

if quantity_symbols > 0:
    initial_range = 1
    final_range = quantity_symbols + 1

    for number in range(initial_range, final_range):
      choice = random.randint(0, len(symbols) -1)
      password_list.append(symbols[choice])

if quantity_numbers > 0:
    initial_range = 1
    final_range = quantity_numbers + 1

    for number in range(initial_range, final_range):
      choice = random.randint(0, len(numbers) -1)
      password_list.append(numbers[choice])

for index in range(1, 100):
   choice_one = random.randint(1, password_length -1)
   choice_two = random.randint(1, password_length -1)

   memory = password_list[choice_one]

   password_list[choice_one] = password_list[choice_two]
   password_list[choice_two] = memory

new_password = ''
for index in range(0, password_length):
   new_password = new_password + f'{password_list[index]}'

print('Sua nova senha é:')
print(new_password)
