from collections import deque

# Contoh peta kota
city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

def bfs_shortest_path(city_map, start, goal):
  
    if start == goal:
        return [start]
    
    # Antrian BFS
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()  
        node = path[-1]  

        if node not in visited:
            neighbors = city_map.get(node, [])  
            
            for neighbor in neighbors:
                new_path = path + [neighbor]  
                queue.append(new_path) 
                
                if neighbor == goal:
                    return new_path  
        
            visited.add(node)  

    return None 




start = 'Home'
goal = 'Hospital'
shortest_path = bfs_shortest_path(city_map, start, goal)

print(f"Jalur terpendek dari {start} ke {goal}: {shortest_path}")