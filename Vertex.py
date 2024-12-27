from __future__ import annotations

class Vertex:
    def __init__(self, word: str, distance, pred = None):
        self.word = word
        self.d = distance
        self.pred = pred
        self.neighbors = []

    def __str__(self) -> str:
        return self.word +", " + str(self.neighbors) + ", distance: " + str(self.d)
    
    def __repr__(self) -> str:
        return str(self)
    
    def __lt__(self, other: Vertex):
        return self.d < other.d
    
    def addNeighbor(self, word, weight):
        self.neighbors.append((word, weight))