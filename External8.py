def dfs(start_node,graph):
    visited=[]
    stack=[start_node]
    print("dfs starting from vertex 2:")
    while stack:
        current=stack.pop()
        if current not in visited :
            visited.append(current)
            print(current,'',end="")
            stack.extend(graph[current])
graph={2:[3,0],
       0:[1],
       1:[3,4],
       3:[4],
       4:[],}
start_node=2
dfs(start_node,graph)