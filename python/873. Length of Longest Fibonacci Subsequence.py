class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = collections.defaultdict(lambda: 2)
        res = 0
        hashmap = {}
        for i in range(n):
            hashmap[A[i]] = i

        for j in range(n):
            for k in range(j + 1, n):
                a_i = A[k] - A[j]
                if a_i >= A[j]:
                    break
                elif a_i not in hashmap:
                    continue
                dp[j, k] = dp[hashmap[a_i], j] + 1
                res = max(res, dp[j, k])
        return res


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        m = len(A)
        dp = [[2 for _ in range(m)] for _ in range(m)]
        res = 0

        hashmap = {A[i]: i for i in range(m)}

        for k in range(2, m):
            for j in range(k - 1, -1, -1):
                a_i = A[k] - A[j]
                if a_i >= A[j]:
                    break
                if a_i not in hashmap:
                    continue

                dp[j][k] = dp[hashmap[a_i]][j] + 1
                res = max(res, dp[j][k])
        return res
