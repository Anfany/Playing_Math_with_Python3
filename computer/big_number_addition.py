# -*- coding：utf-8 -*-
# &Author  AnFany

#  正实数的加法


def big_addition(a, b):
    """
    计算两个正实数的加法
    :param a: 实数
    :param b: 实数
    :return: a+b的和
    """
    if a == b:
        return '0'
    # 获取实数的小数点位数
    decimal_a = 0
    if '.' in a:
        decimal_a = len(a) - a.index('.') - 1
        a = a.replace('.', '')

    decimal_b = 0
    if '.' in b:
        decimal_b = len(b) - b.index('.') - 1
        b = b.replace('.', '')

    # 最长的小数位数
    max_de = max(decimal_a, decimal_b)

    # 两个数转为整数
    if max_de:
        a += '0' * (max_de - decimal_a)
        b += '0' * (max_de - decimal_b)

    # 将两个数前面的0去掉
    new_a = ''
    for i in range(len(a)):
        if a[i] != '0':
            new_a = a[i:]
            break
    new_b = ''
    for j in range(len(b)):
        if b[j] != '0':
            new_b = b[j:]
            break

    # 需要将2个数变为同等长度，长度短的用数字0凑齐
    length_a, length_b = len(new_a), len(new_b)
    if length_a < length_b:
        new_a = '0' * (length_b - length_a) + new_a
    else:
        new_b = '0' * (length_a - length_b) + new_b

    # 将数字逆序排列
    addend_a = new_a[::-1]
    addend_b = new_b[::-1]

    # 下面进行加法
    add = ''  # 存储的和值
    carry = 0  # 进位的数
    for h in range(len(addend_a)):
        a_int = int(addend_a[h])
        b_int = int(addend_b[h])
        sum_int = a_int + b_int + carry
        add += str(sum_int % 10)
        carry = sum_int // 10
    if carry:
        add += str(carry)

    # 获得的结果
    sub_result = add[::-1]

    # 添加小数点
    if max_de:
        length = len(sub_result)
        if length > max_de:
            last_sub = sub_result[:(length - max_de)] + '.' + sub_result[(length - max_de):]
        elif length == max_de:
            last_sub = '0.' + sub_result
        else:
            last_sub = '0.' + '0' * (max_de - length) + sub_result

        # 需要将数字最后的0去掉
        for c in range(len(last_sub)-1, 0, -1):
            if last_sub[c] == '.':
                last_sub = last_sub[:(c + 1)] + '0'
                break
            elif last_sub[c] != '0':
                last_sub = last_sub[:(c + 1)]
                break
    else:
        last_sub = sub_result

    return last_sub


