import random
import time

ALIVE = 1
DEAD = 0

def dead_state(width, height):
    """Construct an empty state with all cells set to DEAD

    Args:
        width (int): width of the state
        height (int): height of the state

    Returns:
        board_state: an array of size width x height, with all cells set to DEAD
    """    
    board_state = [[DEAD for _ in range(height)] for _ in range(width)]

    return board_state

def random_state(width, height):
    """Construct an empty state of size width x height, with all cells set to either DEAD OR ALIVE randomly

    Args:
        width (int): width of the state
        height (int): height of the state

    Returns:
        board_state: an array of size width x height, with all cells set to either DEAD or ALIVE randomly
    """    
    board_state = dead_state(width, height)

    for x in range(width):
        for y in range(height):
            rand = random.random()
            
            if rand >= 0.5:
                board_state[x][y] = DEAD
            else:
                board_state[x][y] = ALIVE

    return board_state

def get_state_height(state):
    """Returns the height of the state

    Args:
        state (array): the state

    Returns:
        height: the height of the state
    """    
    return len(state)

def get_state_width(state):
    """Returns the width of the state

    Args:
        state (array): the state

    Returns:
        height: the width of the state
    """    
    return len(state[0])

def render(state):
    """Pretty prints the current state to the console

    Args:
        state (array): the state
    """    
    height = get_state_height(state)
    width = get_state_width(state)

    # print top border
    print("-" * (width * 2 + 2))

    for y in range(height):
        
        # print left border
        print("|", end="")
        for x in range(width):
            cell = state[y][x]
            if cell == ALIVE:
                # print ALIVE
                print("#", end=" ")
            else:
                # print DEAD
                print(" ", end=" ")
        # print`` right border
        print("|")

    # print bottom border
    print("-" * (width * 2 + 2))

def next_cell_value(coords, state):
    width = get_state_width(state)
    height = get_state_height(state)

    x = coords[0]
    y = coords[1]
    alive_neighbors = 0

    if x >= len(state) or y >= len(state[0]):
        return "Coordinates out of range"

    for x1 in range(max(0, x - 1), min(x + 1, height - 1) + 1):
        for y1 in range(max(0, y - 1), min(y + 1, width - 1) + 1):
            if x1 == x and y1 == y: continue
            if state[x1][y1] == ALIVE:
                alive_neighbors += 1

    # print(f'The number of alive neighbors for cell {coords} is {alive_neighbors}')
    
    if state[x][y] == ALIVE:
        if alive_neighbors <= 1:
            return DEAD
        elif alive_neighbors <= 3:
            return ALIVE
        else:
            return DEAD
    else:
        if alive_neighbors == 3:
            return ALIVE
        else:
            return DEAD
        
def next_board_state(state):
    width = get_state_width(state)
    height = get_state_height(state)

    next_state = dead_state(width, height)

    for x in range(width):
        for y in range(height):
            next_state[x][y] = next_cell_value((x, y), state)

    return next_state

def run_forever(state):
    next_state = state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)

def load_state(filepath):
    with open(filepath, 'r') as f:
        lines = [l.rstrip() for l in f.readlines()]

    height = len(lines)
    width = len(lines[0])
    board = dead_state(height, width)

    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            board[x][y] = int(char)
    return board

if __name__ == "__main__":
    board = load_state('./boards/glider_gun.txt')
    run_forever(board)
