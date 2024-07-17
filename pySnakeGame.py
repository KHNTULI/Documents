import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake settings
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Font
FONT = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

def display_message(msg, color, y_displace=0):
    text_surface = FONT.render(msg, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_displace))
    WINDOW.blit(text_surface, text_rect)
    pygame.display.update()

def display_score(score):
    value = SCORE_FONT.render(f"Score: {score}", True, BLUE)
    WINDOW.blit(value, [0, 0])

def game_loop():
    game_over = False
    game_close = False

    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0

    snake_List = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:
            WINDOW.fill(BLACK)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        WINDOW.fill(BLACK)
        pygame.draw.rect(WINDOW, GREEN, [foodx, foody, SNAKE_SIZE, SNAKE_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(WINDOW, WHITE, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

        display_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 20.0) * 20.0
            length_of_snake += 1

        pygame.time.Clock().tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()

def main_menu():
    menu = True
    while menu:
        WINDOW.fill(BLACK)
        display_message("Welcome to Snake Game", BLUE, -100)
        display_message("Press 1 for Easy", GREEN, -50)
        display_message("Press 2 for Medium", GREEN)
        display_message("Press 3 for Hard", GREEN, 50)
        display_message("Press Q to Quit", RED, 100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    global SNAKE_SPEED
                    SNAKE_SPEED = 10
                    menu = False
                if event.key == pygame.K_2:
                    SNAKE_SPEED = 20
                    menu = False
                if event.key == pygame.K_3:
                    SNAKE_SPEED = 30
                    menu = False
                if event.key == pygame.K_q:
                    menu = False
                    pygame.quit()
                    sys.exit()
    game_loop()

if __name__ == "__main__":
    main_menu()
