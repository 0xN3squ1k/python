import random

print("Welcome to Rock - Paper - Scissors game!.")
options = ["Rock", "Paper", "Scissors"]
pcSelection = random.choice(options).upper()
userSelection = input('Choose "Rock", "Paper" or "Scissors": ').upper()

# Rock Paper Scissors ASCII Art
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art = {
    "ROCK": rock,
    "PAPER": paper,
    "SCISSORS": scissors
}

print("You choose:")
print(art[userSelection])

print("The random choice is:")
print(art[pcSelection])

if userSelection == pcSelection:
    print("### TIE! ###")

elif (
    (userSelection == "ROCK" and pcSelection == "SCISSORS") or
    (userSelection == "PAPER" and pcSelection == "ROCK") or
    (userSelection == "SCISSORS" and pcSelection == "PAPER")
):
    print("### YOU WIN! ###")

else:
    print("### YOU LOSE! ###")
