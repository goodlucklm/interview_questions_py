class CourseScheduleII(object):
    def __init__(self):
        self.graph = dict()

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # build the graph and compute indegree
        indegree = [0] * numCourses
        for relation in prerequisites:
            course = relation[1]
            prerequisite = relation[0]
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
        for i, v in enumerate(indegree):
            if v == 0:
                zero_indegree.append(i)

        # traversal the graph from 0 indegree nodes
        output = []
        count = 0
        while zero_indegree:
            vertice = zero_indegree.pop(0)
            output.append(vertice)
            if vertice in self.graph:
                for v in self.graph[vertice]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        zero_indegree.append(v)
            count += 1

        if count != numCourses:
            return []
        return output


if __name__ == '__main__':
    cs = CourseScheduleII()
    print 'result is', cs.findOrder(3,[1,0])