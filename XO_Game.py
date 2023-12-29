from tkinter import *
import random

def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            game_btns[row][col]['text'] = player
            if check_winner() == False:
                player = players[1]
                label.config(text=(player + " turn"))
            elif check_winner() == True:
                label.config(text=(players[0] + " wins!"))
                
            elif check_winner() == "tie":
                label.config(text=("Tie - no winner!"))
        elif player == players[1]:
            game_btns[row][col]['text'] = player
            if check_winner() == False:
                player = players[0]
                label.config(text=(player + " turn"))
            elif check_winner() == True:
                label.config(text=(players[1] + " wins!"))
                
            elif check_winner() == "tie":
                label.config(text=("Tie - no winner!"))

def check_winner():
    # Check rows
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg = 'green')
            game_btns[row][1].config(bg = 'green')
            game_btns[row][2].config(bg = 'green')
            return True
    
    # Check columns
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg = 'green')
            game_btns[1][col].config(bg = 'green')
            game_btns[2][col].config(bg = 'green')
            return True
    # Check diagonal from top-left to bottom-right
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg = 'green')
        game_btns[1][1].config(bg = 'green')
        game_btns[2][2].config(bg = 'green')
        return True
    # Check diagonal from top-right to bottom-left
    if game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[1][1].config(bg = 'green')
        game_btns[0][2].config(bg = 'green')
        game_btns[2][0].config(bg = 'green')
        return True
   
    # Check for tie
    if check_empty_space() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')
        return "tie"
    # No winner yet
    return False
    
def check_empty_space():
   
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] == "":
                return True
            
    return False

def start_new_game():
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")


# Main window
window = Tk()
window.title("XO Game")

# Players and starting player
players = ["X", "O"]
player = random.choice(players)

# Game buttons
game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Label for turn information
label = Label(text=(player + " turn"), font=('Consolas', 40))
label.pack(side="top")

# Restart button
restart_button = Button(text="Restart", font=('Consolas', 20), command=start_new_game)
restart_button.pack(side="top")

# Frame for buttons
btns_frame = Frame(window)
btns_frame.pack()

# Create game buttons
for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font='Consolas', width=6, height=3,
                                      command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

# Start the game
window.mainloop()