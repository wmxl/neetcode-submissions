class Solution:
    # From the image, we can see that to calculate the amount of water trapped at a position, the greater element to the left l and the greater element to the right r of the current position are crucial. The formula for the trapped water at index i is given by: min(height[l], height[r]) - height[i].
    def trap(self, h: List[int]) -> int:
        i, j = 0, len(h)-1
        lmax, rmax = h[i], h[j]
        s = 0
        print(i)
        print(j)
        while i < j:
            if lmax >= rmax:
                j -= 1
                add = max(0, rmax - h[j])
                s += add
                rmax = max(rmax, h[j])
            else:
                i += 1
                add = max(0, lmax - h[i]) 
                s += add
                lmax = max(lmax, h[i])
            print(f'add:{add} i:{i} j:{j} lmax:{lmax} rmax:{rmax}')
        return s