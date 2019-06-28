# -*- coding：utf-8 -*-
# &Author  AnFany

#  大数加、减法


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
            
    # 两个字符均为空
    if new_a == new_b:
        return '0'

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


#  正实数的加法

def big_addition(a, b):
    """
    计算两个正实数的加法
    :param a: 实数
    :param b: 实数
    :return: a+b的和
    """
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


#  大数加、减法

def big_sub_add(a, b, sign):
    """
    大数的加、减法
    :param a: 实数
    :param b: 实数
    :param sign: 求差或者求和的标识：‘-’：求差。‘+’：求和
    :return: 结果
    """
    # 求差
    if sign == '-':
        # a为负数
        if a[0] == '-':
            # a变为其相反数
            a = a[1:]
            # b为负数
            if b[0] == '-':
                # b变为其相反数
                b = b[1:]
                # 返回b减去a的差
                return big_subtraction(b, a)
            # b为正数
            else:
                # 返回a和b之和的相反数
                return '-' + big_addition(a, b)
        # a为正数
        else:
            # b为负数
            if b[0] == '-':
                # b变为其相反数
                b = b[1:]
                # 返回a与b的和
                return big_addition(a, b)
            # b为正数
            else:
                # 返回a和b的差
                return big_subtraction(a, b)

    # 求和
    elif sign == '+':
        # a为负数
        if a[0] == '-':
            # a变为其相反数
            a = a[1:]
            # b为负数
            if b[0] == '-':
                # b变为其相反数
                b = b[1:]
                # 返回a与b的和的相反数
                return '-' + big_addition(a, b)
            # b为正数
            else:
                # 返回b与a的差
                return big_subtraction(b, a)
        # a为正数
        else:
            # b为负数
            if b[0] == '-':
                # b变为其相反数
                b = b[1:]
                # 返回a与b的差
                return big_subtraction(a, b)
            # b为正数
            else:
                # 返回a和b的和
                return big_addition(a, b)
            
    else:
        return print('运算标识设置错误')

