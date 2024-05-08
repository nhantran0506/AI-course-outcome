from Algorithm import Algorithm

class GREEDY_BEST_FIRST(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        self.frontier = []
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        self.frontier.append(initialstate)

        while len(self.frontier) > 0:
            lowest_index = 0
            for i in range(len(self.frontier)):
                if self.frontier[i].h < self.frontier[lowest_index].h:
                    lowest_index = i

            lowest_node = self.frontier.pop(lowest_index)

            if lowest_node.equal(goalstate):
                return self.get_path(lowest_node)

            self.explored_set.append(lowest_node)
            neighbors = self.get_neighbors(lowest_node)

            for neighbor in neighbors:
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor) or neighbor in self.explored_set or neighbor in self.frontier:
                    continue

                neighbor.h = self.manhattan_distance(goalstate, neighbor)
                if neighbor not in self.frontier:
                    self.frontier.append(neighbor)
                    neighbor.parent = lowest_node
        return None
