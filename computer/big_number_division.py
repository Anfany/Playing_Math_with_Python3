# -*- coding：utf-8 -*-
# &Author  AnFany

#  任意实数的除法：模拟竖式的除法

import big_number_product as b_p  # 引进乘法
import big_number_sub_add as b_s   # 引起减法


def compare_number(str_a, str_b):
    """
    比较用字符串表示的2个正整数的大小
    :param str_a: 正整数
    :param str_b: 正整数
    :return: 前者大返回1,相等返回0，前者小返回-1
    """
    length_a, length_b = len(str_a), len(str_b)

    if length_a > length_b:
        return 1
    elif length_b > length_a:
        return -1
    else:
        for i, j in zip(str_a, str_b):
            i_int, j_int = int(i), int(j)
            if i_int > j_int:
                return 1
            elif i_int < j_int:
                return -1
        return 0


def get_carry(str_a, str_b):
    """
    计算该位可以取的商值
    :param str_a: 该位的被除数
    :param str_b: 除数
    :return: 可以取的商值
    """
    for i in range(1, 11):
        product = b_p.big_product(str(i), str_b)
        if compare_number(str_a, product) == -1:
            return str(i - 1)
        elif compare_number(str_a, product) == 0:
            return str(i)
    return print('被除数' + str_a, '除数' + str_b, '计算商出现错误')


def judge(str_d, decimal):
    """
    判断得到的商值的小数位数是否满足条件
    :param str_d: 商值
    :param decimal: 结果中保留的小数位数
    :return: 满足返回True，否则返回False
    """
    if '.' not in str_d:
        return False
    else:
        if len(str_d) - str_d.index('.') - 1 < decimal:
            return False
        return True


def big_division(a, b, decimal):
    """
    任意实数的除法
    :param a: 任意实数
    :param b: 任意实数
    :param decimal: 结果中保留的小数位数.最后一位数字不进行任何形式的近似。
    对于整除的情况，商值得小数位数如果小于decimal,则不受decimal的限制。如果大于则依然遵循decimal的限制
    :return: 自定义精度的商值
    """
    if a == b:
        return 1  # 不受decimal的限制

    # 判断结果的符号
    sign = ''
    if a[0] == '-':
        a = a[1:]
        if b[0] != '-':
            sign = '-'
        else:
            b = b[1:]
    else:
        if b[0] == '-':
            b = b[1:]
            sign = '-'

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
            
    if new_a == '':
        return '0'
    if new_b == '':
        return print('WARNING：商不能为0')

    # 被除数放大添加的0的个数
    add_0 = 0

    # 如果被除数小于除数，则需要将被除数放大倍数，
    if compare_number(new_a, new_b) == -1:
        add_0 = len(new_b) - len(new_a) + 1  # 保证被除数一定大于除数,被除数比除数多一位
        new_a += '0' * add_0

    # a和b只是小数点位置不同，其他的数字是相同的。也就是说b是a的整数倍
    if add_0:
        if new_a == new_b + '0':
            return '0.' + '0' * (add_0 - 2) + '1'

    # 判断开始对应的位置
    start_carry = 0
    for c in range(len(new_a) + 1):
        if compare_number(new_a[: c], new_b) >= 0:
            start_carry = c - 1
            break

    # 该为对应的被除数
    if start_carry == 0:
        dividend = ''
    else:
        dividend = new_a[: start_carry]

    # 下面进行竖式模拟的除法
    div = ''  # 存储商的结果

    while not judge(div, decimal):  # 这么设置，会导致后面出现为数字0，这种情况后面再处理

        try:
            # 当前的被除数为
            dividend = dividend + new_a[start_carry]
            # 当前位的被除数不小于除数，才可以计算商
            if compare_number(dividend, new_b) >= 0:
                # 此位获得的商
                current_num = get_carry(dividend, new_b)
                # 存储商
                div += current_num
                # 计算差值
                dividend = b_s.big_sub_add(dividend, b_p.big_product(current_num, new_b), '-')
            else:
                # 此时需要借位
                div += '0'

            start_carry += 1
            if dividend == '0':
                dividend = ''

        except IndexError:
            # 当start_carry超过new_a的长度时，此时需要就要加小数点，以及加0
            if '.' not in div:
                div += '.'
            # 当前的被除数为
            if dividend:
                dividend = dividend + '0'

            # 当前位的被除数大于除数，才可以计算商
            if compare_number(dividend, new_b) >= 0:
                # 此位获得的商
                current_num = get_carry(dividend, new_b)
                # 存储商
                div += current_num
                # 计算差值
                dividend = b_s.big_sub_add(dividend, b_p.big_product(current_num, new_b), '-')
            else:
                # 此时需要借位
                div += '0'

            if dividend == '0':
                dividend = ''

    # 如果被除数添加过数字0，此时需要恢复
    if add_0:
        # 首先获的小数点的位置
        de_index = div.index('.')
        # 去除小数点
        div = div.replace('.', '')

        # 如果小数点前面的数字多于add_0
        if de_index > add_0:
            result_div = div[:(de_index - add_0)] + '.' + div[(de_index - add_0):]
        elif de_index == add_0:
            result_div = '0.' + div
        else:
            result_div = '0.' + '0' * (add_0 - de_index) + div
    else:
        result_div = div

    #  对得到的结果进行规范化处理，需要将数字最后的0去掉
    for c in range(len(result_div) - 1, 0, -1):
        if result_div[c] == '.':
            result_div = result_div[: (c+1)] + '0'
            break
        elif result_div[c] != '0':
            result_div = result_div[:(c + 1)]
            break

    # 添加符号
    result_div = sign + result_div

    return result_div

