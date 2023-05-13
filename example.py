from route import *

with open('input.txt', encoding="utf-8") as f:
    read_data = f.read().splitlines()
    railroad = RailNetwork(read_data)
    print('Output #1: ' + str(railroad.get_distance_by_routes('ABC')))
    print('Output #2: ' + str(railroad.get_distance_by_routes('AD')))
    print('Output #3: ' + str(railroad.get_distance_by_routes('ADC')))
    print('Output #4: ' + str(railroad.get_distance_by_routes('AEBCD')))
    print('Output #5: ' + str(railroad.get_distance_by_routes('AED')))
    railroad.setup('C', 'C', 1, 3)
    print('Output #6: ' + str(railroad.count_available_routes()))
    railroad.setup('A', 'C', 4, 4)
    print('Output #7: ' + str(railroad.count_available_routes()))
    railroad.setup('A', 'C', 1, 4)
    print('Output #8: ' + str(railroad.find_shortest_route()))
    railroad.setup('B', 'B', 1, 4)
    print('Output #9: ' + str(railroad.find_shortest_route()))
    railroad.setup('C', 'C', 1, 10)
    print('Output #10: ' + str(railroad.count_routes_by_distance(30)))

