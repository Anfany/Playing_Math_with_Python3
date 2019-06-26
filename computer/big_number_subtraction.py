# -*- coding：utf-8 -*-
# &Author  AnFany

#  正实数的减法


def big_subtraction(a, b):
    """
    计算两个正实数的减法
    :param a: 实数
    :param b: 实数
    :return: a-b的差
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

    # 首先判断两个数哪个大，大的作为被减数，如果b不是大的，则结果需要加负号
    sign = ''
    length_a, length_b = len(new_a), len(new_b)
    minuend, subtrahend = new_a[::-1], new_b[::-1]  # 被减数，减数
    if length_a < length_b:
        sign = '-'
        minuend, subtrahend = new_b[::-1], new_a[::-1]
    elif length_a == length_b:
        for s, d in zip(new_a, new_b):
            if int(s) < int(d):
                sign = '-'
                minuend, subtrahend = new_b[::-1], new_a[::-1]
                break
            elif int(s) > int(d):
                break

    # 被减数由于借位会导致变化
    minuend = list(minuend)  # 字符串变为列表

    # 下面进行减法
    sub = ''
    for h in range(len(subtrahend)):
        m_int = int(minuend[h])
        s_int = int(subtrahend[h])
        if m_int >= s_int:
            sub += str(m_int - s_int)  # 此时不用借位
        else:
            copy_m = minuend.copy()
            for f in range(h+1, len(minuend)):
                f_int = int(minuend[f])
                if f_int == 0:
                    copy_m[f] = '9'  # 为0的数字，借位后变为9
                else:
                    copy_m[f] = str(f_int - 1)
                    sub += str(10 + m_int - s_int)  # 不为0的数字，借位后减去1
                    break
            minuend = copy_m.copy()
    # 需要加上被减数剩余的
    sub += ''.join(minuend[len(subtrahend):])

    # 获得的结果
    sub_result = sub[::-1]

    # 把前面的数字0去掉
    for k in range(len(sub_result)):
        if sub_result[k] != '0':
            sub_result = sub_result[k:]
            break

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

    # 添加符号
    last_sub = sign + last_sub
    return last_sub








