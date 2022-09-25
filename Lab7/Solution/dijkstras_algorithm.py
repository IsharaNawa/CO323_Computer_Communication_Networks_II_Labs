import fileinput    #import for file inputs

#defining the main class for the algorithm
class Graph():

    #constructor of the class
    def __init__(self, Vertices: int, graph: list):
        self.Vertices = Vertices
        self.graph = graph
        self.dist = [float("inf")] * self.Vertices
        self.isDone = [False] * self.Vertices

    #this function will print the output according to the given format
    def formatAndPrintOutput(self, src: int):
        
        print("\nDijkstra's Algorithm Output:")

        #for each vertice in the graph
        for i in range(1, self.Vertices):
            #print the shortest distance
            print("Shortest Distance from", src, "to",
                  i+1, ":", int(self.dist[i]))

    #searching for the vertex with the minimum distance assciated with the edges connected to it
    def currentMinimumDist(self) -> int:
        
        #at first minimum distance is inifity
        currMin = float("inf")

        #do this for all the vertices in the graph
        for v in range(self.Vertices):  

            if not self.isDone[v] and self.dist[v] < currMin: 
                #checking if the current vertex is not delat with and it has a distance less than the current minimum distance

                #if so, update the current minimum distance with the distance
                currMin = self.dist[v]
                #get the index of that so that this vertex can be marked as done
                minIndex = v

        self.isDone[minIndex] = True        #marking the vertex as done
        return minIndex                     #return the index of the vertex

    #this function perform dijkstras algorithm when an graph is passed.
    def dijkstrasAlgorithm(self, src: int):
        
        self.dist[src - 1] = 0      #define the distance to the source as 0

        # get the minimum distance vertex for all the vertices
        for i in range(self.Vertices):
            u = self.currentMinimumDist()

            # for the current vertiex, do this for all the vetices
            for v in range(self.Vertices):

                isNotMinDistance = v != u      #checking if the current vertex is not the minimnum vertex
                isNotDone = not self.isDone[v]      #checking if the currnet vertex is not dealt with
                isLessDist = self.dist[v] > self.dist[u] + self.graph[u][v]     #checking if the distance is less than the currnt distance
                
                #if all those above conditions are met, update the distance to the new value
                if isNotMinDistance and isNotDone and isLessDist:
                    self.dist[v] = self.dist[u] + self.graph[u][v]

        self.formatAndPrintOutput(src)      #finally , print the resutl back to the console

#reading the file
def fileReading() -> tuple:
    fileList = []
    for line in fileinput.input():
        fileList.append(list(map(float, line.split())))
    dimension = int(fileList[0][0])
    adjacencyMatrix = fileList[1:]
    return dimension, adjacencyMatrix


# print the grpah representation to the console
def printGraph(length: int, adjacency: list):
    print("Input Adjacency Matrix length: "+str(length)+"X"+str(length))
    print("Input Adjacency Matrix:")
    for row in adjacency:
        print(row)


if __name__ == "__main__":
    dimenssion, adjacency = fileReading()        #do the file reading and get the dimension and the adjacency matrix
    printGraph(dimenssion, adjacency)       #print the reading material to the console according to the given format
    myGraph = Graph(dimenssion, adjacency)   #making the graph
    myGraph.dijkstrasAlgorithm(src=1)       #do the algorithm and print the results

