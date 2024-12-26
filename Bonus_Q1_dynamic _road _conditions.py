import heapq


def dijkstra(cities, roads, start_city, goal_city):

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


def block_road(roads, city1, city2):

    if city1 in roads:
        roads[city1] = [conn for conn in roads[city1] if conn[0] != city2]
    if city2 in roads:
        roads[city2] = [conn for conn in roads[city2] if conn[0] != city1]


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

# Block a road (e.g., Addis Ababa to Bahir Dar)
block_road(roads, 'Addis Ababa', 'Bahir Dar')
roads['Addis Ababa'].append(('Gondar', 400))
roads['Gondar'].append(('Addis Ababa', 400))

print("Roads after blocking:", roads)


print("Checking connectivity from", start_city, "to", goal_city)
dijkstra_path, dijkstra_cost = dijkstra(cities, roads, start_city, goal_city)
if dijkstra_path:
    print(f"Dijkstra Path (after road blocked): {dijkstra_path} with cost {dijkstra_cost}")
else:
    print("No path found after road block.")
