# BFS

```python
def BFS(graph, start, end, path = [], toPrint = False):
    """ Breadth First Search """
    # create the initial path
    initPath = [start]
    # queue of paths
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        # remove the oldest element in path queue
        tmpPath = pathQueue.pop(0)
        # keep track of last node in the path
        lastNode = tmpPath[-1]
        # check last node is the search element
        if lastNode == end:
            return tmpPath
        for nextNode in graph[lastNode]:
            if nextNode not in tmpPath:
                # add new step to the search paths
                newPath = tmpPath + [nextNode]
                # add new path to eval in the next iteration
                pathQueue.append(newPath)
    
    return None
```
