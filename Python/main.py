# ----------------------------------------------------------------------
# Name:        homework2
# Purpose:     Practice writing Python functions
#
# Author(s):
# ----------------------------------------------------------------------
"""
Implement functions to track Sammy's consumption of carrots.

Sammy is an eco-friendly intelligent agent powered by carrots.
His task is to collect medals at various positions in a grid.
Sammy can only move North, South, West or East.
The carrot consumption per step for each direction is given by a
dictionary that is passed to the various functions.
The functions must work with any dictionary specifying the carrot
consumption.
"""

# Constants
NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"
def carrots_to_medal(sammy, medal, carrot_cost):
    """
    Compute the number of carrots that  Sammy consumes to reach the
    given medal.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medal (tuple) representing the position of a given medal
    :param carrot_cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (integer) the number of carrots consumed assuming Sammy
             does not take any unnecessary detours.
    """
    # Enter your code here and remove the pass statement below
    x, y = sammy
    a, b = medal
    h = x-a
    v = y-b
    cost = 0
    if h > 0:
        cost += h * carrot_cost[WEST]
    else:
        cost += abs(h) * carrot_cost[EAST]
    if v > 0:
        cost += v * carrot_cost[NORTH]
    else:
        cost += abs(v) * carrot_cost[SOUTH]
    return cost
    pass

def min_carrots(sammy, medals, carrot_cost):
    """
    Compute the minimum number of carrots that Sammy consumes to reach a
    medal.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medals (set of tuples) containing the positions of all medals
    :param carrot_cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (integer) the number of carrots.
    """
    # Enter your code here and remove the pass statement below
    if not medals:
        return None

    return min(carrots_to_medal(sammy, m, carrot_cost) for m in medals)
    pass
def most_carrots_medal(sammy, medals, carrot_cost):
    """
    Find the medal that Sammy consumes the most carrots to reach.
    :param sammy (tuple) representing the position of Sammy in the grid
    :param medals (set of tuples) containing the positions of all medals
    :param carrot_cost (dictionary) representing the carrot consumption
    per step for each direction
    :return: (tuple) the position of the medal
    """
    # Enter your code here and remove the pass statement below
    if not medals:
        return None
    res = max(medals, key=lambda m: carrots_to_medal(sammy, m, carrot_cost))
    return res
    pass

def main():
    # The main function is used to test the 3 functions.
    carrot_cost1 = {WEST: 1, EAST: 2, SOUTH: 3, NORTH: 4}
    sammy1 = (10, 3)
    print('----------Testing the carrots_to_medal function----------')
    print(carrots_to_medal(sammy1, (3, 1), carrot_cost1))  # 15
    print(carrots_to_medal(sammy1, (0, 8), carrot_cost1))  # 25
    print(carrots_to_medal(sammy1, (10, 6), carrot_cost1)) # 9
    print(carrots_to_medal(sammy1, (14, 3), carrot_cost1)) # 8
    print(carrots_to_medal(sammy1, (13, 7), carrot_cost1)) # 18
    print(carrots_to_medal(sammy1, (10, 3), carrot_cost1)) # 0
    print('----------')
    sammy2 = (2, 2)
    carrot_cost2 = {NORTH: 1, EAST: 2, WEST: 3, SOUTH: 4 }
    print(carrots_to_medal(sammy2, (3, 1), carrot_cost2))   # 3
    print(carrots_to_medal(sammy2, (0, 8), carrot_cost2))   # 30
    print(carrots_to_medal(sammy2, (10, 6), carrot_cost2))  # 32
    print(carrots_to_medal(sammy2, (14, 3), carrot_cost2))  # 28
    print(carrots_to_medal(sammy2, (13, 7), carrot_cost2))  # 42
    print(carrots_to_medal(sammy2, (10, 3), carrot_cost2))  # 20
    print('----------Testing the min_carrots function----------')
    medals1 = {(3, 1), (0, 8), (13, 7), (1, 4), (10, 6), (14, 3)}
    medals2 = {(10, 3), (14, 3), (13, 7)}
    nomedals = set()
    print(min_carrots(sammy1, medals1, carrot_cost1)) # 8
    result = min_carrots(sammy1, nomedals, carrot_cost1)
    print (result is None) # True
    print(min_carrots(sammy1, medals2, carrot_cost1)) # 0
    print(min_carrots(sammy2, medals1, carrot_cost2))  # 3
    result = min_carrots(sammy2, nomedals, carrot_cost2)
    print(result is None)  # True
    print(min_carrots(sammy2, medals2, carrot_cost2))  # 20
    print('-------Testing the most_carrots_medal function-------')
    print(most_carrots_medal(sammy1, medals1, carrot_cost1)) # (0, 8)
    result = most_carrots_medal(sammy1, nomedals, carrot_cost1)
    print(result is None)  # True
    print(most_carrots_medal(sammy1, medals2, carrot_cost1)) # (13, 7)
    print(most_carrots_medal(sammy1, medals2, carrot_cost2)) # (13, 7)

if __name__ == '__main__':
    main()
