#BFS

graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
}
def Bfs(graph,s):
    queue=[]
    queue.append(s)
    seen=set()
    seen.add(s)
    while len(queue)>0:
        v=queue.pop(0)
        nodes=graph[v]
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
        print(v)
# Bfs(graph,'B')


def Dfs(graph,s):
    stack=[]
    stack.append(s)
    seen=set()
    seen.add(s)
    while len(stack)>0:
        #弹出最后一个
        v=stack.pop()
        nodes=graph[v]
        for i in nodes:
            if i not in seen:
                stack.append(i)
                seen.add(i)
        print(v)
Dfs(graph,'C')