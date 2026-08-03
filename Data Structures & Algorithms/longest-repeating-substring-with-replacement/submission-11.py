class Solution:
    def characterReplacement(self, a: str, k: int) -> int:
        init_k = k
        n = len(a)
        i = j = 0
        cnt = ma = 0
        pre = a[0]
        while i < n:
            if a[i] == pre:
                cnt += 1
                i += 1
                ma = max(ma, cnt)
            else:
                j = i
                next_pre = a[i] 
                # print(f'j = {j} next_pre:{next_pre} k:{k}')
                while i < n and (a[i] == pre or k > 0):
                    if a[i] != pre:
                        k -= 1
                    cnt += 1
                    i += 1
                    # print(f'loop2 pre:{pre} i:{i} k:{k} cnt:{cnt}')
                if k > 0 and cnt < n:
                    cnt = min(cnt + k, n)
                ma = max(ma, cnt)

                i = j
                cnt = 0
                pre = next_pre
                k = init_k
        i = j = n - 1
        pre = a[n-1]
        cnt = 0
        k = init_k
        while i >= 0:
            if a[i] == pre:
                cnt += 1
                i -= 1
                ma = max(ma, cnt)
            else:
                j = i
                next_pre = a[i]
                # print(f'j = {j} next_pre:{next_pre} k:{k}')
                while i >= 0 and (a[i] == pre or k > 0):
                    if a[i] != pre:
                        k -= 1
                    cnt += 1
                    i -= 1
                    # print(f'loop2 pre:{pre} i:{i} k:{k} cnt:{cnt}')
                if k > 0 and cnt < n:
                    cnt = min(cnt + k, n)
                ma = max(ma, cnt)

                i = j
                cnt = 0
                pre = next_pre
                k = init_k

        return ma
        