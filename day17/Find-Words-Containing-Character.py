class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        N = len(words)
        result = []
        for i in range(N):
            if x in words[i]:
                result.append(i)
                

        return result