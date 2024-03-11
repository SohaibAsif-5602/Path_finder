import heapq

class DijkstraAgent:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, source, destination):
        priority_queue = [(0, source, [])]
        visited = set()

        while priority_queue:
            (cost, current_node, path) = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)
            path = path + [current_node]

            if current_node == destination:
                return path

            for neighbor, neighbor_cost in self.graph[current_node].items():
                heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor, path))

        return None

if __name__ == "__main__":
    graph = {
        'A': {'B': 3, 'C': 4},
        'B': {'A': 7, 'C': 5, 'D': 3},
        'C': {'A': 1, 'B': 4, 'D': 9},
        'D': {'B': 6, 'C': 4}
    }

    source_node = input("Enter the source node: ")
    destination_node = input("Enter the destination node: ")

    agent = DijkstraAgent(graph)

    optimal_path = agent.dijkstra(source_node, destination_node)

    if optimal_path:
        print(f"Optimal path from {source_node} to {destination_node}: {optimal_path}")
    else:
        print(f"No path found from {source_node} to {destination_node}")
