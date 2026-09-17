class Solution(object):
    def stringMatching(self, words):
        r = []
        l = len(words)
        for i in range(l):
            for j in range(l):
                if i==j:
                    continue
                if words[i] in words[j]:
                    r.append(words[i])
                    break
        return r