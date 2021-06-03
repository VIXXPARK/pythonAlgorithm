class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    # insert/delete/replace
                    table[i][j] = 1 + min(table[i - 1][j],
                                          table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]

##################################################################################################


class Solution:
    def minDistance(self, word1, word2, i, j, memo):
        """Memoized solution"""
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance2(word1, word2, i + 1, j + 1, memo)
            else:
                insert = 1 + self.minDistance2(word1, word2, i, j + 1, memo)
                delete = 1 + self.minDistance2(word1, word2, i + 1, j, memo)
                replace = 1 + \
                    self.minDistance2(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]

#####################################################################################################


def minDistance(self, word1, word2):
    h, w = len(word1)+1, len(word2)+1
    pre = [i for i in range(w)]
    for i in range(1, h):
        cur = [i for _ in range(w)]
        for j in range(1, w):
            cur[j] = min(pre[j-1]+(word1[i-1] != word2[j-1]),
                         pre[j]+1, cur[j-1]+1)
        pre = cur
    return pre[-1]
