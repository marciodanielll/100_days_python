letter_to_index = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
index_to_letter = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

text = input('Digite o texto:\n').lower()
shift_amount = int(input('Digite o segredo, deve ser um número maior que 0 e menor que 26:\n'))
is_encrypting = bool(int(input('Digite 1 para criptografar ou 0 para descriptografar.\n')))

if not (0 < shift_amount < 26):
    print(shift_amount, 'É um valor incorreto')
else:
    new_text = ''
    for letter in text:
        if letter in letter_to_index:
            position = letter_to_index[letter]
            if is_encrypting:
                new_position = (position + shift_amount - 1) % 26 + 1
            else:
                new_position = (position - shift_amount - 1) % 26 + 1
            new_letter = index_to_letter[new_position]
            new_text += new_letter
        else:
            new_text += letter

    print(new_text)
