import curses
import random

def setup_window():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)  
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(True)  
    return win

def main():
    win = setup_window()
    key = curses.KEY_RIGHT
    snake = [[10, 15], [10, 14], [10, 13]]  
    food = [random.randint(1, 18), random.randint(1, 58)]
    win.addch(food[0], food[1], '*')
    
    score = 0
    while True:
        win.addstr(0, 2, f'Score: {score}')
        win.timeout(100 - (len(snake) // 5 + len(snake) // 10) % 10 * 5)
        
        new_key = win.getch()
        key = key if new_key == -1 else new_key
        
        if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            key = curses.KEY_RIGHT
        
        head = [snake[0][0], snake[0][1]]
        if key == curses.KEY_RIGHT:
            head[1] += 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_DOWN:
            head[0] += 1
        
        if head in snake or head[0] == 0 or head[0] == 19 or head[1] == 0 or head[1] == 59:
            break
        
        snake.insert(0, head)
        
        if head == food:
            score += 10
            food = [random.randint(1, 18), random.randint(1, 58)]
            win.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')
        
        win.addch(snake[0][0], snake[0][1], '#')
    
    curses.endwin()
    print(f'Game Over! Your score: {score}')

if __name__ == '__main__':
    main()

