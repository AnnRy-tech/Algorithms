
Flood Fill Algorithm


The flood fill algorithm is used to fill a connected region in a grid (image, matrix, screen) starting from a given point, replacing all adjacent cells of the same value with a new value.

You’ve probably seen it in MS Paint’s bucket tool 🪣.

🔹 Problem Definition

Given:

A 2D grid (image)

A starting cell (sr, sc)

A newColor

Fill all connected cells (up, down, left, right) having the same original color as the starting cell with newColor.


🔹 Key Idea

Store the original color at (sr, sc)

If original color == new color → do nothing

Traverse all 4-directionally connected cells with the same color

Replace them with newColor


🔹 Approaches
1️⃣ DFS (Depth First Search) – Recursive / Stack
2️⃣ BFS (Breadth First Search) – Queue
