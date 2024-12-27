from __future__ import annotations
from Vertex import Vertex
import heapq
#calculates the weight of an edge given two words of the same length that are one letter apart
def calculateWeight(word1, word2):
    index = 0 
    #find the index of the differing letter
    for i in range(len(word2)):
        #if the letters are different
        if word2[i] != word1[i]:
            #we found the index
            index = i

    weight = abs(ord(word1[index]) - ord(word2[index]))
    return weight

def calculateInfinity(graph: dict[Vertex]):
    infinity = 0
    for vertex in graph.values():
        for neighbor in vertex.neighbors:
            infinity += neighbor[1]
    return infinity

def buildWordGraph(filepath):
    #our Graph is going to use a hash map as the vertex list for 0(1) lookup time
    wordGraph = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            #for each word, make the value in the map a vertex for that corresponding word. 
            #Vertex objects have a list of neighbors. 
            #We will make every distance 0 for now, but will change later to the sum of all edge weights (infinity) when initializing dijkstras
            wordGraph[line] = Vertex(line, 0)
        
    #now, we need to populate edges lists (the AVL trees)
    for word in wordGraph.keys():
        #we will go through each letter in the word and replace it with every letter in the alphabet
        #if that is a valid word, we will add it to the neighbors list
        for i in range(len(word)):
            for j in range(26):
                #use ASCII value to turn int into a character
                char = chr(j+97)
                possibleNeighbor = word[0:i] + char + word[i+1:]
                if possibleNeighbor in wordGraph and possibleNeighbor != word:
                    wordGraph[word].addNeighbor(possibleNeighbor, calculateWeight(word, possibleNeighbor))

    #return the completed graph
    return wordGraph
        
def initializeSingleSource(wordGraph: dict[Vertex], source: str):
    """
        gets the graph ready for dijkstra's by setting each vertex's distance to infinity and pred to None.
        The source's distance will be 0 and also  

    """
    infinity = calculateInfinity(wordGraph)
    for vertex in wordGraph.values():
        if vertex.word != source:
            vertex.d = infinity
            vertex.pred = None
    wordGraph[source].d = 0

def shortestPath(wordGraph: dict[Vertex], startWord: str, endWord: str):
    initializeSingleSource(wordGraph, startWord)
    #initialize an empty priority queue
    pq = []
    #initialize the closed set
    cs = set()
    #add only words of the same length to our heap since we don't need to be concerned with other lengths
    for vertex in wordGraph.values():
        if len(vertex.word) == len(startWord):
            heapq.heappush(pq, vertex)
    #while the queue is not empty
    while pq:
        currentVertex = heapq.heappop(pq)
        #set the currentWord to the actual word field of the vertex that we popped
        currentWord = currentVertex.word
        cs.add(currentVertex)
        if currentWord == endWord:
            # If we've reached the end word, extract and return the path and length
            return extractShortestPath(wordGraph, startWord, endWord)
        for neighbor in currentVertex.neighbors:
            #relax the edges between the neighbors
            if currentVertex.d + neighbor[1] < wordGraph[neighbor[0]].d:
                wordGraph[neighbor[0]].d = currentVertex.d + neighbor[1]
                wordGraph[neighbor[0]].pred = currentVertex
        #update the priority queue with the new d value by calling heapify
        heapq.heapify(pq)
    # If the loop ends without finding the end word, indicate no path was found
    print("No path found")
    return [], 0

def extractShortestPath(wordGraph: dict[Vertex], startWord: str, endWord: str):
    currentWord = endWord
    path = []
    length = 0
    while currentWord != startWord:
        path.append(currentWord)
        currentVertex = wordGraph[currentWord]
        if currentVertex.pred is None:
            print("No path found")
            return [], 0
        length += calculateWeight(currentVertex.word, currentVertex.pred.word)
        currentWord = currentVertex.pred.word
    path.append(startWord)
    path.reverse()
    # print both the path and its length
    print(f"Path: {path}, length: {length}")



#user input implementation
    
#build the graph once before asking the user for input
wordGraph = buildWordGraph("Dict.txt")
key = ""
while key != "q":
    startWord = input("Please enter your starting word: ")
    endWord = input("Please input an ending word of the same length: ")
    if startWord not in wordGraph or endWord not in wordGraph:
        print("Please input two valid words in the dictionary")
        continue
    if len(startWord) != len(endWord):
        print("Words must be the same length")
        continue
    shortestPath(wordGraph, startWord, endWord)
    key = input("Press q to quit. Press any other key to continue: ")