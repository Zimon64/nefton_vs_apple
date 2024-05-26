import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1000,1000])
base_font = pygame.font.Font(None, 32)
befehl = 'PlayerId: '
player_id = ''

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                player_id = player_id[:-1]
            elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                running = False
            else:
                player_id += event.unicode

    screen.fill((0, 0, 0))
    text_surface_befehl = base_font.render(befehl, True, (159, 121, 238))
    text_surface_player_id = base_font.render(player_id, True, (159, 121, 238))
    screen.blit(text_surface_befehl, (10, 10))
    screen.blit(text_surface_player_id, (10 + text_surface_befehl.get_width(), 10))

    pygame.display.flip()
    clock.tick(60)