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
        # print right border
        print("|")

    # print bottom border
    print("-" * (width * 2 + 2))

if __name__ == "__main__":
    state = random_state(20, 30)
    render(state)
