from itertools import permutations

class RailNetwork():

    def __init__(self, graph):
        self.graph: list = graph

    def setup(self, start_town, end_town, min_stops, max_stops, visited_routes = []):
        self.start_town = start_town
        self.end_town = end_town
        self.min_len = min_stops + 1
        self.max_len = max_stops + 1
        self.visited_routes = visited_routes
    
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
    
    def reset_visited_routes(self):
        self.visited_routes = []

    # def count_routes_with_max_stops(self):
    #     has_route = True
    #     count = 0
    #     self.reset_visited_routes()
    #     while has_route:
    #         route = self.find_a_route_max_stops(self.start_town, self.end_town, smax_stops)
    #         if route:
    #             count += 1
    #         else:
    #             has_route = False
    #     return count
    
    def find_route(self, route = ''):
        if route \
            and route[0] == self.start_town and route[len(route) - 1] == self.end_town \
            and len(route) > self.min_len and len(route) < self.max_len:
                self.visited_routes.append(route)
                return route
        elif len(route) == self.max_len:
            self.visited_routes.append(route)
            route = ''
        
        # start route to self.start_town if route is empty
        if len(start_track) == 0: route = self.start_town
        if len(end_track) == 0: route = self.end_town

        start_track = self.suggests_track_by_start_town(start_track)
        end_track = self.suggests_track_by_end_town(end_track)
        if len(start_track) > 1 and len(end_track) > 1:
            route = start_track + end_track[1:]
        return self.find_route(route, start_track, end_track)

    def suggests_track_by_start_town(self, route):
        return next(
            filter(
                lambda track: 
                    # match next town with last town in route, i.e. AB to BC, C is next town
                    track[0] == route[len(route) - 1]
                    and not self.track_is_visited(route + track[1])
                    ,
                self.graph
            ),
            '' # return empty string if no route found
        )
    
    def suggests_track_by_end_town(self, route):
        return next(
            filter(
                lambda track:
                    # match next town with last town in route, i.e. AB to BC, C is next town
                    track[1] == route[len(route) - 1]
                    and not self.track_is_visited(route + track[1])
                    ,
                self.graph
            ),
            '' # return empty string if no route found
        )
    
    def track_is_visited(self, route):
        suggested_route = route
        is_visited = next(
                        filter(
                            lambda visited_route:
                                suggested_route == visited_route
                                ,
                            self.visited_routes
                        ),
                        ''
                    )
        
        return is_visited
        
    def get_track(self, node1, node2):
        track = ''
        for vect in self.graph:
            if vect[0] == node1 and vect[1] == node2:
                track = vect
        return track

