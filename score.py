from asteroid import *
from constants import *

class Score(pygame.sprite.Sprite):
    containers: pygame.sprite.Group
    def __init__(self) -> None:
        self.score: int = 0

    def score_add(self, asteroid):
        if asteroid.radius == ASTEROID_MAX_RADIUS:
            self.score += 20
        elif asteroid.radius == ASTEROID_MIN_RADIUS:
            self.score += 100
        else:
            self.score += 40

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw

    # def update(self) -> None:
    #     pass