class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        each_index = [False] * n
        ans = []

        def dfs(i, each_index):
            if i == n:
                print(each_index)
                subset = []

                for j in range(len(each_index)):
                    if each_index[j]:
                        subset.append(nums[j])
                
                ans.append(subset)
                # print(ans)
                return 

            each_index[i] = True
            dfs(i+1, each_index)
            each_index[i] = False
            dfs(i+1, each_index)
            

        dfs(0, each_index)

        return ans
                