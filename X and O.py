import tkinter as tk
from tkinter import ttk, messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Крестики-Нолики")
        self.master.geometry("400x450")
        self.master.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self._create_widgets()

    def _create_widgets(self):
         # Frame for the grid
        grid_frame = ttk.Frame(self.master, padding="20")
        grid_frame.pack(pady=20, expand=True)
        
        for i in range(9):
            button = ttk.Button(
                grid_frame,
                text="",
                width=2,
                command=lambda idx=i: self.on_button_click(idx),
                style="GameButton.TButton"
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="nsew")
            self.buttons.append(button)

            # Configure grid weights for resizing
            grid_frame.grid_columnconfigure(i % 3, weight=1)
            grid_frame.grid_rowconfigure(i // 3, weight=1)

         # Style for the game buttons
        self.master.style = ttk.Style()
        self.master.style.configure("GameButton.TButton", padding=10, font=("Arial", 36), borderwidth=2, relief="groove")

    def on_button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            self.check_win()
            self.switch_player()
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        
    def check_win(self):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for win in wins:
            a, b, c = win
            if self.board[a] == self.board[b] == self.board[c] != "":
                self.game_over(self.board[a])
                return
            
        if "" not in self.board:
            self.game_over("Tie")

    def game_over(self, winner):
        if winner == "Tie":
             messagebox.showinfo("Игра окончена!", "Ничья!")
        else:
             messagebox.showinfo("Игра окончена!", f"Игрок {winner} победил!")
        
        self.reset_game()

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
