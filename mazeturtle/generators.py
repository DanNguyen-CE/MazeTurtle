from random import sample

def dfs_generator(self, v:int, visited:list, road_used:list, parent:int):
        '''
        Recursive Randomized Depth First Search Algorithm with Backtracking
        Parameters:
            self (Maze): maze class
            v (int): current vertex
            visited (list): list of visited vertices
            road_used (list): history of previous path for backtracking
            parent (int): parent of current vertex
        '''
        # Check if there are still vertices to visit
        c = 0
        for i in range(self.total):
            if visited[i]:
                c += 1
        if c == self.total:
            return
        
        # Add edge to graph representation of maze
        if parent != -1 and not visited[v]:
            self.maze.add_edge(parent, v)

        # Mark vertex as visited
        if not visited[v]:
            visited[v] = True

        # Turtle draws toward current vertex
        self.turtle.goto(((v % self.rows)-.5*self.rows)*self.scale,((v // self.rows)-.5*self.columns) * self.scale)
        
        # Track the current edge
        road_used.append([parent, v])
    
        # Choose random available path
        for x in sample(self.graph.graph[v], len(self.graph.graph[v])):
            if not visited[x]:
                dfs_generator(self, x, visited, road_used, v)
    
        # Backtrack through the last visited vertices
        for y in road_used:
            if y[1] == v:
                dfs_generator(self, y[0], visited, road_used, v)

def it_dfs_generator(self, s):
    '''
    Iterative Randomized Depth First Search Algorithm with Backtracking
    Parameters:
        self (Maze): maze class
        s (int): starting vertex
    '''
    visited = [False]*self.total
    road_used = []
    parent = -1
    stack = [s]
    c = 0

    # While there are still vertices to visit
    while len(stack) and c < self.total:
        
        # Pop a vertex from stack
        v = stack[-1]
        stack.pop()

        # Turtle draws toward current vertex
        self.turtle.goto(((v % self.rows)-.5*self.rows)*self.scale,((v // self.rows)-.5*self.columns) * self.scale)

        # Add edge to graph representation of maze
        if parent != -1 and not visited[v]:
            self.maze.add_edge(parent, v)

        if not visited[v]:
            visited[v] = True
            c += 1

        # Track the current edge
        road_used.append([parent, v])
        parent = v

        # Choose random available path
        any_adj = 0
        for w in sample(self.graph.graph[v], len(self.graph.graph[v])):
            if not visited[w]:
                any_adj += 1
                stack.append(w)
                break
        
        # Backtrack through the last visited vertices
        if any_adj == 0:
            for y in road_used:
                if y[1] == v:
                    stack.append(y[0])
                    break
