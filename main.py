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

    def get_name_player(self, player_1, player_2): # função para pegar o nome dos jogadores
        self.players.append(player_1)
        self.players.append(player_2)

        print(f"Jogadores: {self.players}")

class Jogo(PlayersName):

    placar = []
    posicoes_jogadas = []
    posicoes_bloqueadas = []
    player = "x"

    def iniciar_jogo(self):
        print(f"Jogo iniciado, nome dos jogadores: {self.players[0], self.players[-1]}")

    def jogada(self, posicao, button):
        if posicao in self.posicoes_bloqueadas:
            print("Já existe esta jogada")
            print(self.posicoes_jogadas)
        else:
            self.posicoes_bloqueadas.append(posicao) # guardando a posição para validar se está disponível
            self.posicoes_jogadas.append([posicao, self.player]) # guardando a jogada e o jogador
            button.text = self.player

            if self.player == "x":
                self.player = "O"
            else:
                self.player = "x"

            print(self.posicoes_jogadas)



#tela final do jogo
class TelaFinal(Screen):
    pass


# buildando a aplicação
class Game(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    Game().run()