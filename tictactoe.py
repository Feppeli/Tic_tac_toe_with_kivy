from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class TicTacToeApp(App):
    def build(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Layout principal
        self.main_layout = BoxLayout(orientation="vertical")

        # Grade do jogo
        self.grid = GridLayout(cols=3)
        self.buttons = []

        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = Button(font_size=32, on_press=self.make_move)
                self.grid.add_widget(button)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.main_layout.add_widget(self.grid)

        # Rótulo para mensagens
        self.status_label = Label(text=f"Jogador {self.current_player}, é sua vez!", font_size=24)
        self.main_layout.add_widget(self.status_label)

        return self.main_layout

    def make_move(self, button):
        # Encontre a posição do botão
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col] == button:
                    if self.board[row][col] == "":
                        self.board[row][col] = self.current_player
                        button.text = self.current_player
                        if self.check_winner():
                            self.status_label.text = f"Jogador {self.current_player} venceu!"
                            self.disable_buttons()
                            return
                        elif self.check_draw():
                            self.status_label.text = "Empate!"
                            return
                        else:
                            self.current_player = "O" if self.current_player == "X" else "X"
                            self.status_label.text = f"Jogador {self.current_player}, é sua vez!"
                    return

    def check_winner(self):
        # Verifica linhas, colunas e diagonais
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        # Verifica se o tabuleiro está cheio
        for row in self.board:
            if "" in row:
                return False
        return True

    def disable_buttons(self):
        # Desabilita todos os botões após o fim do jogo
        for row in self.buttons:
            for button in row:
                button.disabled = True


if __name__ == "__main__":
    TicTacToeApp().run()
