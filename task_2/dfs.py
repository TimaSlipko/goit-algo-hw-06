def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0
    
    while stack:
        current, path = stack.pop()
        nodes_explored += 1
        
        if current == goal:
            return path, nodes_explored
        
        if current in visited:
            continue
            
        visited.add(current)
        
        neighbors = sorted(graph.neighbors(current), reverse=True)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    return None, nodes_explored
