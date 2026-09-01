class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        map1={}
        map2={}
        for i in range(len(pattern)):
            if pattern[i] in map1 and map1[pattern[i]]!=words[i]:
                return False
            if words[i] in map2 and map2[words[i]]!=pattern[i]:
                return False

            map1[pattern[i]]=words[i]
            map2[words[i]]=pattern[i]
        return True


