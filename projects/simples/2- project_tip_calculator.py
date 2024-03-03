print("Welcome to tipe calculator.\n\n")

total_bill = float(input("What was total bill?\n"))
percentage_tip = int(input("What percentage tipo wold like to give? 10%, 12%, or 15%\n"))
total_people = int(input("How many people to split the bill?\n"))

calculate = round((total_bill * float(f"1.{percentage_tip}") / total_people), 2)

print(f"Each person should pay: ${calculate}")
