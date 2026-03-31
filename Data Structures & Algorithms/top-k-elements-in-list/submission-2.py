class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1. Count frequencies
        count = Counter(nums)
        
        # 2. Create buckets: index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # 3. Gather results from high freq to low
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res