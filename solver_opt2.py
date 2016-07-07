#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def sum_distance(cities, solution):
    index = 0
    total = 0
    while index < len(solution):
        if index == len(solution) - 1:
            total += distance(cities[solution[index]], cities[solution[0]])
        else:
            total += distance(cities[solution[index]], cities[solution[index + 1]])
        index += 1
    return total

def otp_2(size, path, dist):
    while True:
        count = 0
        for i in xrange(size - 2):
            i1 = i + 1
            for j in xrange(i + 2, size):
                if j == size - 1:
                    j1 = 0
                else:
                    j1 = j + 1
                    if i != 0 or j1 != 0:
                        l1 = dist[path[i]][path[i1]]
                        l2 = dist[path[j]][path[j1]]
                        l3 = dist[path[i]][path[j]]
                        l4 = dist[path[i1]][path[j1]]
                    if l1 + l2 > l3 + l4:
                        new_path = path[i1:j+1]
                        path[i1:j+1] = new_path[::-1]
                        count =1
        if count == 0:
            break
    return path

def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    solution = otp_2(len(solution), solution, dist)
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    solution = solve(cities)
    print_solution(solution)
    total = sum_distance(cities, solution)
    print 'total: ' + str(total)
