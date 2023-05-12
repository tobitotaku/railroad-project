

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
        # exit when town2 is reached
        if len(route) > 0 and town2 == route[len(route) - 1]:
            # don't return route if it only has 1 town, i.e. town1 == town2
            if len(route) == 1:
                return ''
            else:
                self.visited_routes.append(route)
                return route
            
        # start route to town1 if route is empty
        if len(route) == 0: route = town1

        # find next town
        vect = self.get_next_track_to_town(route)
        if len(vect) > 1:
            route += vect[1]
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
            self.visited_routes.append(route)
            return route
            
        # start route to town1 if route is empty
        if len(route) == 0: route = town1

        # find next town
        track = self.get_next_track_to_town(route)
        if len(track) > 1:
            route += track[1]
        return self.find_a_route_exact_stops(town1, town2, exact_stops, route)

    def get_next_track_to_town(self, route):
        return next(
            filter(
                lambda vect: 
                    # match next town with last town in route, i.e. AB to BC, C is next town
                    vect[0] == route[len(route) - 1]
                    and not self.track_is_visited(vect[0:2])
                    ,
                self.graph
            ),
            '' # return empty string if no route found
        )

    def track_is_visited(self, route):
        is_visited = route in next(
                        filter(
                            lambda visited_route: 
                                route in visited_route,
                            self.visited_routes
                        ),
                        ''
                    )
        return is_visited

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

