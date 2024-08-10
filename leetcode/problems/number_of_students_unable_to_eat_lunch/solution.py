class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(students and sandwiches):
            if (sum(students) == len(sandwiches) and sandwiches[0] == 0) or (sum(students) == 0 and sandwiches[0] == 1):
                return len(students)
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                a = students.pop(0)
                students.append(a)
        return 0