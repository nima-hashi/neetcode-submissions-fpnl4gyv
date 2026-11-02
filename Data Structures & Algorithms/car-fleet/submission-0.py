class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[p,s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]:
            arrivalTime = (target - p) / s
            if not stack:
                stack.append(arrivalTime)

            elif stack and stack[-1] < arrivalTime:
                stack.append(arrivalTime)
        
        return len(stack)



        