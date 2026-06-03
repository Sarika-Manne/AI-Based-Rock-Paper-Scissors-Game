import random
from collections import Counter

choices = ["rock", "paper", "scissors"]
user_history = []

user_score = 0
computer_score = 0

def predict_user_move():
    if not user_history:
        return random.choice(choices)

    count = Counter(user_history)
    return count.most_common(1)[0][0]

def get_computer_move():
    predicted = predict_user_move()

    # Counter move
    if predicted == "rock":
        return "paper"
    elif predicted == "paper":
        return "scissors"
    else:
        return "rock"

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

while True:
    user = input("Enter rock, paper, scissors (or quit): ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    user_history.append(user)

    computer = get_computer_move()
    print("Computer chose:", computer)

    result = get_winner(user, computer)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)
