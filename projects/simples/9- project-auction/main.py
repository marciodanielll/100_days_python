import os
from art import logo

def handle_info():
  os.system('clear')
  print(logo)

bid_record = {}

has_another_bid = True

while has_another_bid:
  handle_info()

  bidder_name = input('Qual o seu nome?:\n')
  bid = float(input('Qual o valor do eu lance?\n'))
  another_bid = input('Terá outro apostador? "Yes" ou "Not"\n ').lower()
  
  print(another_bid)

  bid_record[bidder_name] = bid
  handle_info()

  if another_bid == 'not':
    has_another_bid = False
    
    highest_bid = 0
    winner_name = ''
    
    for key in bid_record:
      if bid_record[key] > highest_bid:
        highest_bid =  bid_record[key]
        winner_name = key
    print(f'O vencedor é: {winner_name} com lance de: {highest_bid}')