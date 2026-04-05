class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            dictt[sortedS].append(s)
        return list(dictt.values())

        