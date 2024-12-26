from collections import deque


def bfs_all(cities, roads, start_city):
    visited = set()
    queue = deque([(start_city, [start_city], 0)])
    total_cost = 0
    traversal_path = []

    while queue:
        current_city, path, path_cost = queue.popleft()

        if current_city not in visited:
            visited.add(current_city)
            traversal_path = path
            total_cost = path_cost


            for neighbor, distance in roads.get(current_city, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], path_cost + distance))

        # Stop when we have visited all cities
        if len(visited) == len(cities):
            break

    return traversal_path, total_cost



def dfs_all(cities, roads, start_city):
    visited = set()
    stack = [(start_city, [start_city], 0)]
    total_cost = 0
    traversal_path = []

    while stack:
        current_city, path, path_cost = stack.pop()

        if current_city not in visited:
            visited.add(current_city)
            traversal_path = path
            total_cost = path_cost


            for neighbor, distance in roads.get(current_city, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], path_cost + distance))


        if len(visited) == len(cities):
            break

    return traversal_path, total_cost


def traverse_all_cities(cities, roads, start_city, strategy):
    if strategy == 'bfs':
        return bfs_all(cities, roads, start_city)
    elif strategy == 'dfs':
        return dfs_all(cities, roads, start_city)
    else:
        raise ValueError("Invalid strategy. Use 'bfs' or 'dfs'.")


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

# Call strategy='bfs'
bfs_path, bfs_cost = traverse_all_cities(cities, roads, start_city, strategy='bfs')
print(f"BFS Path: {bfs_path} with cost {bfs_cost}")

# Call strategy='dfs'
dfs_path, dfs_cost = traverse_all_cities(cities, roads, start_city, strategy='dfs')
print(f"DFS Path: {dfs_path} with cost {dfs_cost}")
