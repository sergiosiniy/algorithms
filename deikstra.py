class Deikstras_alg():

    def __init__(self):
        self.graph = dict()
        self.processed = list()
        self.costed = list()
        self.costs = dict()
        self.parents = dict()
        self.infinity = float('inf')
        self.nodescount = 0
        
        
        node = input('Input node name (empty for run algorithm):')
        while node:
            self.graph[node] = dict()
            self.nodescount += 1
            neighbor = input('Node neighbor name (empty for end input): ')
            while neighbor:
                neighbor_weight = None
                while not neighbor_weight:
                    neighbor_weight = int(input("Input weight (can't be empty): "))
                    if neighbor_weight < 0:
                        neighbor_weight = None
                        print("Deikstra's algorithm cant calculate shortest way for negative values!!")
                else:
                    self.graph[node][neighbor] = neighbor_weight
                    if self.nodescount < 2:
                        self.costs[neighbor] = neighbor_weight
                        self.parents[neighbor] = node
                        self.costed.append(neighbor)
                    else:
                        if neighbor not in self.costed:
                            self.costs[neighbor] = self.infinity
                            self.parents[neighbor] = None
                neighbor = input('Node neighbor name (empty for end input): ')
            node = input('Input node name (empty for run algorithm):')
        print("\nCount of nodes: %s" % (self.nodescount,))


    def find_lowest(self, costs):
        lowest_cost = self.infinity
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node


    def find_shortest_way(self):
        node = self.find_lowest(self.costs)
        while node:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest(self.costs)
        return self.costs['finish']


if __name__ == '__main__':
    deikstra = Deikstras_alg()
    print("The shortest way is: ",deikstra.find_shortest_way())
    
