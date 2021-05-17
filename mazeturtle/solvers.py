def bfs_solver(self, start, goal):
    '''
    Shortest Path Breadth First Search Algorithm
    Parameters:
        self (Maze): maze class
        start (int): starting vertex
        goal (int): ending vertex
    '''
    visited = [False]*self.total
    queue = [[start]]

    if start != goal:
        # While there are still vertices to visit
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            # If current node is not visited
            if not visited[node]:
                w = self.maze.graph[node]
                
                # Append neighbors to queue
                for u in w:
                    solution = list(path)
                    solution.append(u)
                    queue.append(solution)
                    
                    # Check if neighbor vertex is goal
                    if u == goal:
                        return solution # Solved!

                visited[node] = True
        
        print("ERROR: No solution exists")
        return []
    
    else:
        print("ERROR: No solution exists")
        return []