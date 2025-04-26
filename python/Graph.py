class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                pass
            else:
                self.graph_dict[start] = [end]

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [path]
        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path



if __name__ == '__main__':
    routes = [
        ("Seoul", "NewYork"),
        ("Seoul", "Toronto"),
        ("Paris", "Toronto"),
        ("Paris", "NewYork"),
        ("Toronto", "NewYork"),
        ("NewYork", "Dubai")
    ]
    route_graph = Graph(routes)

    start = "Seoul"
    end = "NewYork"
    print(route_graph.get_path(start, end))
    print(route_graph.get_shorest_path(start, end))

