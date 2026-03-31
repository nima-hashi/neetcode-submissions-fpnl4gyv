class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(curr_path):
            if goal_reached(curr_path):
                results.append(curr_path[:])
                return

            for choice in available_choices(curr_path):
                if should_skip(choice, curr_path):
                    continue

                curr_path.append(choice)
                backtrack(curr_path)
                curr_path.pop()

        def goal_reached(curr_path):
            return len(curr_path) == len(nums)

        def available_choices(curr_path):
            return nums  # Always consider full input

        def should_skip(choice, curr_path):
            return choice in curr_path  # Skip used elements

        backtrack([])
        return results
        