a = 0
b = 1
you = 0
com = 0

print("    Welcome to SNAKE WATER GUN Game")
print("--------------------------------------")
print("There are 10 rounds!")
while a<10:
    import random
    list = ["Snake", "Water", "Gun"]
    rc = random.choice(list)
    inp1 = input("\nEnter S for Snake W for Water G for Gun: ")
    inp2 = inp1.capitalize()
    a = a + b

# Snake
    if rc == "Snake" and inp2 == "S":
        print("Round", a, "Draw")

    elif rc == "Snake" and inp2 == "W":
        print("Round", a, "You Lose")
        com = com + 1

    elif rc == "Snake" and inp2 == "G":
        print("Round", a, "You Won")
        you = you + 1

# Water
    elif rc == "Water" and inp2 == "S":
        print("Round", a, "You Won")
        you = you + 1

    elif rc == "Water" and inp2 == "W":
        print("Round", a, "Draw")

    elif rc == "Water" and inp2 == "G":
        print("Round", a, "You Lose")
        com = com + 1

# Gun
    elif rc == "Gun" and inp2 == "S":
        print("Round", a, "You Lose")
        com = com + 1

    elif rc == "Gun" and inp2 == "W":
        print("Round", a, "You Won")
        you = you + 1

    elif rc == "Gun" and inp2 == "G":
        print("Round", a, "Draw")

    else:
        print("Wrong input!!!")
        
# After Gun
    if a == 10:
        print("\nRound 0ver!")
        print("Your score is", you)
        print("Computer's score is", com)

        if you>com:
            print("You Won The Game")

        if you<com:
            print("You Lose The Game")

        if you==com:
            print("Game Draw")