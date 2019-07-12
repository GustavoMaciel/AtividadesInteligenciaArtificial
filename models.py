class State:

    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, neighbours):
        self.neighbours.extend(neighbour)

    def add_info(path_cost, extimated_cost):
        self.path_cost = path_cost
        self.extimated_cost = extimated_cost

    def calculate_heuristic(self):
        return self.path_cost + self.expected_cost

    def __str__(self):
        return self.name + self.neighbours

    def __repr__(self):
        return self.name
