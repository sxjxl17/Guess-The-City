import tkinter as tk
import random


l1 = [
    {"city": "New York City", "clue": "Manhattan is its core city."},
    {"city": "London", "clue": "The Royal city. Big Ben in here"},
    {"city": "Tokyo", "clue": "Most populated metropolitan city of the world. Close to the place where nuclear bombs were dropped."},
    {"city": "Singapore", "clue": "Famous Lion Merilion Statue is here."},
    {"city": "Los Angeles", "clue": "Home of Hollywood"},
    {"city": "Hong Kong", "clue": "Richest city occupied by China"},
    {"city": "Paris", "clue": "City of Love"},
    {"city": "Dubai", "clue": "City with Palm shaped Islands"},
    {"city": "Shanghai", "clue": "Financial capital of China"},
    {"city": "Beijing", "clue": "Capital of China"}
]

l2 = [
    {"city": "Zurich", "clue": "Most expensive city in the World"},
    {"city": "Geneva", "clue": "The UN Headquarters are in this Swiss city."},
    {"city": "San Francisco", "clue": "Leading centre of technology in the World. Close to Silicon Valley"},
    {"city": "Sydney", "clue": "Famous Opera House is here."},
    {"city": "Frankfurt", "clue": "Financial capital of Germany. Also called Mainhatten of Europe."},
    {"city": "Chicago", "clue": "Most famous pizzas in USA"},
    {"city": "Toronto", "clue": "Financial capital and biggest city of Canada."},
    {"city": "Melbourne", "clue": "World's second biggest cricket stadium is here."},
    {"city": "Mumbai", "clue": "City of 7 islands"},
    {"city": "Seoul", "clue": "Capital of South Korea"}
]

random.shuffle(l1)
random.shuffle(l2)


level = 1
index = 0
score1 = 0
score2 = 0
username = ""



def start_game():
    global username
    username = name_entry.get()

    start_frame.pack_forget()
    welcome_frame.pack(fill="both", expand=True)

    welcome_label.config(text=f"Welcome,\nCaptain {username}")

    root.after(2000, start_level1)


def start_level1():
    welcome_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    show_question()


def show_question():
    global index

    if level == 1:
        if index < len(l1):
            clue_label.config(text=l1[index]["clue"])
        else:
            check_level1()

    elif level == 2:
        if index < len(l2):
            clue_label.config(text=l2[index]["clue"])
        else:
            show_result()


def submit_answer():
    global index, score1, score2

    guess = answer_entry.get()

    if level == 1:
        if guess.lower() == l1[index]["city"].lower():
            score1 += 1
    else:
        if guess.lower() == l2[index]["city"].lower():
            score2 += 1

    index += 1
    answer_entry.delete(0, tk.END)

    root.after(300, show_question)


def check_level1():
    global level, index

    if score1 < 5:
        clue_label.config(text=f"❌ Failed\nScore: {score1}/10", fg="red")
        submit_btn.config(state="disabled")
    else:
        game_frame.pack_forget()
        level2_frame.pack(fill="both", expand=True)

        level2_label.config(text=f"\n🔥 Qualified for Level 2!\nScore: {score1}/10")

        level = 2
        index = 0

        root.after(2000, start_level2)


def start_level2():
    level2_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    show_question()


def show_result():
    total = score1 + score2

    clue_label.config(text=f"\n🏆 Final Score: {total}/20")
    submit_btn.config(state="disabled")

    with open("stats.txt", "a") as f:
        f.write(f"{username} - {total}/20\n\n")

    leaderboard_btn_game.pack(pady=10)


def show_leaderboard():
    win = tk.Toplevel(root)
    win.title("Leaderboard")
    win.geometry("400x400")
    win.configure(bg="#0f172a")

    tk.Label(win, text="🏆 LEADERBOARD", font=("Arial", 18, "bold"),
             fg="#00ffcc", bg="#0f172a").pack(pady=20)

    try:
        with open("stats.txt", "r") as f:
            data = f.readlines()

        data.sort(reverse=True)

        for line in data[:10]:
            tk.Label(win, text=line.strip(),
                     fg="white", bg="#0f172a").pack()
    except:
        tk.Label(win, text="No scores yet",
                 fg="white", bg="#0f172a").pack()



root = tk.Tk()
root.title("~~~~~ GUESS THE CITY ~~~~~")
root.geometry("500x500")
root.configure(bg="#0f172a")


start_frame = tk.Frame(root, bg="#0f172a")
start_frame.pack(fill="both", expand=True)

tk.Label(start_frame, text="🌍 ~~~~~ GUESS THE CITY ~~~~~",
         font=("Arial", 22, "bold"),
         fg="#00ffcc", bg="#0f172a").pack(pady=40)

name_entry = tk.Entry(start_frame, font=("Arial", 14))
name_entry.pack(pady=10)
name_entry.insert(0, "Enter Name")

tk.Button(start_frame, text="Start Game",
          bg="#00ffcc", fg="black",
          command=start_game).pack(pady=10)

tk.Button(start_frame, text="Leaderboard",
          bg="#ffcc00", fg="black",
          command=show_leaderboard).pack()


welcome_frame = tk.Frame(root, bg="#0f172a")

tk.Label(welcome_frame, text="🌍 CITY GUESSER GAME",
         font=("Arial", 22, "bold"),
         fg="#00ffcc", bg="#0f172a").pack(pady=40)

welcome_label = tk.Label(welcome_frame, text="",
                         font=("Arial", 16),
                         fg="white", bg="#0f172a")
welcome_label.pack()


level2_frame = tk.Frame(root, bg="#0f172a")

level2_label = tk.Label(level2_frame, text="",
                        font=("Arial", 16, "bold"),
                        fg="yellow", bg="#0f172a")
level2_label.pack(pady=100)

# -------- GAME SCREEN -------- #
game_frame = tk.Frame(root, bg="#0f172a")

clue_label = tk.Label(game_frame, text="",
                      font=("Arial", 16),
                      fg="white", bg="#0f172a")
clue_label.pack(pady=40)

answer_entry = tk.Entry(game_frame, font=("Arial", 14))
answer_entry.pack()

submit_btn = tk.Button(game_frame, text="Submit",
                       bg="#00ffcc", fg="black",
                       command=submit_answer)
submit_btn.pack(pady=10)

leaderboard_btn_game = tk.Button(game_frame,
                                 text="View Leaderboard",
                                 bg="#ffcc00",
                                 command=show_leaderboard)

root.mainloop()