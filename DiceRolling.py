import random



while True:
    choice = input("Roll the dice ? (y/n):")
    choice = choice.upper()
    if choice == "Y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"({dice1}, {dice2})")
    elif choice == "N":
        print("Thanks for playing")
        break
    else: print("Invalid Input...")