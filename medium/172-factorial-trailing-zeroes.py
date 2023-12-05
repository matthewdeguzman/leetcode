class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 5 * 4 * 3 * 2 * 1 = 10 (n)
        # 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 > 10 * 10 * (n)
        res = 0
        while n > 0:
            res += n // 5
            n //= 5

        return res
