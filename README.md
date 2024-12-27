# Shortest Word Path Finder

## Overview
This application computes the shortest path between two words in a weighted graph, where the words are connected by edges if they differ by one letter and are of the same length. The program implements a graph-based solution using Dijkstra's algorithm, leveraging an adjacency list to represent the graph and a priority queue for efficient pathfinding.

## Features
- **Graph Construction**: Constructs a graph from a dictionary where each vertex represents a word and edges connect words differing by one letter.
- **Weighted Edges**: Edge weights are calculated as the absolute ASCII value difference of the differing letters.
- **Dijkstra's Algorithm**: Utilized to find the shortest path by systematically exploring the graph to minimize total edge weights while ensuring optimal performance.
- **Interactive Query**: Allows repeated user input for start and end words to compute paths without rebuilding the graph.
- **Path Validation**: Ensures start and end words are of the same length and exist in the dictionary.

## Usage
1. Prepare a dictionary file (`Dict.txt`) containing one word per line.
2. Run the program and input the starting and ending words when prompted.
3. The program will display the shortest path and its total weight or indicate that no path exists.

## Key Implementation Details
- **Graph Representation**: 
  - The graph is stored as a dictionary of `Vertex` objects.
  - Each vertex contains:
    - The word it represents.
    - A list of neighbors with associated edge weights.
    - Distance (`d`) and predecessor (`pred`) attributes for Dijkstra's algorithm.
- **Edge Weight Calculation**: Uses the ASCII difference of the differing letters to compute weights.
- **Dijkstra's Algorithm**: 
  - Maintains a priority queue (`heapq`) to process vertices in order of their current shortest path distance.
  - Updates distances and predecessors during edge relaxation to ensure the shortest path is accurately traced.
  - Handles large datasets efficiently, minimizing unnecessary computations through systematic exploration.
- **Efficient Data Structures**: 
  - A set tracks visited vertices to prevent redundant processing.
  - An adjacency list and priority queue facilitate rapid updates and queries.
- **Path Extraction**: Traces back from the ending word using predecessor pointers to reconstruct the shortest path.

## Example
### Input
- **Starting word**: `game`
- **Ending word**: `kite`
### Output
- **Path**: `game > gate > gite > kite`
- **Length**: Calculated as the sum of edge weights.

## File Structure
- **Vertex.py**: Defines the `Vertex` class representing nodes in the graph.
- **shortestWordPathArrayList.py**: Implements graph construction, Dijkstra's algorithm, and pathfinding logic.
- **Dict.txt**: Input dictionary file containing valid words.

## Running the Program
1. Place the `Dict.txt` file in the same directory as the source code.
2. Execute the program and follow the interactive prompts to input words and find paths.
3. Press `q` to quit or any other key to continue querying paths.
