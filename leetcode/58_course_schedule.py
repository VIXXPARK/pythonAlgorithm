class Solution:
    	def buildAdjacencyList(self, n, edgesList):
            adjList = [[] for _ in range(n)]
            # c2 (course 2) is a prerequisite of c1 (course 1)
            # i.e c2c1 is a directed edge in the graph
            for c1, c2 in edgesList:
                adjList[c2].append(c1)
            return adjList
            
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
    
            # Each vertex can have 3 different states:
            # state 0   : vertex is not visited. It's a default state.
            # state -1  : vertex is being processed. Either all of its descendants
            #             are not processed or it's still in the function call stack.
            # state 1   : vertex and all its descendants are processed.
            state = [0] * numCourses
    
            def hasCycle(v):
                if state[v] == 1:
                    # This vertex is processed so we pass.
                    return False
                if state[v] == -1:
                    # This vertex is being processed and it means we have a cycle.
                    return True
    
                # Set state to -1
                state[v] = -1
    
                for i in adjList[v]:
                    if hasCycle(i):
                        return True
    
                state[v] = 1
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v):
                    return False
    
            return True

#############################################################################################
class Solution:
        def buildAdjacencyList(self, n, edgesList):
            ...
    
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
            visited = set()
    
            def hasCycle(v, stack):
                if v in visited:
                    if v in stack:
                        # This vertex is being processed and it means we have a cycle.
                        return True
                    # This vertex is processed so we pass
                    return False
    
                # mark this vertex as visited
                visited.add(v)
                # add it to the current stack
                stack.append(v)
    
                for i in adjList[v]:
                    if hasCycle(i, stack):
                        return True
    
                # once processed, we pop it out of the stack
                stack.pop()
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v, []):
                    return False
    
            return True


##############################################################################################
class Solution:
        def buildAdjacencyList(self, n, edgesList):
    				...
    
        def topoBFS(self, numNodes, edgesList):
            # Note: for consistency with other solutions above, we keep building
            # an adjacency list here. We can also merge this step with the next step.
            adjList = self.buildAdjacencyList(numNodes, edgesList)
    
            # 1. A list stores No. of incoming edges of each vertex
            inDegrees = [0] * numNodes
            for v1, v2 in edgesList:
                # v2v1 form a directed edge
                inDegrees[v1] += 1
    
            # 2. a queue of all vertices with no incoming edge
            # at least one such node must exist in a non-empty acyclic graph
            # vertices in this queue have the same order as the eventual topological
            # sort
            queue = []
            for v in range(numNodes):
                if inDegrees[v] == 0:
                    queue.append(v)
    
            # initialize count of visited vertices
            count = 0
            # an empty list that will contain the final topological order
            topoOrder = []
    
            while queue:
                # a. pop a vertex from front of queue
                # depending on the order that vertices are removed from queue,
                # a different solution is created
                v = queue.pop(0)
                # b. append it to topoOrder
                topoOrder.append(v)
    
                # increase count by 1
                count += 1
    
                # for each descendant of current vertex, reduce its in-degree by 1
                for des in adjList[v]:
                    inDegrees[des] -= 1
                    # if in-degree becomes 0, add it to queue
                    if inDegrees[des] == 0:
                        queue.append(des)
    
            if count != numNodes:
                return None  # graph has at least one cycle
            else:
                return topoOrder
    
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            return True if self.topoBFS(numCourses, prerequisites) else False

##################################################################
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


