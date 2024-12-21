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

class Jogo(PlayersName):

    placar = []
    #jogador 1 = self.players[0]
    #jogador 2 = self.players[-1]

    def iniciar_jogo(self):
        print(f"Jogo iniciado, nome dos jogadores: {self.players[0], self.players[-1]}")




#tela final do jogo
class TelaFinal(Screen):
    pass


# buildando a aplicação
class Game(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    Game().run()