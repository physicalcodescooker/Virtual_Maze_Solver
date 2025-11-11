# Python Virtual Maze Solver using DFS algorithm

## Introduction

Maze-solving and path-finding algorithms are one of the fundamental components in real world systems that employ automation techniques. 

In autonomous vehicles, for instance, the algorithm generates a path on the map after being fed the current location and destination which helps the vehicle navigate complex routes efficiently.[^1] These algorithms also play a significant role in optimizing emergency evacuation plans, by devising the shortest escape path through the building.[^2] In operations research, the most effective path for the supply chain is modelled by leveraging different path finders.[^3] 

Thus, algorithms of this nature are not only used by puzzle hobbyists but have far reaching applications in diverse fields, aiding in problems ranging from optimization techniques to automation and research.

In this project, a simple Python program employing Numpy and Matplotlib libraries is devised that generates a random virtual maze and then implements the DFS algorithm to find the path that reaches the end point.

The project is aimed to understand the basic ideas that underly the implementation of such algorithms and as a stepping stone towards more complex projects in Robotics, etc. 

## Depth-First Search Algorithm
DFS is an algorithm used to traverse or go through tree/graph data structures. It doesn't provide the optimal or the shortest path, only the first path discovered by it. A version of depth-first search was investigated in the 19th century by French mathematician Charles Pierre Trémaux.[^4]
Even though this algorithm is not the best employed, it has various domain specific applications, such as in finding a most-likely path, limited-space searching problems in AI, etc. It is also hailed for its simplicity and is a sound introduction to such algorithms. 

The algorithm works by starting traversal at some arbitrary or user defined point in the data and moving in the direction of this branch as far as possible. The traversal stops when the algorithm reaches a pre-defined end-point. 

The node is defined as every point in the data structure while the link between two data points is the edge. The path or each visited node point is recorded by a 'stack' memory. We assume that there occurs in the maze a starting and end point. Apart from that, if there is no edge between two nodes then the algorithm is constrained to not traverse between them.[^5]  In the stack, each node traversed is stored. The basic steps followed by the algorithm is as such:

1. The node address or label of the arbitrary starting point is stored in the stack. The point then traverves to the next node that is linked to it. If this node is not equal to the end point then it is added to the stack and the point continues its journey.
  
2. The point visits all the branches and nodes linked to the one it currently resides in until there is no further edge. The node labels are stacked and the path is created.

3.If the node reaches a point where it is not at the end point and the only node linked to the current node has been previously traversed and present in the stack the algorithm undergoes 'backtracking'. It goes back to the previous node while removing the 'dead end' node from the stack. This ensures that there is no repitition of nodes in the stack and the path created is actually solving the maze.

4.It then follows that branch in a similar manner of stacking and backtracking. This continues until the end point is reached.

The resultant stack is the path devised as each node point in order of traversal. 

## Conclusion 
The DFs algorithm provides a coherent starting point for beginners in the field and as an academic exercise to students. Its elegance lies in the simplicity of its working and straight forward manner of execution.



### References
[^1]: Li-sang Liu, Jia-feng Lin, et al. (02/15/2021). Path Planning for Smart Car Based on Dijkstra Algorithm and Dynamic Window Approach. https://doi.org/10.1155/2021/8881684
[^2]: Occello, Micheal. (2023). Solving optimization problems in emergency evacuation. https://doi.org/10.31130/UD-JST.2023.118ICT
[^3]:Liu, K. (2025). Design of intelligent logistics path planning algorithm for operations research. https://doi.org/10.2478/amns-2025-0232
[^4]:  Even, Shimon. (2011). Graph Algorithms (2nd ed.), Cambridge University Press, pp. 46–48, ISBN 978-0-521-73653-4.
[^5]: Valenzula, Audi. (03/08/2020). Solving mazes with Depth-First Search. https://medium.com/swlh/solving-mazes-with-depth-first-search-e315771317ae
