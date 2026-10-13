import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from logger import log_state
from logger import log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
def main():
    pygame.init()
    font = pygame.font.Font(None, 36)
    

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    Score.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH /2), (SCREEN_HEIGHT /2))
    asteroidField = AsteroidField()
    player_score = Score()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")

        score_text = font.render(f"Score: {player_score.score}", True, "white")
        screen.blit(score_text, (10, 10))

        updatable.update(dt)
        for object in asteroids:
            if player.collides_with(object):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(object):
                    log_event("asteroid_shot")
                    player_score.score_add(object)
                    shot.kill()
                    object.split()
                    print(player_score.score)

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
