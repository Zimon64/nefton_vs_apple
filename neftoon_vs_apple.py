import pygame
import random
# 5import time

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
leibniz_pic = pygame.image.load('leibniz.jpg')
partialdiff_pic = pygame.image.load('partialdif.png')


class Player(object):
    def __init__(self, x, y, width, hight, life):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.speed = 10
        self.boundary = 30
        self.hitbox = (self.x + 10, self.y, 230, 250)
        self.hp = 99
        self.visible = True
        self.life = life

    def draw(self, window):
        if self.visible:
            if keys[pygame.K_LEFT] and nefton.x > - nefton.boundary - 120:
                nefton.x -= nefton.speed
            elif nefton.x == - nefton.boundary - 120:
                nefton.x = win_width - 120
            elif keys[pygame.K_RIGHT] and nefton.x < win_width + nefton.boundary - 120:
                nefton.x += nefton.speed
            elif nefton.x == win_width + nefton.boundary - 120:
                nefton.x = - nefton.boundary - 100

            if (apple.hitbox[1] - nefton.hitbox[3] <= nefton.hitbox[1] <= apple.hitbox[1] + apple.hitbox[3] and
                    apple.hitbox[0] - nefton.hitbox[2] <= nefton.hitbox[0] <= apple.hitbox[0] + apple.hitbox[2]):
                    nefton.hit()
                    window.blit(partialdiff_pic, (nefton.x + 50, nefton.y + 50))

            self.hitbox = (self.x + 78, self.y, 90, 250)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)

            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0] - (-100), self.hitbox[1], 99, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0] - (-100), self.hitbox[1], 99 - (99 - self.hp), 10))

            pygame.draw.rect(window, (255, 255, 0), (self.hitbox[0] - (-100), self.hitbox[1] - (-15), 99, 10))
            pygame.draw.rect(window, (0, 255, 255), (self.hitbox[0] - (-100), self.hitbox[1] - (-15), 99 - ((99 / 3) * (3 - self.life)), 10))

    def hit(self):

        if nefton.hp > 33:
            nefton.hp -= 33
            apple.y = - 60
            apple.x = random.randint(50, win_width - 50)
        elif nefton.life > 1:
            apple.x = random.randint(50, win_width - 50)
            apple.y = - 60
            apple.count = 0
            nefton.life -= 1
            apple.speed_actual = apple.speed_start
            nefton.hp = 99
        else:
            apple.speed_actual = 0
            nefton.hp = 0
            nefton.visible = False
        print('d/dx')


class Apple(object):
    def __init__(self, x, y, width, hight, radius):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.radius = radius
        self.speed_actual = 7
        self.speed_start = 7
        self.hitbox = (self.x, self.y, 60, 60)
        self.count = 0
        self.count_final = 0
        self.next_speed = 10

    def draw(self, window):

        if apple.y < win_hight:
            apple.y += apple.speed_actual
        elif apple.count == apple.next_speed:
            apple.next_speed = apple.next_speed + 10
            apple.speed_actual += 3
        else:
            apple.y = - 60
            apple.x = random.randint(50, win_width - 50)
            apple.count += 1
        self.hitbox = (self.x, self.y, 60, 60)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)

        if apple.count >= 1 + apple.count_final:
            apple.count_final += 1


class Basket(object):
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight
        self.picture = pygame.image.load('korb.png')

    #def draw(self, window):


def redraw_game_window():
    window.blit(background, (0, 0))
    highscore = font_highscore.render('Highscore: ' + str(apple.count_final), 1, (155, 155, 155))
    text = font_apple.render('Äpfel: ' + str(apple.count), 1, (255, 255, 255))
    hp = font_hp.render('HP: ' + str(nefton.hp), 1, (255, 255, 255))
    window.blit(highscore, (10, 10))
    window.blit(text, (10, 60))
    window.blit(hp, (830, 10))
    nefton.draw(window)
    apple.draw(window)

    window.blit(nefton_pic, (nefton.x, nefton.y))
    window.blit(apple_pic, (apple.x, apple.y))

    if nefton.life == 3:
        window.blit(basket_1.picture, (790, 70))
        window.blit(basket_2.picture, (860, 70))
        window.blit(basket_3.picture, (930, 70))
    elif nefton.life == 2:
        window.blit(basket_2.picture, (860, 70))
        window.blit(basket_3.picture, (930, 70))
    elif nefton.life == 1:
        window.blit(basket_3.picture, (930, 70))
        window.blit(leibniz_pic, (nefton.x, nefton.y))

    pygame.display.update()


nefton = Player(win_width - win_width // 2, win_hight - win_hight // 4, 250, 250, 3)
apple = Apple(random.randint(0, win_width), - 60, 60, 60, 30)
font_apple = pygame.font.SysFont('arial', 50, True, True)
font_highscore = pygame.font.SysFont('arial', 50, True, True)
basket_1 = Basket(60, 60)
basket_2 = Basket(60, 60)
basket_3 = Basket(60, 60)
font_hp = pygame.font.SysFont('arial', 50, True)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if nefton.visible == False:
            print('score: ' + str(apple.count_final))
            run = False

    keys = pygame.key.get_pressed()

    redraw_game_window()
clock.tick(60)
pygame.quit()
