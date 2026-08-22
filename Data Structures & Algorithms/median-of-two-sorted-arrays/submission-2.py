class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def left_index(mid):
            if mid % 2 == 0:
                return mid // 2 - 1
            else:
                return mid // 2

        def right_index(mid):
            if mid % 2 == 0:
                return mid // 2 + 1
            else:
                return mid // 2 + 1 
        
        def get(a, i):
            if i < 0: 
                return -math.inf
            if i >= len(a):
                return math.inf
            return a[i]
        
        def cal_result():
            if  mid1 % 2 == 1 and mid2 % 2 == 0:
                return nums2[mid2 // 2]
            elif mid1 % 2 == 0 and mid2 % 2 == 1:
                return nums1[mid1 // 2]
            elif mid1 % 2 == 0 and mid2 % 2 == 0:
                return (nums1[mid1 // 2] + nums2[mid2 // 2]) / 2
            else:
                left = []
                if left_index(mid1) >= 0:
                    left.append(nums1[left_index(mid1)])
                if left_index(mid2) >= 0:
                    left.append(nums2[left_index(mid2)])    
                right = [] 
                if right_index(mid2) < len(nums2):
                    right.append(nums2[right_index(mid2)])
                if right_index(mid1) < len(nums1):
                    right.append(nums1[right_index(mid1)])
                
                left_num = left[0] if len(left) == 1 else max(left[0], left[1])
                right_num = right[0] if len(right) == 1 else min(right[0], right[1])
                return (left_num + right_num)/2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        # split point can be index itself or between 2 points
        n1 = (n1 - 1) * 2
        n2 = (n2 - 1) * 2
        l1, r1 = -1, n1 + 1
        l2, r2 = -1, n2 + 1
        # invariable: left and right is always equal in both 2 points
        # exit condition is when 2 mids close enough
        # always in shorter array
        mid1 = (l1 + r1) // 2
        mid2 = (l2 + r2) // 2
        while l1 <= r1:
            if get(nums1, right_index(mid1)) < get(nums2, left_index(mid2)):
                l1 = mid1 + 1                
            elif get(nums1, left_index(mid1)) > get(nums2, right_index(mid2)):
                r1 = mid1 - 1
            elif mid1 % 2 == 0 and nums1[mid1 // 2] < get(nums2, left_index(mid2)):
                l1 = mid1 + 1       
            elif mid1 % 2 == 0 and nums1[mid1 // 2] > get(nums2, right_index(mid2)):
                r1 = mid1 - 1
            elif mid2 % 2 == 0 and nums2[mid2 // 2] < get(nums1, left_index(mid1)):
                r1 = mid1 - 1       
            elif mid2 % 2 == 0 and nums2[mid2 // 2] > get(nums1, right_index(mid1)):
                l1 = mid1 + 1  
            else:
                return cal_result()

            new_mid1 = (l1 + r1) // 2
            mid2 = mid2 - (new_mid1 - mid1)
            mid1 = new_mid1

        # return cal_result()