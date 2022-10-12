# ----------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 4 - Implement astar and some heuristics
#
# Author(s):
# ----------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation

Your task for homework 4 is to implement:
1.  astar
2.  single_heuristic
3.  better_heuristic
4.  gen_heuristic
"""
import data_structures



def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    # Enter your code here and remove the pass statement below
    closed = set()  # keep track of our explored states
    fringe = data_structures.PriorityQueue()  # for ucs, the fringe is a PriorityQueue
    state = problem.start_state()
    root = data_structures.Node(state, None, None)
    fringe.push(root, 0)
    while not fringe.is_empty():
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.solution()  # we found a solution
        if node.state not in closed:  # we are implementing graph search
            closed.add(node.state)
            for child_state, action, action_cost in problem.expand(node.state):
                all_cost = action_cost + node.cumulative_cost 
                f = all_cost + heuristic(child_state, problem)
                child_node = data_structures.Node(child_state, node, action,all_cost)
                fringe.push(child_node, f)
    return None  # Failure -  no solution was found


def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*.
    Running A* with this null heuristic, gives us uniform cost search
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def single_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return:
    """
    # Enter your code here and remove the pass statement below
    if problem.is_goal(state):
        return 0
    x= manhattan_distance(state[0],state[1][0])
    
    return x


def better_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    if problem.is_goal(state):
        return 0
    x= dest(state[0],state[1][0],problem.cost) 

    return x


def gen_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    if problem.is_goal(state):
        return 0
    x= dest(state[0],state[1][0],problem.cost) 
    return x
def manhattan_distance(sammy, medal) :
    x, y = sammy
    a, b = medal
    h = x-a
    v = y-b
    cost = abs(h) + abs(v)  
    return cost


def dest (sammy,medal,carrot_cost) :
    x, y = sammy
    a, b = medal
    h = x-a
    v = y-b
    cost = 0
    if h > 0:
        cost += h * carrot_cost["W"]
    else:
        cost += abs(h) * carrot_cost["E"]
    if v > 0:
        cost += v * carrot_cost["N"]
    else:
        cost += abs(v) * carrot_cost["W"]
    return cost


