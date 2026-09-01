class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer=[]
        for word in words:
            map1={}
            map2={}
            match=True
            for i in range (len(pattern)):
                if pattern[i] in map1 and map1[pattern[i]]!=word[i]:
                    match=False
                    break
                if word[i] in map2 and map2[word[i]]!=pattern[i]:
                    match=False
                    break
                map1[pattern[i]]=word[i]
                map2[word[i]] = pattern[i]
            if match:
                answer.append(word)
        return answer
