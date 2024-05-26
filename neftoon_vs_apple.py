#!/bin/python3

import pygame
import random
import scoreboard
import subprocess
import name_input

subprocess.run(['python', 'name_input'])
name = str(name_input.player_id)

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
leibniz_pic = pygame.image.load('leibniz.png')
partialdiff_pic = pygame.image.load('partialdif.png')
golden_apple_pic = pygame.image.load('goldenl_apple.png')
principia_pic = pygame.image.load('principia.png')


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

            if ((apple.hitbox[1] - nefton.hitbox[3] <= nefton.hitbox[1] <= apple.hitbox[1] + apple.hitbox[3] and
                    apple.hitbox[0] - nefton.hitbox[2] <= nefton.hitbox[0] <= apple.hitbox[0] + apple.hitbox[2]) or
                    (apple_r.hitbox[1] - nefton.hitbox[3] <= nefton.hitbox[1] <= apple_r.hitbox[1] + apple_r.hitbox[3]
                     and apple_r.hitbox[0] - nefton.hitbox[2] <= nefton.hitbox[0] <= apple_r.hitbox[0] +
                     apple_r.hitbox[2]) or (apple_l.hitbox[1] - nefton.hitbox[3] <= nefton.hitbox[1] <=
                                            apple_l.hitbox[1] + apple_l.hitbox[3] and apple_l.hitbox[0] -
                                            nefton.hitbox[2] <= nefton.hitbox[0] <= apple_l.hitbox[0] +
                                            apple_l.hitbox[2]) or (apple_2.hitbox[1] - nefton.hitbox[3] <=
                                                                   nefton.hitbox[1] <= apple_2.hitbox[1] +
                                                                   apple_2.hitbox[3] and apple_2.hitbox[0] -
                                                                   nefton.hitbox[2] <= nefton.hitbox[0] <=
                                                                   apple_2.hitbox[0] + apple_2.hitbox[2])):
                nefton.hit()
                window.blit(partialdiff_pic, (nefton.x + 50, nefton.y + 50))

            elif (golden_apple.hitbox[1] - nefton.hitbox[3] <= nefton.hitbox[1] <= golden_apple.hitbox[1] +
                  golden_apple.hitbox[3] and golden_apple.hitbox[0] - nefton.hitbox[2] <= nefton.hitbox[0] <=
                  golden_apple.hitbox[0] + golden_apple.hitbox[2]):
                nefton.death()
                window.blit(partialdiff_pic, (nefton.x + 50, nefton.y + 50))

            elif (principia.hitbox[1] - nefton.hitbox[3] <= nefton.hitbox[1] <= principia.hitbox[1] +
                  principia.hitbox[3] and principia.hitbox[0] - nefton.hitbox[2] <= nefton.hitbox[0] <=
                  principia.hitbox[0] + principia.hitbox[2]):

                if principia.visible and apple.count % principia.count == 0:
                    principia.toggle_visibility(False)
                    nefton.extra_life()
                    window.blit(leibniz_pic, (nefton.x, nefton.y))

            self.hitbox = (self.x + 78, self.y, 90, 250)
            # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)

            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0] - (-100), self.hitbox[1], 99, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0] - (-100), self.hitbox[1], 99 - (99 - self.hp), 10))

            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0] - (-100), self.hitbox[1] - (-15), 99, 10))
            pygame.draw.rect(window, (0, 255, 255), (self.hitbox[0] - (-100), self.hitbox[1] -
                                                     (-15), 99 - ((99 / 3) * (3 - self.life)), 10))

    @staticmethod
    def hit():

        if nefton.hp > 33:
            nefton.hp -= 33
            apple.y = - 60
            apple.x = random.randint(50, win_width - 50)
            apple_l.x = -59
            apple_r.x = 999
            apple_l.y = apple.y
            apple_r.y = apple.y
            golden_apple.y = -60
            if apple.count >= apple.count_next_apple:
                apple_2.y = apple.y
            # print('d/dx')
        elif nefton.life > 1:
            apple.x = random.randint(50, win_width - 50)
            apple.y = - 60
            apple_2.y = apple.y
            apple_l.y = apple.y
            apple_r.y = apple.y
            golden_apple.y = -60
            apple.count = 0
            nefton.life -= 1
            apple.speed_actual = apple.speed_start
            nefton.hp = 99
            apple.apple_spawn_count = apple.abbruch
            # print('d/dx')
        else:
            apple.speed_actual = 0
            nefton.hp = 0
            nefton.visible = False
            print('\ngame over')

    @staticmethod
    def death():

        apple.speed_actual = 0
        nefton.hp = 0
        nefton.visible = False
        print('\ngame over')

    @staticmethod
    def extra_life():

        nefton.hp = 99

        # print('\nextra life!!!')


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
        self.apple_spawn_count = 3  # vlt. ändern
        self.abbruch = 3  # vlt. ändern
        self.count_final = 0
        self.count_next_apple = 20
        self.next_speed = 10
        self.death_number = 33

    def draw(self, window):

        if apple.y < win_hight:
            apple.y += apple.speed_actual
            if apple.count >= apple.count_next_apple:
                apple_2.y += apple.speed_actual
            apple_l.y += apple.speed_actual
            apple_r.y += apple.speed_actual
            apple_l.x = -59
            apple_r.x = 999
        elif apple.count == apple.next_speed and apple.count <= 120:
            apple.next_speed = apple.next_speed + 10
            apple.speed_actual += 3
        elif apple.count == apple.apple_spawn_count and apple.apple_spawn_count > 0:
            apple.apple_spawn_count += apple.abbruch  # vlt. ändern
            apple.x = nefton.x + 80
            apple.y = - 60
            apple_2.y = apple.y
            apple_l.x = -59
            apple_r.x = 999
            apple_l.y = apple.y
            apple_r.y = apple.y
            apple.count += 1
        elif apple.count >= apple.count_next_apple:
            apple.y = - 60
            apple.x = random.randint(50, win_width - 50)
            apple_2.y = - 65
            apple_2.y += apple.speed_actual
            apple_2.x = random.randint(50, win_width - 500)
            apple_l.y = apple_2.y
            apple_r.y = apple_2.y
            apple_l.x = -59
            apple_r.x = 999
            apple.count += 1
        else:
            apple.y = - 60
            apple.x = random.randint(50, win_width - 50)
            apple_2.y = - 65
            apple_2.x = random.randint(50, win_width - 50)
            apple_l.y = apple_2.y
            apple_r.y = apple_2.y
            apple_l.x = -59
            apple_r.x = 999
            apple.count += 1

        if golden_apple.y <= win_hight and apple.count % golden_apple.death_number == 0 and apple.count > 0:
            golden_apple.y += apple.speed_actual
        else:
            golden_apple.x = random.randint(50, win_width - 50)
            golden_apple.y = - 65

        self.hitbox = (self.x, self.y, 60, 60)
        # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)
        apple_2.hitbox = (apple_2.x, apple_2.y, 60, 60)
        # pygame.draw.rect(window, (0, 255, 0), apple_2.hitbox, 1)
        apple_r.hitbox = (apple_r.x, apple_r.y, 60, 60)
        # pygame.draw.rect(window, (255, 0, 0), apple_r.hitbox, 1)
        apple_l.hitbox = (apple_l.x, apple_l.y, 60, 60)
        # pygame.draw.rect(window, (255, 0, 0), apple_l.hitbox, 1)
        if apple.count % golden_apple.death_number == 0 and apple.count > 0:
            golden_apple.hitbox = (golden_apple.x, apple_l.y, 60, 60)
            pygame.draw.rect(window, (255, 0, 0), golden_apple.hitbox, 1)
        else:
            golden_apple.hitbox = (golden_apple.x, golden_apple.y, 60, 60)

        if apple.count >= 1 + apple.count_final:
            apple.count_final += 1


