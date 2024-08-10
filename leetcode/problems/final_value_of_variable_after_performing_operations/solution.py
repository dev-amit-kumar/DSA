class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for i in operations:
            if "+" in i:
                output += 1
            else:
                output -= 1
        return output