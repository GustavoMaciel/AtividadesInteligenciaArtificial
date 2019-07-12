def choose_state(frontier):
    return frontier.pop()

def search (initial_state, goal):
    frontier = [initial_state]
    explored = set()

    while True:
        print(frontier)
        if len(frontier) <= 0:
            return False

        current_state = choose_state(frontier)
        explored.add(current_state)

        if current_state == goal:
            return current_state

        for state in current_state.neighbours:
            if state not in frontier and state not in explored:
                frontier.append(state)
