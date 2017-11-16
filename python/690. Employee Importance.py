"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if employees is None or len(employees) == 0:
            return 0

        hashmap = {e.id: e for e in employees}
        res = 0
        stack = [hashmap[id]]
        while stack:
            curr = stack.pop()
            res += curr.importance
            for i in curr.subordinates:
                stack.append(hashmap[i])

        return res
