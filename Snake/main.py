import pygame
from GeneralData.GeneralData import SCREEN_WIDTH, SCREEN_HEIGHT, draw_grid
from SnakeClass.SnakeClass import Snake
from FoodClass.FoodClass import Food


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace", 16)

    score = 0
    while True:
        clock.tick(10)
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render("Score".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()


main()
