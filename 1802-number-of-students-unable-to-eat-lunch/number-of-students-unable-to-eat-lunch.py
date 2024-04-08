class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        k = 0
        while k < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                k = 0
            else:
                x = students.pop(0) 
                students.append(x)
                k += 1
        return len(sandwiches)
                
            