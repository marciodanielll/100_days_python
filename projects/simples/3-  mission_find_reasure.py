print("Bem-vindo à Ilha do Tesouro.\nSua missão é encontrá-lo.\n")

decisionOne = (input("Esquerda ou Direita?\n")).lower()

if decisionOne == 'direita':
  print("\nCaiu em um buraco. \nGame Over.")
else:
  decisionTwo = (input("\nNadar ou Esperar?\n")).lower()
  if decisionTwo == 'nadar':
   print("\nAtacado por tubarões.\nGame Over.")
  else:
    decisionThree = (input("\nQual a porta escolhe?\nAzul, Amarela ou Vermelha?\n")).lower()
    if decisionThree == 'azul':
      print("\nDevorado por feras.\nGame Over.")
    elif decisionThree == 'vermelha':
      print("\nQueimando no fogo.\nGame Over.")
    elif decisionThree == "amarela":
      print("\nVocê venceu")
    else:
      print("Game Over.")