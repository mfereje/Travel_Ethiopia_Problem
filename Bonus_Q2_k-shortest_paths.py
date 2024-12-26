import heapq


def dijkstra(cities, roads, start_city, goal_city):
    """
    Standard Dijkstra's Algorithm to find the shortest path from start_city to goal_city.
    """
    pq = [(0, start_city, [])]
    visited = set()

    while pq:
        current_cost, current_city, path = heapq.heappop(pq)


        if current_city == goal_city:
            return path + [current_city], current_cost

        if current_city in visited:
            continue

        visited.add(current_city)


        for neighbor, distance in roads.get(current_city, []):
            if neighbor not in visited:
                heapq.heappush(pq, (current_cost + distance, neighbor, path + [current_city]))

    return [], float('inf')


def yen_k_shortest_paths(cities, roads, start_city, goal_city, k):

    first_path, first_cost = dijkstra(cities, roads, start_city, goal_city)
    if not first_path:
        return [], []

    k_shortest_paths = [(first_path, first_cost)]
    potential_paths = []

    for i in range(1, k):

        for j in range(len(first_path) - 1):
            blocked_roads = roads.copy()
            u, v = first_path[j], first_path[j + 1]


            blocked_roads[u] = [(neigh, dist) for neigh, dist in blocked_roads[u] if neigh != v]


            path, cost = dijkstra(cities, blocked_roads, start_city, goal_city)
            if path:
                potential_paths.append((path, cost))


        if potential_paths:
            potential_paths.sort(key=lambda x: x[1])
            next_path, next_cost = potential_paths.pop(0)
            k_shortest_paths.append((next_path, next_cost))
            potential_paths.clear()
    return k_shortest_paths

# Example Usage
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

start_city = 'Addis Ababa'
goal_city = 'Mekelle'
roads['Addis Ababa'].append(('Gondar', 400))
roads['Gondar'].append(('Addis Ababa', 400))
k = 2

k_shortest_paths = yen_k_shortest_paths(cities, roads, start_city, goal_city, k)


for idx, (path, cost) in enumerate(k_shortest_paths, 1):
    print(f"Path {idx}: {path} with cost {cost}")
