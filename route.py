

class RailNetwork():

    def __init__(self, graph):
        self.graph: list = graph
        self.visited_routes = []

    def get_distance_by_routes(self, routes) -> int:
        _distance = 0
        r = 0
        while r + 1 < len(routes):
            # pass
            node1 = routes[r]
            node2 = routes[r + 1]
            track = self.get_track(node1, node2)
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
            distance = str(_distance)
        return distance

    def find_a_route_max_stops(self, town1, town2, max_stops, route = ''):
        # exit when after max_stops is reached
        if len(route) == max_stops + 1:
            # return empty string if town2 is not reached
            if len(route) > 0 and town2 != route[len(route) - 1]:
                return ''
            else:
                return route
        # exit when town2 is reached
        if len(route) > 0 and town2 == route[len(route) - 1]:
            # don't return route if it only has 1 town, i.e. town1 == town2
            if len(route) == 1:
                return ''
            else:
                return route
            
        # start route to town1 if route is empty
        if len(route) == 0: route = town1

        # find next town
        vect = self.get_next_town(route)
        if len(vect) > 1:
            route += vect[1]
            self.visited_routes.append(vect)
        return self.find_a_route_max_stops(town1, town2, max_stops, route)
    
    def reset_visited_routes(self):
        self.visited_routes = []

    def count_routes_with_max_stops(self, town1, town2, max_stops):
        has_route = True
        count = 0
        self.reset_visited_routes()
        while has_route:
            route = self.find_a_route_max_stops(town1, town2, max_stops)
            if route:
                count += 1
            else:
                has_route = False
        return count
    
    def find_a_route_exact_stops(self, town1, town2, exact_stops, route = '', ):
        # exit when after exact_stops is reached
        if len(route) > exact_stops + 1:
            return ''

        # exit when town2 is reached
        if len(route) > 0 and town2 == route[len(route) - 1] and len(route) == exact_stops + 1:
            return route
            
        # start route to town1 if route is empty
        if len(route) == 0: route = town1

        # find next town
        vect = self.get_next_town(route)
        if len(vect) > 1:
            route += vect[1]
            self.visited_routes.append(vect)
        return self.find_a_route_exact_stops(town1, town2, exact_stops, route)

    def get_next_town(self, route):
        return next(
            filter(
                # filter by current town and exclude route
                lambda vect: vect[0] == route[len(route) - 1] \
                    and vect not in self.visited_routes,
                self.graph
            ),
            '' # return empty string if no route found
        )

    def count_routes_with_exact_stops(self, town1, town2, exact_stops):
        has_route = True
        count = 0
        self.reset_visited_routes()
        while has_route:
            route = self.find_a_route_max_stops(town1, town2, exact_stops)
            if route:
                count += 1
            else:
                has_route = False
        
    def get_track(self, node1, node2):
        track = ''
        for vect in self.graph:
            if vect[0] == node1 and vect[1] == node2:
                track = vect
        return track

