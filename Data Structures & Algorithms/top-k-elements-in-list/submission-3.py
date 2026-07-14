class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = dict()
        for i in nums:
            if i not in temp.keys():
                temp[i] = 1
                continue
            temp[i] +=1
        occurs = sorted(temp.values())[::-1]
        res = set()
        
        for j in occurs:
            for i,v in temp.items():
                if v == j :
                    res.add(i)
                if k == len(res) :
                    return list(res)
        
