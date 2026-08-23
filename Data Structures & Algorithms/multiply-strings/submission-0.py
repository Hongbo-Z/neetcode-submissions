class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        # return "".join(map(str, res[beg:]))
        return "".join([str(x) for x in res[beg:]])


# map(str, [4, 0, 8])

# 相当于依次执行：

# str(4)   # "4"
# str(0)   # "0"
# str(8)   # "8"

# 所以效果类似于：

# ["4", "0", "8"]

# 但要注意，map() 不会直接返回 list，它返回一个 map object，也就是一个 iterator

# 你可以把 map(f, iterable) 简单记成：

# [f(x) for x in iterable]

# 逻辑上等价于：

# [str(x) for x in [4, 0, 8]]
        