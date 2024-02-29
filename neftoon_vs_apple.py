import pygame
import random
pygame.init()

win_width = 1000
win_hight = 1000

window = pygame.display.set_mode((win_width, win_hight))
white = pygame.color.Color('#FFFFFF')
pygame.display.set_caption('Nefton vs Apple')
clock = pygame.time.Clock()

nefton_pic = pygame.image.load('nefton_250.png')
apple_pic = pygame.image.load('real_apple.png')
background = pygame.image.load('background.jpeg')

apple_count = 0


class Player(object):
    def __init__(self, x, y, width, hight):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.speed = 10
        self.boundary = 30
        self.hitbox = (self.x + 10, self.y, 230, 250)
        self.hp = 99
        self.visible = True

    def draw(self, window):

        self.hitbox = (self.x + 10, self.y, 230, 250)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 3)

        pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 15, 99 * 2, 10))
        pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 15, 99 * 2, 10))

    def hit(self):

        if self.hp > 0:
            self.hp = -33
        else:
            self.visible = False
        print('d/dx')


class Apple(object):
    def __init__(self, x, y, width, hight):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.speed = 7
        self.hitbox = (self.x, self.y, 60, 60)

    def draw(self, window):
        self.hitbox = (self.x, self.y, 60, 60)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 3)


def redraw_game_window():
    window.blit(background, (0, 0))
    text = font_apple.render('Äpfel: ' + str(apple_count), 1, (255, 255, 255))
    window.blit(text, (10, 10))
    nefton.draw(window)
    apple.draw(window)

    window.blit(nefton_pic, (nefton.x, nefton.y))
    window.blit(apple_pic, (apple.x, apple.y))
    pygame.display.update()


nefton = Player(win_width - win_width // 2, win_hight - win_hight // 4, 500, 500)
apple = Apple(random.randint(0, win_width), - 60, 60, 60)
font_apple = pygame.font.SysFont('arial', 50, True, True)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and nefton.x > - nefton.boundary - 120:
        nefton.x -= nefton.speed
    elif nefton.x == - nefton.boundary - 120:
        nefton.x = win_width - 120
    elif keys[pygame.K_RIGHT] and nefton.x < win_width + nefton.boundary - 120:
        nefton.x += nefton.speed
    elif nefton.x == win_width + nefton.boundary - 120:
        nefton.x = - nefton.boundary - 100

    if apple.y < win_hight:
        apple.y += apple.speed
    else:
        apple.y = - 60
        apple.x = random.randint(50, win_width - 50)

    if apple.y == -60:
        apple_count += 1

    redraw_game_window()
clock.tick(60)
pygame.quit()
