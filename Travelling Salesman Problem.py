import itertools
import sys
def calculate_distance(coords, order):
    distance = 0
    num_cities = len(order)
    for i in range(num_cities):
        city1 = order[i]
        city2 = order[(i + 1) % num_cities]
        distance += ((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2) ** 0.5
    return distance
def traveling_salesman_brute_force(coords):
    num_cities = len(coords)
    min_distance = sys.maxsize
    min_order = None
    for order in itertools.permutations(range(num_cities)):
        distance = calculate_distance(coords, order)
        if distance < min_distance:
            min_distance = distance
            min_order = order
    return min_order, min_distance
# Example usage
if __name__ == "__main__":
    # Example coordinates of cities (x, y)
    city_coordinates = [(0, 0), (1, 2), (3, 1), (2, 3)]
    min_order, min_distance = traveling_salesman_brute_force(city_coordinates)
    print("Optimal order:", min_order)
    print("Optimal distance:", min_distance)
