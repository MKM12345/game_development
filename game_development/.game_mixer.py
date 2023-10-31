import pygame
from panda3d.core import Point3, Vec3
from direct.showbase.ShowBase import ShowBase

class GameDevelopment3D:
    def __init__(self):
        self.panda3d_app = ShowBase()
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.panda3d_app.userExit()

            self.screen.fill((0, 0, 0))
            pygame.display.flip()

            self.panda3d_app.taskMgr.step()

            self.clock.tick(60)

def start_game():
    game_dev_3d = GameDevelopment3D()
    game_dev_3d.run_game()

# The code won't execute immediately. You can call start_game() when you want to run the game.

