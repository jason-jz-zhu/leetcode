class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        l3 = l1 + l2
        num3 = [0] * l3
        for i in range(l1 - 1, -1, -1):
            carry = 0
            for j in range(l2 - 1, -1, -1):
                carry = carry + num3[i + j + 1] + (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                remainder = carry % 10
                carry = carry // 10
                num3[i + j + 1] = remainder
            j -= 1
            num3[i + j + 1] = carry

        i = 0
        while i < l3 and num3[i] == 0:
            i += 1
        return '0' if i == len(num3) else ''.join(str(x) for x in num3[i:])
