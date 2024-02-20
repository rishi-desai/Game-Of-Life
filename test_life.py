import unittest
from life import *

class TestLife(unittest.TestCase):
    
    def test_dead_state(self):
        # Test case for dead_state function
        width = 3
        height = 3
        state = dead_state(width, height)
        expected_state = [[DEAD, DEAD, DEAD],
                          [DEAD, DEAD, DEAD],
                          [DEAD, DEAD, DEAD]]
        self.assertEqual(state, expected_state)
    
    def test_random_state(self):
        # Test case for random_state function
        width = 3
        height = 3
        state = random_state(width, height)
        self.assertEqual(len(state), height)
        self.assertEqual(len(state[0]), width)
    
    def test_get_state_height(self):
        # Test case for get_state_height function
        state = [[ALIVE, DEAD, ALIVE],
                 [DEAD, ALIVE, DEAD]]
        height = get_state_height(state)
        self.assertEqual(height, 2)
    
    def test_get_state_width(self):
        # Test case for get_state_width function
        state = [[ALIVE, DEAD, ALIVE],
                 [DEAD, ALIVE, DEAD]]
        width = get_state_width(state)
        self.assertEqual(width, 3)
    
    def test_next_cell_value(self):
        # Test case for next_cell_value function
        coords = (1, 1)
        state = [[ALIVE, DEAD, ALIVE],
                 [DEAD, ALIVE, DEAD]]
        next_value = next_cell_value(coords, state)
        self.assertEqual(next_value, ALIVE)
    
    def test_next_board_state(self):
        # Test case for next_board_state function
        state = [[ALIVE, DEAD, ALIVE],
                 [DEAD, ALIVE, DEAD],
                 [ALIVE, DEAD, DEAD]]
        next_state = next_board_state(state)
        expected_next_state = [[DEAD, ALIVE, DEAD],
                               [ALIVE, ALIVE, DEAD],
                               [DEAD, DEAD, DEAD]]
        self.assertEqual(next_state, expected_next_state)

if __name__ == "__main__":
    unittest.main()
