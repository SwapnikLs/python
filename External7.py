def bfs(start_node,graph):
    visited=[]
    queue=[start_node]
    print("breadth first search starting from vertex 2:")
    while queue:
        current=queue.pop()
        if current not in visited:
            visited.append(current)
            print(current,'',end="")
            queue.extend(graph[current])
graph= {2:[0,3],
       3:[1],
       1:[],
       0:[],}
start_node=2
bfs(start_node,graph)