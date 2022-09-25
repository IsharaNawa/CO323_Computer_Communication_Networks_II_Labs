import fileinput        #import for file inputs

#defining the main class for the algorithm
class Graph:

    #constructor of the class
    def __init__(self, Vertices: int, graph: list):
        self.Vertices = Vertices
        self.graph = graph
        self.dist = [float("Inf")] * self.Vertices

    #this function will print the output according to the given format
    def formatAndPrintOutput(self, src: int):
        #printing the title
        print("\nBellman-Ford Algorithm Output:")
        
        #for each vertice in the graph
        for i in range(1, self.Vertices):
            #print the shortest distance
            print("Shortest Distance from", src, "to",
                  i+1, ":", int(self.dist[i]))

    #this function perform bellamanford algorithm when an graph is passed.
    def BellmanFordAlgorithm(self, src: int):
        
        self.dist[src - 1] = 0      #define the distance to the source as 0

        #do this for all the vertices otherthan the source
        #hence self.vertices - 1 times
        for i in range(self.Vertices - 1):

            #do this for each edge in the graph and update the distance
            for u, v, w in self.graph:

                isNotInfinity = self.dist[u] != float("Inf")         
                Dist = self.dist[u] + w < self.dist[v]

                #when above two conditions are met, update the new height of v
                if isNotInfinity and Dist:
                    self.dist[v] = self.dist[u] + w

        # Checks the shorter path for each edge, to identify negative-weight cycles
        # If there is a negative-weight cycle, the program will be terminated with an exception

        #do this for each edge and check for negative-weight cycle
        for u, v, w in self.graph:

            #negative-weigh cycle conditions
            isNotInfinity = self.dist[u] != float("Inf")
            Dist = self.dist[u] + w < self.dist[v]
            
            #when both the bools are true, throw an error message to the console
            if isNotInfinity and Dist:
                print("This graph contains a negative-weight cycle!")
                return

        #if there are no any negative-weight cycle print the output to the console
        self.formatAndPrintOutput(src)


# convert adjaceny list into a list of edges
def ConverToEdges(length: int, adjacency: list) -> list:
    myList = []
    for i in range(length):
        for j in range(length):
            if adjacency[i][j] != float("inf") and adjacency[i][j] != 0.0:
                myList.append([i, j, adjacency[i][j]])
    return myList


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


#main function
if __name__ == "__main__":
    dimension, adjacency = fileReading()         #do the file reading and get the dimension and the adjacency matrix
    printGraph(dimension, adjacency)              #print the reading material to the console according to the given format
    edges = ConverToEdges(dimension, adjacency)        #convert the matrix to a list of edges
    myGraph = Graph(dimension, edges)       #making the graph
    myGraph.BellmanFordAlgorithm(src=1)     #do the algorithm and print the results
