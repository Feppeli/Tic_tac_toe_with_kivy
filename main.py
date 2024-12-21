from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


#gerenciador de tela
class GerenciadorDeTelas(ScreenManager):
    pass

#tela inicial do game
class TelaInicial(Screen):
    pass

#telas do jogo
class PlayersName(Screen):
    players = []

    def get_name_player(self, player_1, player_2):
        self.players.append(player_1)
        self.players.append(player_2)

        print(f"Jogadores: {self.players}")

class Jogo(Screen):
    victorys = []





#tela final do jogo
class TelaFinal(Screen):
    pass


# buildando a aplicação
class Game(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    Game().run()