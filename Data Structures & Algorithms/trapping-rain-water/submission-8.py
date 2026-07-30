class Solution:
    def trap(self, h: List[int]) -> int:
        def calc(i, j):
            min_height = min(h[i],h[j])
            black = 0
            for k in range(i, j+1):
                black += min(min_height, h[k])
            output = min_height * (j - i + 1) - black
            # print(f"min_height:{min_height} i:{i} j:{j} black:{black} output:{output}")
            print(f"i:{i} j:{j} output:{output}")
            return output

        n = len(h)
        i = 0
        left_i = right_i = -1
        # find first left, low and right
        while i < n:
            print(f'first loop, i:{i}')
            if h[i] == 0:
                i += 1
                continue
            left = h[i]
            left_i = i
            while i < n and h[i] >= left:
                left_i = i
                i += 1
            left = h[left_i] # left equal first hill

            low = left
            while i < n and h[i] <= low:
                low = h[i] # until first higher than low, this is finall low, and the first higher is right
                i += 1
            if i < n:
                right = h[i]
                right_i = i
            break

        if left_i == -1 or right_i == -1:
            return 0
        if i == n - 1:
            return calc(left_i, right_i)

        output = 0
        l = [left_i] # l mean trap water left-right endpoint list, l is always big to small
        print(f"l:{l} frist_left_i: {left_i} first_right_i: {right_i}")
        while i < n:
            print(f'2th loop, i:{i} l:{l}')
            # from first right to last right
            while i < n and h[i] >= right:
                right = h[i]
                right_i = i
                i += 1

            if right > h[l[0]]:
                print(f"if {right} > {h[l[0]]}")
                output += calc(l[0], right_i)
                l = [right_i]
            else:
                print("else")
                # append last right's endpoint to l, pop out endpoints smaller than it.
                j = len(l) - 1
                while j >= 0 and h[l[j]] < right:
                    j -= 1
                    l.pop()
                l.append(right_i)
            print(f"l:{l}")
            # find all low and first right
            low = right
            while i < n and h[i] <= low:
                low = h[i]
                i += 1
            if i < n:
                right = h[i]
        print(f"l:{l}")

        for i in range(len(l) - 1):
            output += calc(l[i], l[i+1])
        return output