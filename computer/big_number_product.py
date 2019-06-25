# -*- coding：utf-8 -*-
# &Author  AnFany


def big_product(a, b):
    """
    字符串形式返回a和b的乘积，Python3对于整数的乘积是由无限精度的，但是对于小数乘积的精度是有限的
    本程序适用于任意实数的乘积
    :param a: 任意实数
    :param b: 任意实数
    :return: 字符串形式的乘积
    """
    # 乘积的正负标识
    sign = ''
    if a[0] != '-':
        if b[0] == '-':
            sign = '-'
    else:
        if b[0] != '-':
            sign = '-'

    # 获取两个数的小数位数
    decimal_a, decimal_b = 0, 0
    if '.' in a:
            decimal_a = len(a) - a.index('.') - 1
    if '.' in b:
        decimal_b = len(b) - b.index('.') - 1

    # 去除数中的负号和小数点
    del_a = a.replace('-', '').replace('.', '')
    del_b = b.replace('-', '').replace('.', '')

    # 要把数字前面的数字0去掉
    new_a = ''
    for s in range(len(del_a)):
        if del_a[s] != '0':
            new_a = del_a[s:][::-1]
            break
    new_b = ''
    for d in range(len(del_b)):
        if del_b[d] != '0':
            new_b = del_b[d:][::-1]
            break
    if not new_a or not new_b:
        return '0'

    # 长度较短的数设置为乘数
    length_a, length_b = len(new_a), len(new_b)
    if length_a > length_b:
        new_b, new_a = new_a, new_b

    # 开始计算乘数的每一位与被乘数的乘积
    multiplier_product = []
    for i in range(len(new_a)):  # 乘数的每一位
        carry = 0  # 进位的数
        single_product = []  # 存储乘数的该位与被乘数的乘积的每一个位置上的数字列表
        a_number = int(new_a[i])  # 变为整数
        new_b = '0' * (1 if i else 0) + new_b  # 因为下一位乘积需要错位，因此在被乘数前面加0，方便后期的计算
        for j in range(len(new_b)):
            pro = a_number * int(new_b[j]) + carry  # 计算乘积与进位的和
            single_product.append(pro % 10)  # 被10整除的余数是该位得到的数字
            carry = pro // 10  # 进位的数
        if carry:  # 最后，如果进位的数不是0，需要加到乘积的列表里面
            single_product.append(carry)
        multiplier_product.append(single_product)  # 存储到总的乘积列表中

    # 因为乘数的每一位的乘积的列表长度不同，为了便于相加，变为统一的长度
    new_all_product = []
    for p in multiplier_product:
        new_all_product.append(p + [0] * (len(multiplier_product[-1]) - len(p)))  # 短的用数字0来添加

    # 每一位的乘积进行相加
    product_sum_str = ''  # 相加得到的字符串
    carry = 0  # 进位的数
    for s in range(len(new_all_product[0])):
        sum_str = carry
        for r in new_all_product:
            sum_str += r[s]  # 求和
        product_sum_str += str(sum_str % 10)  # 结果中的数字
        carry = sum_str // 10  # 进位的数
    if carry:  # 最后，如果进位不为0，则需要添加到结果中
        product_sum_str += str(carry)

    # 根据两个数小数点后面的位数和，添加小数点
    decimal_sum = decimal_a + decimal_b
    length = len(product_sum_str)
    # 如果乘积的位数小于小数的位数，需要补0
    if decimal_sum:
        if decimal_sum > length:
            product_sum_str += '0' * (decimal_sum - length)+ '.0'
        elif decimal_sum == length:
            product_sum_str = product_sum_str[: decimal_sum] + '.0'
        else:
            product_sum_str = product_sum_str[: decimal_sum] + '.' + product_sum_str[decimal_sum:]

        # 需要把最后的数字0去掉
        for k in range(len(product_sum_str)):
            if product_sum_str[k] == '.':
                product_sum_str = product_sum_str[(k+1):]
                break
            elif product_sum_str[k] != '0':
                product_sum_str = product_sum_str[k:]
                break
    # 添加乘积的正负标识
    last_pro_str = product_sum_str + sign

    return last_pro_str[::-1]  # 列表反转就是最终的结果
