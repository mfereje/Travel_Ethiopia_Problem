import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue



def ucs(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, [start]))
    visited = set()

    while not pq.empty():
        cost, path = pq.get()
        city = path[-1]

        if city in visited:
            continue

        visited.add(city)

        if city == goal:
            return path, cost

        for neighbor, distance in graph.get(city, []):
            if neighbor not in visited:
                new_cost = cost + distance
                new_path = list(path)
                new_path.append(neighbor)
                pq.put((new_cost, new_path))

    return None, float('inf')



def visualize_graph_with_highlighted_path(roads, ucs_path):
    G = nx.Graph()


    for city, connections in roads.items():
        for connected_city, distance in connections:
            G.add_edge(city, connected_city, weight=distance)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')


    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)  # All roads in gray

    # Highlight the UCS path in green
    if ucs_path:
        ucs_edges = list(zip(ucs_path, ucs_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=ucs_edges, edge_color='green', width=3, style='solid')

    plt.title("Road Network of Ethiopia with Highlighted UCS Path")
    plt.show()


# Input Data
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}


start_city = 'Addis Ababa'
goal_city = 'Mekelle'


ucs_path, ucs_path_cost = ucs(roads, start_city, goal_city)

print(f"Path found by UCS: {ucs_path}")
print(f"Total cost: {ucs_path_cost}")


visualize_graph_with_highlighted_path(roads, ucs_path)
