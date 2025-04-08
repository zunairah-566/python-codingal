import random
while True:
    user_action = input("Enter a choice(rock, paper, scissor):")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"you chose{user_action}, computer chose {computer_action} \n")
    #conditions
    if user_action == computer_action:
        print("Its a Tie")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("you won")
        else:
            print("computer won")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("you won")
        else:
            print("computer won")            
    elif user_action == "paper":
        if computer_action == "rock":
            print("you won")
        else:
            print("computer won")       