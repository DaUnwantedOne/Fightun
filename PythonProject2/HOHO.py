import pygame
import sys
import random
pygame.init()
death_sawnd = pygame.mixer.Sound("RoblosDS.mp3")
pygame.display.set_caption("BawnsBawns")

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
RED = (255, 0, 0)

font_big = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 36)

def play_gaym():
    hover_width, hover_height = 100, 15
    hover_x = WIDTH // 2 - hover_width // 2
    hover_y = HEIGHT - 40
    hover_speed = 7

    ball_radius = 15
    ball_x = random.randint(ball_radius, WIDTH - ball_radius)
    ball_y = 50
    ball_speed_y = 5
    ball_speed_x = 3

    score = 0
    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hover_x > 0:
            hover_x -= hover_speed
        if keys[pygame.K_RIGHT] and hover_x < WIDTH - hover_width:
            hover_x += hover_speed
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
            ball_speed_x = -ball_speed_x
        if ball_y - ball_radius <= 0:
            ball_speed_y = -ball_speed_y

        if (hover_y < ball_y + ball_radius < hover_y + hover_height and
                hover_x < ball_x < hover_x + hover_width):
            score += 1
            ball_speed_y = -(ball_speed_y + 1)

        if ball_y - ball_radius > HEIGHT:
            death_sawnd.play()
            playing = False
            return score

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (hover_x, hover_y, hover_width, hover_height))
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        score_text = font_small.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

def game_over(score):
    screen.fill(WHITE)

    final_score_text = font_big.render(f"Final Score: {score}", True, BLACK)
    final_score_rect = final_score_text.get_rect(center=(WIDTH // 3, HEIGHT // 4 - 20))
    screen.blit(final_score_text, final_score_rect)

    if score < 10:
        message = "ANG HINA MO, MAN!"
    else:
        message = "WHAT THE PACK?!"

    msg_text = font_big.render(message, True, RED)
    msg_rect = msg_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(msg_text, msg_rect)

    restart_text = font_small.render("AR TO RISTART AND KYU TO KWIT", True, BLACK)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    screen.blit(restart_text, restart_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
while True:
    paynalskur = play_gaym()
    restart = game_over(paynalskur)
    if not restart:
        break
