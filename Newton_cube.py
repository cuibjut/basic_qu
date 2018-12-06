#!coding=UTF_8
import math
"""
迭代
x(n+1) = x(n) - f(x(n))/f'(x(n))
"""


def cube_compution(input):
    x0 = 1
    x1 = x0 - (x0 - input / math.pow(x0, 2)) / 3

    while math.fabs(x1 - x0) > 0.000001:  # 一定要用fabs绝对值， 否则得到结果可能不准确
        x0 = x1
        x1 = x0 - (x0 - input / math.pow(x0, 2)) / 3

    return x1


if __name__ == '__main__':
    input = 8
    cube_value = cube_compution(input)
    print(cube_value)

