"""node class used for creating new node states"""


class Node():
    """node class used for creating new node states"""
    def __init__(self, environment):
        self.start_state = environment
        self.state_string = ""
        self.empty_spot = None
        self.depth = 0
        self.heuristic = None
        self.path = []

    def find_empty_position(self):
        """find the empty position of the node's state"""
        for i in range(10):
            if self.start_state[i] == 0:
                empty_position = i
                return empty_position
        return None

    def create_state_string(self):
        """create string of integers found in the array for start_state"""
        for number in self.start_state:
            self.state_string += str(number)
        return self.state_string

    def set_path(self, previous_node, new_spot):
        """set the path of the open position"""
        if not previous_node.path:
            self.path.append(str(previous_node.empty_spot) + " swapped for " + str(new_spot))
            return self.path


        self.path.append(str(previous_node.empty_spot) + " swapped for " + str(new_spot))
        self.path.append(previous_node.path)
        return self.path

    def calculate_misplaced_tiles(self):
        """calculates the number of tiles that are out of position and creates a heuristic from
         this number."""
        heuristic = 0
        for tile in range(9):
            if tile == 8:
                if self.start_state[8] != 0:
                    heuristic += 1
            else:
                if self.start_state[tile] != (tile + 1):
                    heuristic += 1

        self.heuristic = heuristic
        return self.heuristic

    def calculate_manhattan_distance(self):
        """Calculates the total cost of tiles that need to be moved to correct position"""
        heuristic = 0
        counter = 0
        for row in range(3):
            for column in range(3):
                current_val = self.start_state[counter]
                counter += 1
                if current_val == 0:
                    continue
                else:
                    correct_row, correct_column = find_correct_position(current_val)
                    out_of_place = abs(row - correct_row) + abs(column - correct_column)
                    heuristic += out_of_place


        self.heuristic = heuristic
        return self.heuristic

def find_correct_position(value):
    """finds the correct position of the current value"""
    if value in (1, 2, 3):
        row = 0
        column = value - 1
        return row, column
    if value in (4, 5, 6):
        row = 1
        column = (value) - 4
        return row, column
    if value in (7, 8):
        row = 2
        column = (value) - 7
        return row, column

    return None
