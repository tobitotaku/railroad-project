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

    def find_all_routes_with_towns(self, towns, route = '', routes: list = []):
        # set start town as initial town
        if len(route) == 0:
            routes = []
            route += self.start_town
        # if route is not empty and route is valid, add route to routes
        if len(route) > 1 \
            and route[0] == self.start_town \
            and route[-1] == self.end_town \
            and len(route) == towns:
                routes.append(route)
                return routes
        # if route is not empty and route is invalid, return routes
        elif len(route) == towns:
            return routes
        i = 0
        while i < len(self.graph):
            next_town = ''
            # if last town in route is the same as the first town in a track, add the second town in the track to route
            if route[-1] == self.graph[i][0]:
                next_town = self.graph[i][1]
            
            # if next town is not empty, find all routes with next town
            if next_town:
                self.find_all_routes_with_towns(towns, route + next_town, routes)
            i += 1
        return routes

    def find_available_routes(self):
        available_routes = {}
        for n in range(self.min_len, self.max_len + 1):
            # find all possible routes with n towns
            all_possible_routes = self.find_all_routes_with_towns(n)
            for route in all_possible_routes:
                distance = self.get_distance_by_routes(route)
                if distance != 'NO SUCH ROUTE':
                    available_routes[route] = distance
        return available_routes
    
    def count_available_routes(self):
        return len(self.find_available_routes())

    # find shortest route where keys are routes and values in dict are distances
    def find_shortest_route(self):
        routes = self.find_available_routes()
        return min(routes.values())
    
    # find routes with distance less than given distance
    def find_routes_by_distance(self, distance):
        routes = self.find_available_routes()
        return filter(lambda route: routes[route] < distance, routes.keys())
    
    # count routes with distance less than given distance
    def count_routes_by_distance(self, distance):
        routes = self.find_routes_by_distance(distance)
        return len(list(routes))
    
