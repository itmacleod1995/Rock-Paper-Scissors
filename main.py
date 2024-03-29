import random

def chooseWinner(playerChoice, computerChoice):
    """Method to decide the winner"""
    if playerChoice == "0" and computerChoice == 2:
        print("Player wins!")
    elif playerChoice == "1" and computerChoice == 0:
        print("Player wins!")
    elif playerChoice == "2" and computerChoice == 1:
        print("Player wins!")
    elif int(playerChoice) == computerChoice:
        print("Draw!")
    else:
        print("Computer wins")

game = True
while game:
    computerChoices = [0, 1, 2]
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. Type q to quit: ")
    print("")
    if choice == "q":
        print("Thank you for playing!")
        break

    computerChoice = random.choice(computerChoices)

    print("Player choice: ")
    if choice == "0":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif choice == "1":
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    print("Computer choice: ")

    if computerChoice == 0:
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif computerChoice == 1:
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    chooseWinner(playerChoice=choice, computerChoice=computerChoice)