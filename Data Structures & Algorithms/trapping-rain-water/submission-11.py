class Solution:
    def trap(self, h: List[int]) -> int:
        def calc(i, j):
            min_height = min(h[i],h[j])
            black = 0
            for k in range(i, j+1):
                black += min(min_height, h[k])
            return min_height * (j - i + 1) - black

        n = len(h)
        i = 0
        # find first valley that can trap water
        while i < n - 1 and h[i+1] >= h[i]:
            i += 1
        left = i
        while i < n - 1 and h[i+1] <= h[i]:
            i += 1
        # reached the last one -> no valley found         # this is also why bound=n-1 correct, because we need to find turning point,
        if i >= n - 1:                                    # turning point needs h[i+1] to exist, so last index can never be one
            return 0

        output = 0
        peaks = [left] # peaks mean trap water left-right endpoint list, peaks is always big to small
        while i < n - 1:
            # from first right to last right
            while i < n - 1 and h[i+1] >= h[i]:
                i += 1
            right = i

            # if right is higher than highest left end, calc current and make this one new left end
            if h[right] > h[peaks[0]]:
                output += calc(peaks[0], right)
                peaks = [right]
            else:
                # append last right's endpoint to peaks, pop out endpoints smaller than it.
                while len(peaks) > 1 and h[peaks[-1]] < h[right]:
                    peaks.pop()
                peaks.append(right)

            # find next lowest (valley)
            while i < n-1 and h[i+1] <= h[i]:
                i += 1

        for k in range(len(peaks) - 1):
            output += calc(peaks[k], peaks[k+1])
        return output