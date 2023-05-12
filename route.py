

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

    def find_a_route(self, town1, town2, max_stops, visited_routes = [], route = ''):
        # merge once visited_routes from external parameter
        if len(visited_routes) > 0:
            self.visited_routes += visited_routes

        # exit when after max_stops is reached
        if len(route) == max_stops + 1:
            # return empty string if town2 is not reached
            if len(route) > 0 and town2 != route[len(route) - 1]:
                return ''
            else:
                return route
        # exit when town2 is reached
        if len(route) > 0 and town2 == route[len(route) - 1]:
            return route
            
        # set current_town to town1 if current_town is empty
        if len(route) == 0: route = town1

        # find next town
        vect = next(
            filter(
                # filter by current town and exclude route
                lambda vect: vect[0] == route[len(route) - 1] \
                    and vect not in self.visited_routes,
                self.graph
            ),
            '' # return empty string if no route found
        )
        if len(vect) > 1:
            route += vect[1]
            self.visited_routes.append(vect)
        return self.find_a_route(town1, town2, max_stops, [], route)
    
    def count_routes_with_max_stops(self, town1, town2, max_stops, ):
        has_route = True
        count = 0
        while has_route:
            route = self.find_a_route(town1, town2, max_stops, self.visited_routes)
            if len(route) > 0:
                count += 1
            else:
                has_route = False
        return count
        
    def get_track(self, node1, node2):
        track = ''
        for vect in self.graph:
            if vect[0] == node1 and vect[1] == node2:
                track = vect
        return track

