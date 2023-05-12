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

    def test_find_route_CDC(self):
        self.assertEqual(self.railnetwork.find_a_route('C', 'C', 3), 'CDC')

    def test_find_route_CEBC(self):
        self.assertEqual(self.railnetwork.find_a_route('C', 'C', 3, ['CD8']), 'CEBC')

if __name__ == '__main__':
    unittest.main()

print