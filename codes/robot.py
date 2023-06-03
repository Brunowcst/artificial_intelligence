import random

class Grid:
    """
    """
    def __init__(self, width, height=None, obstacles=0, obs = None):
        """
        """
        if height == None:
            height = width
        self.dimension = (width, height)
        self.create_nodes()
        self.obstacles = self.create_obstacles(obstacles)
        self.remove_obstacles()
        self.create_edges()
        
    def create_nodes(self):
        """
        """
        width, height = self.dimension
        self.nodes = {}

        count = 1
        for i in range(1, width + 1):
            for j in range(1, height + 1):
                self.nodes[(i, j)] = (count, "(%d,%d)" % (i, j))
                count += 1

    def create_edges(self):
        """
        """
        width, height = self.dimension
        self.edges = []

        for (i, j) in self.nodes:
            delta = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
            for (a, b) in delta:
                if (a, b) in self.nodes:
                    x, xi = self.nodes[(i, j)]
                    y, yi = self.nodes[(a, b)]
                    self.edges.append((x, y, "%s>%s" % (xi, yi)))

    def create_obstacles(self, num_obstacles):
        width, height = self.dimension
        obstacles = []

        while len(obstacles) < num_obstacles:
            (x, y) = self.gera_rand(num_obstacles)
            if (x, y) not in obstacles:
                obstacles.append((x, y))
        
        return obstacles
    
    def gera_rand(self, num_obstacles):
        width, height = self.dimension

        for i in range(num_obstacles):
            x = random.randint(1, width)
            y = random.randint(1, height)
        return (x,y)

    def remove_obstacles(self):
        obstacle_nodes = list(self.obstacles)
        for (i, j) in obstacle_nodes:
            if (i, j) in self.nodes:
               del self.nodes[(i, j)]

    def to_tgf(self):
        """
        """
        content = []
        for (i, j) in self.nodes:
            node_id, node_info = self.nodes[(i, j)]
            content.append("%d %s" % (node_id, node_info))
        content.append('#')
        for (i, j, info) in self.edges:
            content.append("%d %d %s" % (i, j, info))
        return '\n'.join(content)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        w, h, obstacles = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        g = Grid(w, h, obstacles)
        print(g.to_tgf())
