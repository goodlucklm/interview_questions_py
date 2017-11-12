class Graph:
    def __init__(self):
        self.graph = dict()  # key: task name, value: list of connected vertices
        self.stack = []

    def addEdge(self, task1, task2):
        if task1 not in self.graph.keys():
            self.graph[task1] = []
        if task2 not in self.graph.keys():
            self.graph[task2] = []
        self.graph[task1].append(task2)

    def topologicalSort(self, taskIndex, taskList, visitedList):
        # marked for visit only once
        visitedList[taskIndex] = True

        # recurse for adjacent vertices
        task = taskList[taskIndex]
        for t in self.graph[task]:
            i = taskList.index(t)
            if not visitedList[i]:
                self.topologicalSort(i, taskList, visitedList)

        # all done, push to stack
        self.stack.insert(0, task)

    def sortTasks(self):
        tasks = self.graph.keys()
        visitedList = [False] * len(tasks)

        for i in range(len(tasks)):
            if not visitedList[i]:
                self.topologicalSort(i, tasks, visitedList)

    def getStack(self):
        return self.stack


if __name__ == '__main__':
    g = Graph()
    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.sortTasks()
    print g.getStack()