class Basket(object):
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight
        self.picture = pygame.image.load('korb.png')


class BasketFull(object):
    def __init__(self, width, hight):
        self.width = width
        self.higth = hight
        self.picture = pygame.image.load('korb_voll.png')


class Principia(object):
    def __init__(self, x, y, width, hight, count):
        self.x = x
        self.y = y
        self.count = count
        self.coordinates = (self.x, self.y)
        self.width = width
        self.hight = hight
        self.hitbox = (self.x, self.y, 60, 60)
        self.visible = True

    def draw(self, window):
        if apple.count % self.count == 0 and not apple.count == 0:
            window.blit(principia_pic, (self.x, self.y))

            self.y = win_hight - 150 - principia.hight
            self.hitbox = (self.x, self.y, 60, 60)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)
        elif apple.count % self.count != 0:
            self.visible = True
            self.x = random.randint(60, win_width - 60)
        else:
            self.x = random.randint(60, win_width - 60)

    def toggle_visibility(self, visible):
        self.visible = visible

    def check_collision(self, player_hitbox):
        # Überprüfe, ob es eine Kollision mit dem Spieler-Hitbox gibt
        if (player_hitbox[1] - self.hitbox[3] <= self.hitbox[1] <= player_hitbox[1] + player_hitbox[3] and
                player_hitbox[0] - self.hitbox[2] <= self.hitbox[0] <= player_hitbox[0] + player_hitbox[2]):
            self.toggle_visibility(False)


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
    principia.draw(window)

    window.blit(nefton_pic, (nefton.x, nefton.y))
    window.blit(apple_pic, (apple.x, apple.y))
    window.blit(apple_pic, (apple_2.x, apple_2.y))
    window.blit(apple_pic, (apple_l.x, apple_l.y))
    window.blit(apple_pic, (apple_r.x, apple_r.y))
    window.blit(golden_apple_pic, (golden_apple.x, golden_apple.y))

    if nefton.life == 3:
        window.blit(basket_1.picture, (790, 70))
        window.blit(basket_2.picture, (860, 70))
        window.blit(basket_3.picture, (930, 70))
    elif nefton.life == 2:
        window.blit(basket_voll_1.picture, (790, 70))
        window.blit(basket_2.picture, (860, 70))
        window.blit(basket_3.picture, (930, 70))
    elif nefton.life == 1:
        window.blit(basket_voll_1.picture, (790, 70))
        window.blit(basket_voll_2.picture, (860, 70))
        window.blit(basket_3.picture, (930, 70))
    elif nefton.life == 1 and nefton.hp == 33:
        window.blit(basket_voll_1.picture, (790, 70))
        window.blit(basket_voll_2.picture, (860, 70))
        window.blit(basket_voll_2.picture, (930, 70))
        window.blit(leibniz_pic, (nefton.x, nefton.y))

    pygame.display.update()


