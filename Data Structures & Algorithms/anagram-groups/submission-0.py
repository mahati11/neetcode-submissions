class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()
        for word in strs:
            t =str(sorted(word))
            if t not in temp.keys():
                temp[t] = [word]
                continue
            temp[t].append(word)
        return list(temp.values())

            



