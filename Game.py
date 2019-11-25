import pygame
from Fruit import Fruit
from Snake import Snake

# window
WIDTH = 1000
HEIGHT = 800
BG_COLOR = 50, 50, 50
# snake_head
SNAKE_HEAD_START_POSITION = (WIDTH / 2, HEIGHT / 2)
SNAKE_HEAD_DIRECTION = "left"
SNAKE_HEAD_COLOR = 26, 148, 49
# snake_body
SNAKE_BODY_COLOR = 60, 179, 113
# Set game
clock = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Snake")
screen.fill(BG_COLOR)
# Game objects
snake_head = Snake(SNAKE_HEAD_START_POSITION, SNAKE_HEAD_DIRECTION, SNAKE_HEAD_COLOR)
snake_body = []
fruit = Fruit(WIDTH, HEIGHT)


def main():
    run = True
    while run:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
            elif events.type == pygame.KEYDOWN:
                snake_head.keyboard_input(events.key)

        # Erease last step
        if len(snake_body) > 0:
            snake_body[-1].clear(screen, BG_COLOR)
        else:
            snake_head.clear(screen, BG_COLOR)

        # Move then check collision
        move_snake_body()
        snake_head.move()
        body_collision()
        border_collision()
        fruit_collision()

        # Draw Head then body
        snake_head.draw(screen)
        for body in snake_body:
            body.draw(screen)


        fruit.draw(screen)
        pygame.display.flip()
        clock.tick(20)

    pygame.quit()
    quit()


def border_collision():
    if snake_head.x < 0:
        reset_game()
    elif snake_head.x >= WIDTH:
        reset_game()
    elif snake_head.y < 0:
        reset_game()
    elif snake_head.y >= HEIGHT:
        reset_game()


def fruit_collision():
    if snake_head.x == fruit.x and snake_head.y == fruit.y:
        fruit.move(WIDTH, HEIGHT)
        add_body_part()


def body_collision():
    for body in snake_body:
        if snake_head.x == body.x and snake_head.y == body.y:
            reset_game()


def add_body_part():
    if len(snake_body) == 0:
        snake_body.insert(0, Snake((snake_head.x, snake_head.y), snake_head.direction, SNAKE_BODY_COLOR))
    else:
        snake_body.append(Snake((snake_body[-1].x, snake_body[-1].y), snake_head.direction, SNAKE_BODY_COLOR))


def move_snake_body():
    if len(snake_body) == 1:
        snake_body[0].x = snake_head.x
        snake_body[0].y = snake_head.y
    elif len(snake_body) > 1:
        for i in range(len(snake_body)-1, -1, -1):
            if i == 0:
                snake_body[0].x = snake_head.x
                snake_body[0].y = snake_head.y
            else:
                snake_body[i].y = snake_body[i-1].y
                snake_body[i].x = snake_body[i-1].x


def reset_game():
    screen.fill(BG_COLOR)
    snake_head.reset(SNAKE_HEAD_START_POSITION)
    fruit.move(WIDTH, HEIGHT)
    snake_body.clear()


main()
