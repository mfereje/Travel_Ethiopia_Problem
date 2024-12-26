from collections import deque
import heapq


def bfs_all(cities, roads, start_city):
    visited = set()
    queue = deque([(start_city, [start_city], 0)])
    total_cost = 0

    while queue:
        current_city, path, current_cost = queue.popleft()

        if current_city not in visited:
            visited.add(current_city)
            total_cost += current_cost


            for neighbor, distance in roads.get(current_city, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], distance))

        if len(visited) == len(cities):
            break

    return path, total_cost


# DFS for unweighted graph
def dfs_all(cities, roads, start_city):
    visited = set()
    stack = [(start_city, [start_city], 0)]
    total_cost = 0

    while stack:
        current_city, path, current_cost = stack.pop()

        if current_city not in visited:
            visited.add(current_city)
            total_cost += current_cost  # Add the cost of reaching this city

            # Explore all neighbors
            for neighbor, distance in roads.get(current_city, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], distance))

        if len(visited) == len(cities):
            break

    return path, total_cost


# Main traversal function
def traverse_all_cities(cities, roads, start_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').

    Returns:
    - path: List of cities representing the traversal path.
    - cost: Total cost (distance) of the traversal.
    """
    if strategy == 'bfs':
        return bfs_all(cities, roads, start_city)

    elif strategy == 'dfs':
        return dfs_all(cities, roads, start_city)

    else:
        raise ValueError("Invalid strategy. Use 'bfs' or 'dfs'.")


# Example Usage
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510)],
    'Bahir Dar': [('Gondar', 180)],
    'Gondar': [('Mekelle', 300)],
    'Mekelle': []
}

start_city = 'Addis Ababa'

# call with strategy='bfs'
bfs_path, bfs_cost = traverse_all_cities(cities, roads, start_city, strategy='bfs')
print(f"BFS Path: {bfs_path} with cost {bfs_cost}")

# call with  strategy='dfs'
dfs_path, dfs_cost = traverse_all_cities(cities, roads, start_city, strategy='dfs')
print(f"DFS Path: {dfs_path} with cost {dfs_cost}")
