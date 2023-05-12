from itertools import permutations

class RailNetwork():
    min_len = 1
    max_len = 1

    def __init__(self, graph):
        self.graph: list = graph
    
    def setup(self, start_town, end_town, min_stops = 1, max_stops = 10):
        self.start_town = start_town
        self.end_town = end_town
        if min_stops < 1:
            min_stops = 1
        self.min_len = min_stops + 1
        self.max_len = max_stops + 1
    
    def get_distance_by_routes(self, routes) -> int:
        _distance = 0
        r = 0
        while r + 1 < len(routes):
            # pass
            node1 = routes[r]
            node2 = routes[r + 1]
            track = next((track for track in self.graph if track[0] == node1 and track[1] == node2), '')
            if track:
                _distance += int(track[2])
            else:
                # if no track found, return -1 and routes is invalid
                _distance = -1
                break
            r += 1
        if _distance < 0:
            distance = 'NO SUCH ROUTE'
        else:
            distance = int(_distance)
        return distance

    def find_available_routes(self):
        available_routes = {}
        characters = 'ABCDE'
        characters_len = len(characters)
            
        for n_stops in range(self.min_len, self.max_len + 1):
            if n_stops == 2:
                route = self.start_town + self.end_town
                distance = self.get_distance_by_routes(route)
                if distance != 'NO SUCH ROUTE':
                    available_routes[route] = distance
            else:
                all_possible_routes = permutations(characters * characters_len, n_stops - 2)
                for route_tuple in all_possible_routes:
                    route = self.start_town + ''.join(route_tuple) + self.end_town
                    distance = self.get_distance_by_routes(route)
                    if distance != 'NO SUCH ROUTE':
                        available_routes[route] = distance
        return available_routes
    
    def count_available_routes(self):
        return len(self.find_available_routes())

    def find_shortest_route(self):
        routes = self.find_available_routes()
        return min(routes.values())