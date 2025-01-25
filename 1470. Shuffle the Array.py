class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y=nums[n:]
        out=[]
        for i in range(len(x)):
            out.append(x[i])
            if i<len(y):
                out.append(y[i])
        return out
