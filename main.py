from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


#gerenciador de tela
class GerenciadorDeTelas(ScreenManager):
    pass

#tela inicial do game
class TelaInicial(Screen):
    pass

class Jogo(Screen):
    pass

#tela final do jogo
class TelaFinal(Screen):
    pass

class Game(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == "__main__":
    Game().run()