from ..components import info, player
from .. import setup
from .. import constants as C
import pygame


class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info = info.Info('level')
        self.setup_background()
        self.setup_player()

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,
                                                 (int(rect.width * C.BG_MULTI), int(rect.height * C.BG_MULTI)))
        self.background_rect = self.background.get_rect()

    def setup_player(self):
        self.player = player.Player('mario')
        self.player.rect.x, self.player.rect.y = 110, 490

    def update_player_position(self):
        self.player.rect.x += self.player.x_vel
        self.player.rect.y += self.player.y_vel

    def update(self, surface, keys):
        self.player.update(keys)
        self.update_player_position()
        self.draw(surface)

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        surface.blit(self.player.image, self.player.rect)
        self.info.draw(surface)
