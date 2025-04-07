class Game:
    def __init__(self):
        self.turn = "X"
        self.tie = False
        self.winner = None
        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }

    def play_game(self):
        print("Welcome to Py-Pac-Poe! Let's play Tic-Tac-Toe.")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        self.render()

    def print_board(self):
        b = self.board
        print(
            f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            -----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            -----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """
        )

    def print_message(self):
        if self.tie:
            print("It's a tie!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move. Try again.")

    def check_for_winner(self):
        b = self.board
        win_combinations = [
            ('a1', 'b1', 'c1'),  # Top row
            ('a2', 'b2', 'c2'),  # Middle row
            ('a3', 'b3', 'c3'),  # Bottom row
            ('a1', 'a2', 'a3'),  # Left column
            ('b1', 'b2', 'b3'),  # Middle column
            ('c1', 'c2', 'c3'),  # Right column
            ('a1', 'b2', 'c3'),  # Diagonal TL-BR
            ('a3', 'b2', 'c1'),  # Diagonal BL-TR
        ]

        for combo in win_combinations:
            if b[combo[0]] and b[combo[0]] == b[combo[1]] == b[combo[2]]:
                self.winner = b[combo[0]]
                break

    def check_for_tie(self):
        if all(space is not None for space in self.board.values()) and self.winner is None:
            self.tie = True
            
    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"


if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
