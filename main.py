class TicTacToe:
    def __init__(self):
        self.board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]
        self.board_rows = 3
        self.board_cols = 3
        self.teams = ["X", "O"]

        while True:
            player_1_move = str(input('Where to place an X? -> '))
            self.move(player_1_move, "X")
            self.update_board()
            c = self.check_board()
            if c[0]:
                break
            

            player_2_move = str(input('Where to place an O? -> '))
            self.move(player_2_move, "O")
            self.update_board()
            c = self.check_board()
            if c[0]:
                break
            
        print(f"{c[1]} won!")

    def move(self, move_slot, team):
        x, y = int(move_slot[0]), int(move_slot[1])
        slot = self.board[x][y]
        if slot == "-":
            self.board[x][y] = self.board[x][y].replace("-", team)


    def update_board(self):
        print(self.board[0][0] + self.board[0][1] + self.board[0][2])
        print(self.board[1][0] + self.board[1][1] + self.board[1][2])
        print(self.board[2][0] + self.board[2][1] + self.board[2][2])
        print('')

    def check_board(self):
        for team in self.teams:
            for cols in range(self.board_cols):
                vertical = []
                horizontal = []
                for rows in range(self.board_rows):
                    slot = self.board[rows][cols]
                    if slot == team:
                        vertical.append(slot)
                    if len(vertical) == 3:
                        if len(set(vertical)) == 1: # checks if items are identical
                            return True, team

                    slot = self.board[cols][rows]
                    if slot == team:
                        horizontal.append(slot)
                    if len(horizontal) == 3:
                        if len(set(horizontal)) == 1: # checks if items are identical
                            return True, team
        return False, ""

                

if __name__ == "__main__":
    TicTacToe()