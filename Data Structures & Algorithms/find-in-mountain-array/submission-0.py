class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        def findLeftTarget(m):
            l = 0
            r = m
            while l <= r:
                mid = (l + r) // 2
                midVal = mountainArr.get(mid)
                if midVal == target:
                    return mid
                if midVal > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        def findRightTarget(m):
            length = mountainArr.length()
            l = m
            r = length - 1
            
            while l <= r:
                mid = (l + r) // 2
                midVal = mountainArr.get(mid)
                if midVal == target:
                    return mid
                if midVal > target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        length = mountainArr.length()
        l, r = 1, length - 2

        while l <= r:

            mid = (l + r) // 2
            leftVal = mountainArr.get(mid - 1)
            midVal = mountainArr.get(mid)
            rightVal = mountainArr.get(mid + 1)

            if midVal > leftVal and midVal > rightVal: #mountainPeak
                if midVal == target:
                    return mid
                leftSearch = findLeftTarget(mid) 
                if leftSearch != -1:
                    return leftSearch 
                return findRightTarget(mid+1) 
            
            if midVal < leftVal:
                r = mid - 1
            
            else:
                l = mid + 1
        return -1
