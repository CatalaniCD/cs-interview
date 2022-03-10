# DFS

### Depth First Search

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

### Shortest Path usign Depth First Search

```python

def DFS_Shortest_Path(graph, start, end, path = [], shortest = None):
    path = path + [start]
    # path found - termination case
    if start == end:
        return path
    # check if start not in edge
    if not start in graph.keys():
        return None
    # explore nodes
    for node in graph[start]:
        # avoid cycles
        if node not in path: 
            # check if no shortes or path_length < shortest_path
            if shortest == None or len(path) < len(shortest):
                # step until termination case
                newPath = DFS_Shortest_Path(graph, node, end, path, shortest)
                # after termiantion case
                if newPath != None:
                    shortest = newPath                     
    return shortest
    
```

### Cycle Detection with Depth First Search

```python

def DFS_cycle(graph, start, path = []):
    """ Detect Cycles with a Depth First Search """
    # append to path
    path = path + [start]
    
    # graph start
    for node in graph[start]:
        # check if node != path init        
        if node not in path:          
            
            # return true after termination case
            if DFS_cycle(graph, node, path):
                return True      
            
        # return true before termination case
        elif node == path[0]:
            return True
            
```
