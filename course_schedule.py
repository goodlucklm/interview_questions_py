class CourseSchedule(object):
    def __init__(self):
        self.graph = dict()

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build the graph and compute indegree
        indegree = dict()
        for relation in prerequisites:
            course = relation[0]
            prerequisite = relation[1]
            if not course in self.graph:
                self.graph[course] = []
                indegree[course] = 0
            if not prerequisite in self.graph:
                self.graph[prerequisite] = []
                indegree[prerequisite] = 0
            self.graph[course].append(prerequisite)
            indegree[prerequisite] += 1

        # build the queue of 0 indegree nodes
        zero_indegree = []
        for k in indegree.keys():
            if indegree[k] == 0:
                zero_indegree.append(k)

        # traversal the graph from 0 indegree nodes
        output = []
        count = 0
        while zero_indegree:
            vertice = zero_indegree.pop(0)
            output.append(vertice)
            for v in self.graph[vertice]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    zero_indegree.append(v)
            count += 1

        if count != len(self.graph):
            return False
        return True


if __name__ == '__main__':
    cs = CourseSchedule()
    cs.canFinish(0, [[1,0],[0,1]])





