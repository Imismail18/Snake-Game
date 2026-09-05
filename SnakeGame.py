import random
import curses


# Initializes the curses screen and creates the game window.
# Time complexity O(1)
def init_game():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(True)

    screen_hight, screen_width = screen.getmaxyx()
    window = curses.newwin(screen_hight, screen_width, 0, 0)
    window.keypad(True)
    window.timeout(100)

    return screen, window, screen_hight, screen_width


# Creates the snake starting body in the middle of the screen.
# Time complexity O(1)
def create_snake(screen_hight, screen_width):
    start_x = screen_width // 4
    start_y = screen_hight // 2
    
    return [
        [start_y, start_x],
        [start_y, start_x - 1],
        [start_y, start_x - 2],
    ]


# Places food in a free cell on the board.
# Time complexity O(n), where n is the snake length.
def spawn_food(snake, screen_hight, screen_width):
    while True:
        food = [
            random.randint(1, screen_hight - 2),
            random.randint(1, screen_width - 2),
        ]
        if food not in snake: return food


# Checks whether the snake has hit the wall or itself.
# Time complexity O(n), where n is the snake length.
def is_game_over(snake, screen_hight, screen_width):
    head_y, head_x = snake[0]
    is_wall_hit = head_y in (0, screen_hight - 1) or head_x in (0, screen_width - 1)
    is_self_collision = snake[0] in snake[1:],
    
    return is_wall_hit or is_self_collision


# Moves the snake one step in the current direction.
# Time complexity O(n), where n is the snake length.
def move_snake(snake, key):
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN: new_head[0] += 1
    elif key == curses.KEY_UP: new_head[0] -= 1
    elif key == curses.KEY_LEFT: new_head[1] -= 1
    elif key == curses.KEY_RIGHT: new_head[1] += 1

    snake.insert(0, new_head)
    
    return new_head


# Draws the snake and food onto the game window.
# Time complexity O(n), where n is the snake length.
def draw_game(window, snake, food):
    window.erase()
    window.addch(food[0], food[1], curses.ACS_PI)
    for y, x in snake: window.addch(y, x, curses.ACS_CKBOARD)
    window.refresh()


# Runs the main game loop.
# Time complexity O(n) per frame, where n is the snake length.
def main():
    _, window, screen_hight, screen_width = init_game()
    snake = create_snake(screen_hight, screen_width)
    food = spawn_food(snake, screen_hight, screen_width)
    key = curses.KEY_RIGHT

    while True:
        next_key = window.getch()

        if next_key != -1: key = next_key

        if is_game_over(snake, screen_hight, screen_width):
            curses.endwin()
            break

        new_head = move_snake(snake, key)

        if new_head == food: food = spawn_food(snake, screen_hight, screen_width)
        else:
            tail_y, tail_x = snake.pop()
            window.addch(tail_y, tail_x, ' ')

        draw_game(window, snake, food)

    print("Game over! Press any key to exit.")


if __name__ == "__main__":
    try:
        
        main()
        
    except KeyboardInterrupt: curses.endwin()
