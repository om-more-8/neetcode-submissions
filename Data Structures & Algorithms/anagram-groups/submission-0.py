class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #for each string in arr id have to make a freq hashmap to keep it as identity of that string
        for s in strs:
            freqMap = [0] * 26 
            for i in s:
                freqMap[ord(i) - ord("a")] += 1
            
            #1.treating the freqMap/count hashset as my key to separate or cluster the similar strings  
            #2.converting to tuple because list datatype isnot hashable and cant be used as key
            res[tuple(freqMap)].append(s)

        return list(res.values())

        

