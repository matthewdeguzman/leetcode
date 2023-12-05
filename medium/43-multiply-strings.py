class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
          123
           25
          ---
        0 5 10 15
        2 4  6  0
        ----------
        3  0  7  5

        532
          0

        """
        if "0" in [num1, num2]:
            return "0"
        # [0, 0, 18, 4, 5]

        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        for i1, i in enumerate(num2[::-1]):
            for idx, j in enumerate(num1[::-1]):
                res[len(res) - idx - 1 - i1] += int(i) * int(j)

        for j in range(len(res) - 1, 0, -1):
            res[j - 1] += res[j] // 10
            res[j] %= 10

        # find first instance of not 0
        for start in range(0, len(res)):
            if res[start] != 0:
                break

        return "".join([str(i) for i in res[start:]])
