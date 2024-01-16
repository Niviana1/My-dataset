import tkinter as tk
from tkinter import messagebox

def create_button(row, column):
    return tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda: button_click(row, column))

def disable_buttons():
    for button_row in buttons:
        for button in button_row:
            button['state'] = tk.DISABLED

def restart_game():
    global player_turn, move_count
    player_turn, move_count = 1, 0
    label2['bg'], label2['text'] = "skyblue", 'Player-1 Turn'
    
    for button_row in buttons:
        for button in button_row:
            button.config(text='', bg='white', state=tk.NORMAL)

def button_click(row, column):
    global player_turn, move_count

    button = buttons[row][column]

    if button['text'] == '' and move_count < 9:
        symbol = 'X' if player_turn == 1 else 'O'
        button.config(text=symbol, bg="skyblue" if player_turn == 1 else "#e8956f")
        label2.config(bg="#e8956f" if player_turn == 1 else "skyblue", text=f'Player-{3-player_turn} Turn')

        player_turn, move_count = 3 - player_turn, move_count + 1
        check_winner()

def check_winner():
    global move_count
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]
    ]

    for combination in win_combinations:
        symbols = [buttons[row][column]['text'] for row, column in combination]
        if symbols == ['X', 'X', 'X'] or symbols == ['O', 'O', 'O']:
            disable_buttons()
            winner = '1' if symbols[0] == 'X' else '2'
            messagebox.showinfo("Tic Tac Toe", f"Winner is player {winner}")
            return

    if move_count == 9:
        disable_buttons()
        messagebox.showinfo("Tic Tac Toe", "Match is Draw.")

# Main code
window = tk.Tk()
window.title('Tic Tac Toe')

frame = tk.Frame(master=window)
frame.pack(pady=10)

label = tk.Label(master=frame, text="Tic Tac Toe", font=("Arial", 15))
label.pack()

frame1 = tk.Frame(master=window, borderwidth=2, relief=tk.SUNKEN, bg='#dadec3')
frame1.pack(padx=10, pady=10)

buttons = [[create_button(row, col) for col in range(3)] for row in range(3)]
for row, button_row in enumerate(buttons):
    for col, button in enumerate(button_row):
        button.grid(row=row, column=col, padx=8, pady=8)

frame2 = tk.Frame(master=window, border=2, relief=tk.SUNKEN, bg='#dadec3')
frame2.pack()

label1 = tk.Label(master=frame2, text="Player 1 --> X\nPlayer 2 --> O", width=10)
label1.grid(row=0, column=0, padx=5)

button_restart = tk.Button(master=frame2, text="Restart", width=10, height=3, relief=tk.GROOVE, command=restart_game)
button_restart.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(master=frame2, text='Player-1 Turn', bg="skyblue", width=10, height=3, relief=tk.SUNKEN)
label2.grid(row=0, column=2, padx=5)

player_turn, move_count = 1, 0

window.mainloop()
      
