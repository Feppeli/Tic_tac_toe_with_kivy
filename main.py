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
    posicoes_jogadas = [[None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None], [None, None]]
    posicoes_bloqueadas = []
    player = "X"

    def iniciar_jogo(self):
        print(f"Jogo iniciado, nome dos jogadores: {self.players[0], self.players[-1]}")

    def verificar_vitoria(self):
        #vertificando o primeiro jogador
        if self.posicoes_jogadas[0] == [1, "X"] and self.posicoes_jogadas[1] == [2, "X"] and self.posicoes_jogadas[2] == [3, "X"]:
            self.placar.append(self.players[0])
            print(f"Vencedor é o: {self.players[0]}")
        elif self.posicoes_jogadas[3] == [4, "X"] and self.posicoes_jogadas[4] == [5, "X"] and self.posicoes_jogadas[5] == [6, "X"]:
            self.placar.append(self.players[0])
            print(f"Vencedor é o: {self.players[0]}")
        elif self.posicoes_jogadas[6] == [7, "X"] and self.posicoes_jogadas[7] == [8, "X"] and self.posicoes_jogadas[8] == [9, "X"]:
            self.placar.append(self.players[0])
            print(f"Vencedor é o: {self.players[0]}")
        elif self.posicoes_jogadas[0] == [1, "X"] and self.posicoes_jogadas[4] == [5, "X"] and self.posicoes_jogadas[8] == [9, "X"]:
            self.placar.append(self.players[0])
            print(f"Vencedor é o: {self.players[0]}")
        elif self.posicoes_jogadas[2] == [3, "X"] and self.posicoes_jogadas[4] == [5, "X"] and self.posicoes_jogadas[6] == [7, "X"]:
            self.placar.append(self.players[0])
            print(f"Vencedor é o: {self.players[0]}")
        else:
            #Verificando o segundo jogador
            if self.posicoes_jogadas[0] == [1, "O"] and self.posicoes_jogadas[1] == [2, "O"] and self.posicoes_jogadas[2] == [3, "O"]:
                self.placer.append(self.players[-1])
                print(f"Vencedor é o: {self.players[-1]}")
            elif self.posicoes_jogadas[3] == [4, "O"] and self.posicoes_jogadas[4] == [5, "O"] and self.posicoes_jogadas[5] == [6, "O"]:
                self.placer.append(self.players[-1])
                print(f"Vencedor é o: {self.players[-1]}")
            elif self.posicoes_jogadas[6] == [7, "O"] and self.posicoes_jogadas[7] == [8, "O"] and self.posicoes_jogadas[8] == [9, "O"]:
                self.placer.append(self.players[-1])
                print(f"Vencedor é o: {self.players[-1]}")
            elif self.posicoes_jogadas[0] == [1, "O"] and self.posicoes_jogadas[4] == [5, "O"] and self.posicoes_jogadas[8] == [9, "O"]:
                self.placer.append(self.players[-1])
                print(f"Vencedor é o: {self.players[-1]}")
            elif self.posicoes_jogadas[2] == [3, "O"] and self.posicoes_jogadas[4] == [5, "O"] and self.posicoes_jogadas[6] == [7, "O"]:
                self.placer.append(self.players[-1])
                print(f"Vencedor é o: {self.players[-1]}")
            else:
                if len(self.posicoes_bloqueadas) >= 9:
                    print("empate")
        print(self.posicoes_jogadas)


    def jogada(self, posicao, button):
        if posicao in self.posicoes_bloqueadas:
            print("Já existe esta jogada")
        else:
            self.posicoes_bloqueadas.append(posicao) # guardando a posição para validar se está disponível
            #self.posicoes_jogadas.append([posicao, self.player]) # guardando a jogada e o jogador
            index = posicao - 1
            self.posicoes_jogadas[index] = [posicao, self.player]
            button.text = self.player

            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"

            self.verificar_vitoria()



#tela final do jogo
class TelaFinal(Screen):
    pass


# buildando a aplicação
class Game(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    Game().run()