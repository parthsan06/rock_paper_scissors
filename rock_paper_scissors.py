import random

# Rock Paper Scissors ASCII Art
Rock = ("""
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)
""")

Paper = ("""
    _______
---'    ____)____
        ______)
        _______)
        _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
        ______)
    __________)
    (____)
---.__(___)
""")

# The chocies
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
if user_choice == 0:
    print(Rock)
elif user_choice == 1:
    print(Paper)
elif user_choice == 2:
    print(Scissors)
else:
    print("Invalid choice. Please choose a number between 0, 1 , 2.")

bot_choice = random.randint(0,2)
if bot_choice == 0:
    print("computer chose:\n", Rock)
elif bot_choice == 1:
    print("computer chose:\n", Paper)
elif bot_choice == 2:
    print("computer chose:\n", Scissors)

# The game

if bot_choice == 0 and user_choice == 0:
    print("It's a tie.")
if bot_choice == 0 and user_choice == 1:
    print("You win")
if bot_choice == 0 and user_choice == 2:
    print("You lose")

if bot_choice == 1 and user_choice == 0:
    print("You lose.")
if bot_choice == 1 and user_choice == 1:
    print("It's a tie.")
if bot_choice == 1 and user_choice == 2:
    print("You win.")

if bot_choice == 2 and user_choice == 0:
    print("You win.")
if bot_choice == 2 and user_choice == 1:
    print("You lose.")
if bot_choice == 2 and user_choice == 2:
    print("It's a tie.")

# A better solution by GPT:
# import random

# choices = ["Rock", "Paper", "Scissors"]

# # ASCII art optional
# rock = "✊"
# paper = "✋"
# scissors = "✌️"
# ascii_art = [rock, paper, scissors]

# user_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))
# bot_choice = random.randint(0, 2)

# print(f"\nYou chose: {choices[user_choice]} {ascii_art[user_choice]}")
# print(f"Computer chose: {choices[bot_choice]} {ascii_art[bot_choice]}")

# # Game result logic
# if user_choice == bot_choice:
#     print("It's a tie!")
# elif (user_choice - bot_choice) % 3 == 1:
#     print("You win!")
# else:
#     print("You lose.")

    # 🔄 It Feels Like Magic, But It’s Just Circular Logic
    # Think of Rock (0), Paper (1), Scissors (2) arranged in a circle:

    # markdown
    # Copy code
    #      0 (Rock)
    #     /       \
    # 2 (Scissors) 1 (Paper)
    # Now:

    # Going clockwise, each move beats the next.

    # (user - bot) % 3 == 1 checks if you're one step ahead in that circle.
