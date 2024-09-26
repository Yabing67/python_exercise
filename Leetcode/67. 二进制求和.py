# my solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        bin_sum = str(bin(sum))
        return bin_sum[2:]

# solution 2
    def addBinary_v2(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

# solution 3
    def addBinary_v3(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary_v3('10', '10'))
