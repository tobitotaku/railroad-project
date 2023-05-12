from route import *
# from unittest import *
import unittest


class TestRailNetwork(unittest.TestCase):
    
    def setUp(self) -> None:
        self.graph = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
        self.railnetwork  = RailNetwork(self.graph)

    def tearDown(self) -> None:
        return super().tearDown()

    def test_get_track(self):
        node1 = 'A'
        node2 = 'B'
        track = self.railnetwork.get_track(node1, node2)
        self.assertEqual(track, 'AB5')

    def test_input1(self):
        routes = 'ABC'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), '9')
    
    def test_input2(self):
        routes = 'AD'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), '5')

    def test_input3(self):
        routes = 'ADC'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), '13')

    def test_input4(self):
        routes = 'AEBCD'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), '22')

    def test_input5(self):
        routes = 'AED'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), 'NO SUCH ROUTE')

    def test_route_is_visited_yes(self):
        self.railnetwork.visited_routes = ['CDCDC']
        self.assertEqual(self.railnetwork.route_is_visited('CDC'), True)

    def test_route_is_visited_no(self):
        self.railnetwork.visited_routes = ['CEBC']
        self.assertEqual(self.railnetwork.route_is_visited('CDC'), False)

    # find route CDC, max stops 3
    # def test_find_route_CDC(self):
    #     self.assertEqual(self.railnetwork.find_a_route_max_stops('C', 'C', 3), 'CDC')

    # find route CEBC, max stops 3
    # def test_find_route_CEBC(self):
    #     # route CDC is already visited
    #     self.railnetwork.visited_routes = ['CDC']
    #     self.assertEqual(self.railnetwork.find_a_route_max_stops('C', 'C', 3), 'CEBC')

    # # find route town C to C, max stops 3
    # # test prevent town of origin == town of destination, i.e. result route = 'C' 
    # def test_find_route_C(self):
    #     # route CDC and CEBC is already visited
    #     self.railnetwork.visited_routes = ['CDC', 'CEBC']
    #     self.assertEqual(self.railnetwork.find_a_route_max_stops('C', 'C', 3), '')

    # # count all routes with max stops from town C to C
    # def test_count_routes_C_to_C(self):
    #     self.assertEqual(self.railnetwork.count_routes_with_max_stops('C', 'C', 3), 2)

    # sections: find route A to C, exact stops 4
    # expect route ABCDC
    # def test_find_route_ABCDC(self):
    #     self.assertEqual(self.railnetwork.find_a_route_exact_stops('A', 'C', 4), 'ABCDC')

    # # expect route ADCDC
    # def test_find_route_ADCDC(self):
    #     self.railnetwork.visited_routes = ['AB', 'CD2']
    #     self.assertEqual(self.railnetwork.find_a_route_exact_stops('A', 'C', 4), 'ADCDC')

    # section: count all routes with exact stops 4 from town A to C
    # def test_count_routes_A_to_C(self):
    #     self.assertEqual(self.railnetwork.count_routes_with_exact_stops('A', 'C', 4), 3)

if __name__ == '__main__':
    unittest.main()

print