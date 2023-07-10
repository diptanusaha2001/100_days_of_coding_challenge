class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        l, r = 0, len(nums) - 1

        while (l <= r):
            mid = l + (r - l) // 2
            if (nums[mid] < target):
                l = mid + 1
            elif (nums[mid] > target):
                r = mid - 1
            else:
                r1 = mid + 1
                l1 = mid - 1
                if (l1 >= l and r1 <= r and nums[r1] == target and nums[l1] != target):
                    start = l
                    l = mid
                elif (l1 >= l and r1 <= r and  nums[l1] == target and nums[r1] != target):
                    end = r
                    r = mid
                else:
                    if (nums[l] == nums[r] == target):
                        return [l, r]
                    elif (nums[l] != target):
                        l += 1
                    elif (nums[r] != target):
                        r -= 1
        return [start, end]
            
         
