class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ans=[]
        left=0
        for right in range(len(nums)):
            while q and q[-1][0] <=nums[right]:
                q.pop()
            q.append((nums[right], right))
            if right-left+1 == k:
                ans.append(q[0][0])
                left+=1
            while q and q[0][1]< left:
                q.popleft()
        return ans



        