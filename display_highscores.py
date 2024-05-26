import pygame
import csv

pygame.init()

# Lese die Highscores aus der Datei
top_ten = []
with open('score_list.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        top_ten.append({'Nr.': row['Nr.'], 'Name': str(row['Name']), 'Score': int(row['Score']), 'Date': str(row['Date'])})

def display_highscores(top_ten):
    score_window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Highscores')
    score_font = pygame.font.SysFont('arial', 30, True)
    run = True

    while run:
        score_window.fill((0, 0, 0))
        y_offset = 50
        for idx, score in enumerate(top_ten[:10]):
            score_text = score_font.render(f"{idx + 1}. {score['Name']} - {score['Score']} - {score['Date']}", 1, (159, 121, 238))
            score_window.blit(score_text, (50, y_offset))
            y_offset += 40

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

    pygame.quit()

display_highscores(top_ten)
