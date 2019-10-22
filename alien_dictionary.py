"""
Given a sorted dictionary of alien language, find the order of characters.
e.g: Input ["baa", "abcd", "abca", "cab", "cad"]
Output: b,d,a,c
"""

def dictToGraph(A):
    graph ={}

    for word in A:
        for ch in word:
            if ch not in graph.keys():
                graph[ch] = []

    size = len(graph)
    for i in range(size):
        w1 = arr[i][0]
        if (i+1 < size):
            w2 = arr[i+1][0]
        else:
            w2 = ""
        if (w1 != w2 and len(w2) > 0):
            graph[w1].append(w2)
    return graph

def TopologicalSort(graph):
    TopologicalSortedList = []
    ZeroInDegreeVertexList = []

    inDegree = {u : 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    for k in inDegree:
        if inDegree[k] == 0:
            ZeroInDegreeVertexList.append(k)

    while(ZeroInDegreeVertexList):
        v = ZeroInDegreeVertexList.pop(0)
        TopologicalSortedList.append(v)
        for neighbour in graph[v]:
            inDegree[neighbour] -= 1
            if(inDegree[neighbour] == 0):
                ZeroInDegreeVertexList.append(neighbour)
    return TopologicalSortedList

arr = ["baa", "abcd", "abca", "cab", "cad"]
graph = dictToGraph(arr)
order = TopologicalSort(graph)
print(order)