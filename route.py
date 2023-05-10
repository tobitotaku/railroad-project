

class RailNetwork():

    def __init__(self, graph):
        self.graph: list = graph
    
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
        print(f"distance = {distance}")
        return distance

    def get_shortest_route(self, node1, node2):
        track = ''
        for vect in self.graph:
            # todo
            pass
        return track
    
    def get_track(self, node1, node2):
        track = ''
        for vect in self.graph:
            if vect[0] == node1 and vect[1] == node2:
                track = vect
        return track

