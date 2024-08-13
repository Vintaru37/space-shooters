import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups) # initializes the inherited class
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2() # by default is 0,0
        self.speed = 300

    def update(self, dt):
        # player movement
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]) # keys[pygame.K_RIGHT returns a boolean, int converts True = 1, False = 0
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction # normalizes the diagonal movement
        self.rect.center += self.direction * self.speed * dt

        # player shooting
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print("fire laser")

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

# surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

all_sprites = pygame.sprite.Group()

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
for i in range(20):
        Star(all_sprites, star_surf)

player = Player(all_sprites)

while running:
    dt = clock.tick() / 1000 # delta time in seconds
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # closes the game on hitting the X in the top right corner
            running = False

    # update
    all_sprites.update(dt)

    # draw the game
    display_surface.fill('darkgray')
    
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit() # STOPS ALL THE ACTIONS