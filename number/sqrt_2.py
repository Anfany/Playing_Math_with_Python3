# -*- coding：utf-8 -*-
# &Author  AnFany

#  计算自定义精度的2的算数平方根：直接法，二分法，牛顿迭代法，数对比值法，

import big_number_product as b_p   # 大数乘法
import big_number_division as b_d  # 大数除法
import big_number_sub_add as b_s_a  # 大数加减法


def compare_number(a):
    """
    比较用字符串表示的数字和2的大小
    :param a: 正实数，字符串
    :return: 前者小返回-1, 否则返回1
    """
    if a[0] == '1':
        return -1
    return 1


def judge_sqrt(str_d, decimal):
    """
    判断str_d小数点后面的数字是否达到了要求
    :param str_d: 字符串数字，代表平方根
    :param decimal: 小数点后面的数字个数
    :return: 达到了返回True，否则返回False
    """
    if '.' not in str_d:
        return False
    if len(str_d) - str_d.index('.') - 1 >= decimal:
        return True
    else:
        return False


def sqrt_2_direct(decimal):
    """
    利用直接法计算2的算数平方根
    :param decimal: 自定义精度，小数点后面的数字位数
    :return: 2的算数平方根
    """
    sqrt_number = '1.'  # 算数平方根的整数部分
    # 判断当前的平方根是否满足要求
    while not judge_sqrt(sqrt_number, decimal):
        # 试错法获取下一个数字
        for i in range(1, 11):
            # 添加数字后
            new_sqrt = sqrt_number + str(i)
            # 计算乘积
            product = b_p.big_product(new_sqrt, new_sqrt)
            # 判断和2的比较结果
            compare_result = compare_number(product)
            # 如果大于2，说明上一个值是对的
            if compare_result == 1:
                sqrt_number += str(i - 1)
                break
            # 添加1-9都不大于2，说明需要添加的就是数字9
            if i == 10:
                sqrt_number += str(9)
    return sqrt_number


def accuracy(str_d, decimal):
    """
    str_d与2的差的绝对值是否小于1e(-decimal)
    :param str_d: 字符串的数字，代表乘积
    :param decimal: 代表精度
    :return: 小于返回True,否则返回False
    """
    # 计算两数的差
    sub = b_s_a.big_subtraction(str_d, '2')
    if sub[0] == '-':
        sub = sub[1:]
    sign = 0  # 判断差值中小数点之后，连续为0的个数
    cc = 0  # 小数点的判断标识
    for h in sub:
        if h == '.':  # 小数点出现
            cc = 1
        elif h != '0':  # 只要出现其他的数字，就判断连续为0的个数是否满足需求的精度
            if sign > decimal - 1:
                return True
            else:
                return False
        else:  # 小数点出现后，只要为0就开始加1
            if cc:
                sign += 1


# 利用二分法计算2的算数平方根
def sqrt_2_dichotomy(decimal):
    """
    利用二分法计算2的算数平方根，和直接法不同，此法是通过得到的乘积和2的差来判断是否终止
    :param decimal: 乘积与2的差，绝对值小于1e(-decomical)
    :return: 2的算数平方根
    """
    min_num = '0'  # 二分法开始的最小值
    max_num = '2'  # 二分法开始的最小值
    middle_num = ''  # 二分法开始的中间值
    product = '1'
    # 通过判断当前乘积和2的差是否满足条件
    while not accuracy(product, decimal):
        #  计算中间值，注意中间值的精度稍微大于decimal即可。
        # 平方根的精确位数和乘积的精确位数基本相等
        # 如果平方根的前M位是精确的，那么其平方和2的差值小数点后面连续为0的个数基本也是M个。但这并不是绝对的
        middle_num = str(b_d.big_division(b_s_a.big_addition(min_num, max_num), '2', decimal + 5))
        # 计算乘积
        product = b_p.big_product(middle_num, middle_num)
        # 判断大小
        compare_result = compare_number(product)
        if compare_result == 1:
            # 大值变小
            max_num = middle_num
        elif compare_result == -1:
            # 小值变大
            min_num = middle_num
    return middle_num, product


# 利用牛顿迭代法计算2的算数平方根
def sqrt_2_newton(decimal):
    """
    利用牛顿迭代f计算2的算数平方根，和二分法相同，此法也是通过得到的乘积和2的差来判断是否终止
    :param decimal: 乘积与2的差，绝对值小于1e(-decomical)
    :return: 2的算数平方根
    """
    start_num = '1'
    product = '1'
    # 通过判断当前乘积和2的差是否满足条件
    while not accuracy(product, decimal):
        # a = (a + (2/a)) /2
        # 保留位数也要比decimal稍微大点
        start_num = b_d.big_division(b_s_a.big_addition(start_num,
                                                        b_d.big_division('2', start_num, decimal + 5)), '2', decimal + 5)
        # 计算乘积
        product = b_p.big_product(start_num, start_num)

    return start_num, product


# 构造数对的方法
def sqrt_2_sequence(decimal):
    """
    构造数对。数对元素之间的商值看作根号2的近似。
    和二分法、牛顿迭代法相同，此法也是通过得到的乘积和2的差来判断是否终止
    :param decimal: 小数的精度
    :return:
    """
    # 初始数对
    s = ['1', '1']
    # 初始比值
    radio = '1'
    # 乘积
    product = '1'
    # 通过判断当前乘积和2的差是否满足条件
    while not accuracy(product, decimal):
        c_s = s.copy()
        # 构造下一个数对
        s[0] = b_s_a.big_addition(c_s[0], c_s[1])
        s[1] = b_s_a.big_addition(str(b_p.big_product('2', c_s[0])), c_s[1])
        # 计算比值，保留位数也要比decimal稍微大点
        radio = str(b_d.big_division(s[1], s[0], decimal + 5))
        # 计算乘积
        product = b_p.big_product(radio, radio)
    return radio, product





