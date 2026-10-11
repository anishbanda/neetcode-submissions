class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((t, i))
                continue
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append((t, i))
        
        return result
            