import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock =pygame.time.Clock()
    
    dt = 0
    
    # Create groups for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Set the groups as containers for the Player class
    Player.containers = (updatable, drawable)

    # Create asteroids group
    asteroids = pygame.sprite.Group()

    # Set the group as containers for the Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # Set the containers for AsteroidField (only updatable)
    AsteroidField.containers = (updatable,)
    
    # Create player after setting containers
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    # Create the asteroid field
    asteroid_field = AsteroidField()

    # Create the shot group
    shots = pygame.sprite.Group()

    # Set the containers for Shot (only updatable)
    Shot.containers = (updatable, drawable, shots)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        
        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()
            
            # Check for collisions between asteroids and shots
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()  # Split the asteroid instead of just killing it
                    shot.kill()      # Remove the shot
                    break  # No need to check other shots for this asteroid
        
        # Draw all drawable objects
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main()

