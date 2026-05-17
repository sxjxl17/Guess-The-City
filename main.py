import tkinter as tk
import random
username = input("Enter username: ")
print("\n\n --- GUESS THE CITY ---")
print(f"Welcome, Captain {username}")
print("\nLEVEL 1\n\n")

l1 = [
    {"city": "New York City", "clue- ": "Its main region is Manhattan."},
    {"city": "London", "clue- ": "The Big Ben is here"},
    {"city": "Tokyo", "clue- ": "World's most metropolitan area in the world. Close to the where nuclear bombs were dropped"},
    {"city": "Singapore City", "clue- ": "City where famous Lion Fountain Statue is located."},
    {"city": "Los Angeles", "clue- ": "Home of Hollywood"},
    {"city": "Hong Kong", "clue- ": "Rich city occupied by China"},
    {"city": "Paris", "clue- ": "Eiffel tower is here."},
    {"city": "Dubai", "clue- ": "Artificial islands in shape of a palm tree."},
    {"city": "Shanghai", "clue- ": "Financial capital of China"},
    {"city": "Beijing", "clue- ": "Capital of China"}
]

random.shuffle(l1)
score = 0
for q in l1:
    print("Clue: ", q["clue- "])

    guess = input("Guess the city: ")
    if guess.lower() == q["city"].lower():
        print("\nCorrect\n--------------------------------------------")
        score += 1  
print(f"Level 1 Score = {score}/10")
   
if (score == 5) or (score == 6) or (score == 7) or (score == 8) or (score == 9) or (score == 10):
    print("\nYou're qualified for Level 2!\n")
else:
    print("YOU'RE FAIL!")
    exit()

print("LEVEL 2")

l2 = [
    {"city": "Zurich", "clue- ": "Most expensive city in the world."},
    {"city": "Geneva", "clue- ": "UN Headquarters are in this city of Switzerland."},
    {"city": "San Francisco", "clue- ": "World's leading hub of Technology. Close to Silicon valley."},
    {"city": "Sydney", "clue- ": "Famous opera house is located here."},
    {"city": "Frankfurt", "clue- ": "Financial hub of Germany. Also called as Mainhatten of Europe."},
    {"city": "Chicago", "clue- ": "Most famous pizzas in USA"},
    {"city": "Toronto", "clue- ": "Most populated city and financial capital of Canada."},
    {"city": "Melbourne", "clue- ": "Second largest cricket stadium in the world is here."},
    {"city": "Mumbai", "clue- ": "The city of 7 Islands"},
    {"city": "Seoul", "clue- ": "Kpop started from this city."}
]
random.shuffle(l2)

for q in l2:
    print("Clue: ", q["clue- "])
    guess = input("\nGuess the city: ")
    if guess.lower() == q["city"].lower():
        print("\nCorrect\n-----------------------------")
        score += 1
print(f"\nFinal Score = {score}/20\n-------------------------------")

with open("stats.txt", "a") as file:
    file.write(f"{username} - {score}/20\n")
    file.close()

print("\nALL SCORES\n")
with open("stats.txt", "r") as file:
    print(file.read())
    file.close()

