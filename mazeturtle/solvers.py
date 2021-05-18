def bfs_solver(self, start, goal):
    '''
    Shortest Path Breadth First Search Algorithm
    Parameters:
        self (Maze): maze class
        start (int): starting vertex
        goal (int): ending vertex
    '''
    visited = [False] * self.total
    queue = [[start]]
    parent = {0:-1}
    prev = 0

    if start != goal:
        # While there are still vertices to visit
        while queue:
            path = queue.pop(0)
            v = path[-1]

            if (parent[v] != -1): # Go to parent before drawing next vertex
                if (v not in self.maze.graph[prev]): # Only for non neighboring vertices
                    self.turtle.up()
                    self.turtle.goto(((parent[v] % self.rows) - 0.5 * self.rows) * self.scale,
                                    ((parent[v] // self.rows) - 0.5 * self.columns) * self.scale)
                    self.turtle.down()

                self.turtle.goto(((v % self.rows) - 0.5 * self.rows) * self.scale,
                                ((v // self.rows) - 0.5 * self.columns) * self.scale)
                prev = v
            
            # If current node is not visited
            if not visited[v]:
                w = self.maze.graph[v]
                
                # Append neighbors to queue
                for u in w:
                    solution = list(path)
                    parent[u] = v # Save this vertex's parent
                    solution.append(u)
                    queue.append(solution)
                    
                    # Check if neighbor vertex is goal
                    if u == goal:
                        self.turtle.goto(((u % self.rows) -0.5 * self.rows) * self.scale,
                                        ((u // self.rows) -0.5 * self.columns) * self.scale)
                        return solution # Solved!

                visited[v] = True
        
        print("ERROR: No solution exists")
        return []
    
    else:
        print("ERROR: No solution exists")
        return []