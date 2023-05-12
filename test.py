from route import *
# from unittest import *
import unittest


class TestRailNetwork(unittest.TestCase):
    
    def setUp(self) -> None:
        self.graph = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
        self.railnetwork  = RailNetwork(self.graph)

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

    def test_count_routes_C_to_C(self):
        self.railnetwork.setup('C', 'C', 1, 4)
        self.assertEqual(self.railnetwork.count_available_routes(), 4)

    def test_count_routes_A_to_C(self):
        self.railnetwork.setup('A', 'C', 4, 4)
        self.assertEqual(self.railnetwork.count_available_routes(), 3)

if __name__ == '__main__':
    unittest.main()

print