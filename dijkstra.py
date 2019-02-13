from collections import defaultdict 
 
class Graph: 

    def minDistance(self,dist,queue): 
        minimum = float("Inf") 
        min_index = -1

        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 

    def printPath(self, parent, j): 
        
        if parent[j] == -1 : 
            print (j, end=" ")
            return
        self.printPath(parent , parent[j]) 
        print (j, end=" ")
        
    def printSolution(self, dist, parent, src): 
        i= int(input("Enter the destination: "))
        if i>int(len(dist)-1):
            i=len(dist)-1
        print("Vertex \t\tDistance from Source\tPath") 
        print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i]), end=" ")
        self.printPath(parent,i)


    def dijkstra(self, graph, src): 

        row = len(graph) 
        col = len(graph[0]) 

        dist = [float("Inf")] * row 

        parent = [-1] * row 

        dist[src] = 0

        queue = [] 
        for i in range(row): 
            queue.append(i)                         
            
        while queue: 

            u = self.minDistance(dist,queue) 
     
            queue.remove(u) 

            for i in range(col): 

                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 

        print(parent)

        self.printSolution(dist, parent, src) 

g= Graph() 

def dijkstra(matrix, n, src):
    cost = [[0 for x in range(n)] for x in range(1)]
    visited = []
    visited.append(src)
    elepos = 0
    for j in range(n):
        cost[0][j] = matrix[src][j]
    mini = 999
    for x in range(n - 1):
        mini = 999
        for j in range(n):
            if cost[0][j] <= mini and j not in visited:
                mini = cost[0][j]
                elepos = j
        visited.append(elepos)
        for j in range(n):
            if cost[0][j] > cost[0][elepos] + matrix[elepos][j]:
                cost[0][j] = cost[0][elepos] + matrix[elepos][j]
    print("The visited nodes are", visited)
    print("The cost to various vertices in order", cost)
    

def main():
    print("Dijkstras algorithm graph using matrix representation \n")
    n = int(input("Enter number of vertices"))
    # print("enter the values of the matrix")
    matrix = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(input("enter the values of the matrix"))
    print(matrix)
    src = int(input("Enter the source vertex"))
    dijkstra(matrix, n, src)
    g.dijkstra(matrix,src)

main()
