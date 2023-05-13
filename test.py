from route import *
import unittest


class TestRailNetwork(unittest.TestCase):
    
    def setUp(self) -> None:
        self.graph = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
        self.railnetwork  = RailNetwork(self.graph)

    # test distance route ABC
    def test_input1(self):
        routes = 'ABC'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), 9)
    
    # test distance route AD
    def test_input2(self):
        routes = 'AD'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), 5)

    # test distance route ADC
    def test_input3(self):
        routes = 'ADC'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), 13)

    # test distance route AEBCD
    def test_input4(self):
        routes = 'AEBCD'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), 22)

    # test distance route AED
    def test_input5(self):
        routes = 'AED'
        self.assertEqual(self.railnetwork.get_distance_by_routes(routes), 'NO SUCH ROUTE')

    # test count routes C to C with max 3 stops
    def test_count_routes_C_to_C(self):
        self.railnetwork.setup('C', 'C', 1, 3)
        self.assertEqual(self.railnetwork.count_available_routes(), 2)

    # test count routes A to C with exactly 4 stops
    def test_count_routes_A_to_C(self):
        self.railnetwork.setup('A', 'C', 4, 4)
        self.assertEqual(self.railnetwork.count_available_routes(), 3)

    # test distance of shortest route A to C
    def test_shortest_route_A_to_C(self):
        self.railnetwork.setup('A', 'C', 1, 4)
        self.assertEqual(self.railnetwork.find_shortest_route(), 9)

    # test distance of shortest route B to B
    def test_shortest_route_B_to_B(self):
        self.railnetwork.setup('B', 'B', 1, 4)
        self.assertEqual(self.railnetwork.find_shortest_route(), 9)

    # test count routes C to C with distance less than 30
    def test_count_routes_by_distance_C_to_C(self):
        self.railnetwork.setup('C', 'C', 1, 10)
        self.assertEqual(self.railnetwork.count_routes_by_distance(30), 7)

if __name__ == '__main__':
    unittest.main()