nefton = Player(win_width - win_width // 2, win_hight - win_hight // 4, 250, 250, 3)
apple = Apple(random.randint(60, win_width - 60), - 60, 60, 60, 30)
apple_2 = Apple(random.randint(60, win_width - 60), - 60, 60, 60, 30)
apple_l = Apple(-59, -60, 60, 60, 30)
apple_r = Apple(999, -60, 60, 60, 30)
golden_apple = Apple(random.randint(60, win_width - 60), - 60, 60, 60, 30)
font_apple = pygame.font.SysFont('arial', 50, True, True)
font_highscore = pygame.font.SysFont('arial', 50, True, True)
principia = Principia(random.randint(60, win_width - 60), 800, 60, 60, 100)
basket_1 = Basket(60, 60)
basket_2 = Basket(60, 60)
basket_3 = Basket(60, 60)
basket_voll_1 = BasketFull(60, 60)
basket_voll_2 = BasketFull(60, 60)
basket_voll_3 = BasketFull(60, 60)
font_hp = pygame.font.SysFont('arial', 50, True)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if not nefton.visible:

            run = False

    keys = pygame.key.get_pressed()

    redraw_game_window()
clock.tick(60)

pygame.quit()

score = apple.count_final
score_list, top_ten, max_score = scoreboard.scoreboard(name, score)
# print(top_ten.to_string(index=False))

subprocess.run(['python', 'display_highscores.py'])
