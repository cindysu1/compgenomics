from math import inf


def solve_pebbles(grid_file):
    """Code for the "Pebble Beach" problem. This problem involves implementing
    an O(n) dynamic programming algorithm for computing the maximum value of
    the placement of pebbles under the constraint that no pebbles can be
    vertically or horizontally adjacent.

    Args: grid_file (str): a string with the name of the file that contains
          the grid of values. Each line of that file should contain a row
          of four integers, separated by tabs

    Returns: the maximal score for the optimal pebble placements
    """

    # set up board with values in the grid file
    grid = []
    board = open(grid_file, "r")
    for row in board:
        current = [int(value) for value in row.strip().split('\t')]
        grid.append(current)

    # create a list of lists storing the max values for each end pattern for each row
    maxes = []

    # create dict to store values of different conformations, with the values being the columns containing a pebble
    patterns = {0: [], 1: [0], 2: [1], 3: [2], 4: [3], 5: [0,3], 6: [0,2], 7: [1,3]}

    # create a dict where the key is the pattern number and the value is a list of patterns it is compatible with
    compatibility = {0: [0,1,2,3,4,5,6,7], 1: [0,2,3,4,7], 2: [0,1,3,4,5,6], 3: [0,1,2,4,5,7], 4: [0,1,2,3,6],
                     5: [0,2,3], 6: [0,2,4,7], 7: [0,1,3,6]}

    # iterate through all rows in grid
    for i in range(len(grid)):
        # create an array to store the max values for each pattern type to append to the maxes array
        row = []
        # iterate through pattern types
        for j in range(8):
            # row_sum is the sum of the values for the row with the selected pattern
            row_sum = 0
            # adds values at positions with a pebble in the selected pattern
            for position in patterns[j]:
                row_sum += grid[i][position]
            # previous_row is the max value from the i-1 row from a compatible pattern
            previous_row = 0
            for index in compatibility[j]:
                # no row above the first row
                if i == 0:
                    continue
                if maxes[i-1][index] > previous_row:
                    previous_row = maxes[i-1][index]
            # the max value for the given pattern in the given row is the sum of the value and the max previous row
            row.append(previous_row+row_sum)
        maxes.append(row)
    #  Return the maximum value of the placement of pebbles
    return max(maxes[len(grid)-1])



def run_pebbles():
    """Run solve pebbles. You may try to create different grid files to debug
    that match the formatting of grid.txt (tab separated values)

    Note: there is no reporting in this problem, only `solve_pebbles` will
    be evaluated for correctness.
    """

    # max_sample1 = solve_pebbles("sample1.txt")
    # print(f"The max score for this grid is {max_sample1}")

    max_score = solve_pebbles("grid.txt")
    print(f"The max score for this grid is {max_score}")


if __name__ == "__main__":
    """Run run_pebbles(). Do not modify this code"""
    run_pebbles()
