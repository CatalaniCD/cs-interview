# DFS

```python

def DFS(graph, start, end, path = []):    
    path += [start]
    # path found
    if start == end:
        return path    
    # check if start not in edge
    if not start in graph.keys():
        return None
    # explore nodes
    for node in graph[start]:   
        # avoid cycles
        if node not in path:        
            # step to the next edge until Termination Case
            newpath = DFS(graph, node, end, path)
            # after Termination Case
            if newpath: 
                return newpath  
    return None

```
