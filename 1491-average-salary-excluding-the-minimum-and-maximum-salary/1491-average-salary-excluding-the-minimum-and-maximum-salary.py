class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        totalSalary = sum(salary)

        return (totalSalary - (salary[0] + salary[n-1])) / (n-2)