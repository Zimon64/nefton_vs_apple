import pygame
import csv


def display_scores(top_ten, name):
    pygame.init()

    top_ten = []
    with open('score_list.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            top_ten.append(
                {'Nr.': row['Nr.'], 'Name': str(row['Name']), 'Score': int(row['Score']), 'Date': str(row['Date'])})

    with open('score_list.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        personal_score = None
        for row in reader:
            if row['Name'] == name:
                personal_score = {'Nr.': None, 'Name': row['Name'], 'Score': int(row['Score']), 'Date': row['Date']}
                break

    score_window = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Highscores')
    score_font = pygame.font.SysFont('arial', 30, True)
    run = True

    while run:
        score_window.fill((0, 0, 0))
        y_offset = 50
        if personal_score:
            personal_text = score_font.render(f"Your Score: {personal_score['Name']} / {personal_score['Score']} / {personal_score['Date']}", 1, (159, 121, 238))
            score_window.blit(personal_text, (50, y_offset))
            y_offset += 40
        for idx, score in enumerate(top_ten[:10]):
            score_text = score_font.render(f"{idx + 1}. {score['Name']} / {score['Score']} / {score['Date']}", 1, (159, 121, 238))
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
