import random

def determine_winner(user_action, computer_action):
    victories = {
        "rock": "scissor",  # Rock beats scissors
        "paper": 'rock',  # Paper beats rock
        "scissor": "paper"  # Scissors beats paper
    }
    print(f"Computer: {computer_action}")
    defeats = victories[user_action]
    if user_action == computer_action:
        print("It's a tie!")
        return 'tie'
    elif computer_action in defeats:
        print("You win!")
        return 'human'
    else:
        print("You lose.")
        return 'computer'


if __name__ == '__main__':
    words = ['rock', 'paper', 'scissor']
    humanscore = 0
    computerscore = 0


    while max(humanscore,computerscore) <3:
        user = input("Your: ")
        computer = random.choice(words)
        result = determine_winner(user, computer)
        if result == "human":
            humanscore = humanscore + 1
        if result == "computer":
            computerscore = computerscore + 1

    if humanscore > computerscore:
        print("YOU WON!")
    if computerscore > humanscore:
        print("COMPUTER WON!")
    if computerscore == humanscore:
        print('ITS A TIE!')

















