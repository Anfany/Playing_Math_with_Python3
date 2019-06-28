# -*- coding：utf-8 -*-
# &Author  AnFany

#  计算自定义精度的任意正实数的算数平方根：直接法，二分法，牛顿迭代法，数对比值法，

import big_number_product as b_p   # 大数乘法
import big_number_division as b_d  # 大数除法
import big_number_sub_add as b_s_a  # 大数加减法


class SQRT():
    def __init__(self, number, decimal, sign='s', method='s_direct'):
        """
        计算自定义精度的任意正整数的算数平方根：直接法，二分法，牛顿迭代法，数对比值法，
        :param number:  进行开平方的数, 整数或者小数均可，字符串或者非字符串均可
        :param decimal:  需要控制的精度
        :param sign: 默认为's'，'s'：控制平方根的精度，获取小数点后第一个非0的数字开始计算，decimal位的准确的数字。
                     'p'：使得输出的平方根的平方与number的误差绝对值不大于1e(-decimal)
        :param method: 默认为's_direct'，'s_direct'：直接法；'s_dichotomy'：二分法；
                      's_newton'：牛顿迭代法；'s_sequence'：牛顿迭代法；
        """
        self.n = str(number)
        self.d = decimal
        self.s = sign
        self.m = method

        self.add = 8  # 当利用二分法，牛顿迭代法，数对比值法，如果sign=‘s’，就是获取准确的平方根，需要将精度扩大
        self.l = 0  # 对于0.0002，0.05这样的整数部分为0的，计算其小数点后面连续为0的个数，判断精度时需要用到
        self.change = self.trans_number()  # 数字变为标准格式缩小的倍数。在计算平方根位数的时候需要多算这几位

    def trans_number(self):
        """
        需要将数字变为小数点前面只有一位数字的数，并使得缩小的倍数是10的偶数次方
        例如：11.22变为0.1122，缩小了100倍，11662.33变为1.166233缩小了10000倍，0.89，0.0028这样的值不进行转变
        需要记录倍数的一半，最后需要对得到的结果进行放大处理
        :return: 缩小的倍数的一半以及变化后的数字
        """
        # 首选判断是不是小数
        if '.' not in self.n:
            length = len(self.n)
            if length == 1:
                self.n += '.0'  # 为了后面比较大小更方便，添加上小数点
                return 0
            elif length % 2 == 0:
                self.n = '0.%s' % self.n
                return length // 2
            else:
                self.n = '%s.%s' % (self.n[0], self.n[1:])
                return length // 2
        else:
            # 首先判断小数点的位置
            d_index = self.n.index('.')
            if d_index == 1:
                # 对于0.0002，0.05这样的整数部分为0的，计算其小数点后面连续为0的个数
                if self.n[0] == '0':
                    for s in self.n[2:]:
                        if s == '0':
                            self.l += 1
                        else:
                            break
                return 0

            self.n = self.n.replace('.', '')
            if d_index % 2 == 0:
                self.n = '0.%s' % self.n
            else:
                self.n = '%s.%s' % (self.n[0], self.n[1:])
            return d_index // 2

    def compare_number(self, p):
        """
        比较用字符串表示的数字和转换后的开方的数的大小
        :param p:  字符串，代表当前平方根的平方
        :return: 前者小返回-1, 等于返回0，大于返回1
        """
        # 首先判断字符串p中是否有小数点，没有的话添加上，因为比较大小不会影响结果
        if '.' not in p:
            p += '.0'
        # 首先判断p中整数的部分
        d_index = p.index('.')  # 为1
        # 因为self.n的整数部分只有一位
        if d_index > 1:
            return 1
        else:
            # 比较整数部分的大小
            int_p = int(p[0])
            int_n = int(self.n[0])
            if int_p > int_n:
                return 1
            elif int_p < int_n:
                return -1
            else:
                # 挨个数字比较小数部分
                f_p, f_n = p[2:], self.n[2:]
                length_p, length_n = len(f_p), len(f_n)
                min_length = min(length_p, length_n)
                for h in range(min_length):
                    int_f_p = int(f_p[h])
                    int_f_n = int(f_n[h])
                    if int_f_p > int_f_n:
                        return 1
                    elif int_f_p < int_f_n:
                        return -1
                # 判断长度较大的剩余的数字是不是均为0
                if length_p == length_n:
                    return 0
                elif length_p > length_n:
                    if list(set(f_p[min_length:])) == ['0']:
                        return 0
                    else:
                        return 1
                else:
                    if list(set(f_n[min_length:])) == ['0']:
                        return 0
                    else:
                        return -1

    def control_s(self, s_d, decimal):
        """
        平方根小数点后面第一个非0的数字开始计数
        :param s_d: 需要判断的对象，代表平方根
        :param decimal: 数字个数的要求
        :return: 不满足返回False，满足返回True
        """
        # 首先判断字符串s_d中是否有小数点，没有的话添加上，不会影响结果
        if '.' not in s_d:
            s_d += '.0'
        # 判断小数点的位置
        d_index = s_d.index('.')
        first_no_zero = 0  # 第一个非0的数是否出现的标识
        count = 0  # 开始计数
        for h in s_d[(1 + d_index):]:  # 排除掉小数点
            if h != '0':
                first_no_zero = 1  # 第一个非0的数出现
                count += 1
            else:
                if first_no_zero:
                    count += 1
        if count >= decimal:
            return True
        else:
            return False

    def control_p(self, s_d, decimal):
        """
        s_d的平方与转换后的开方的数之间的差值绝对值不大于1e(-decimal)
        :param s_d: 需要判断的对象，代表平方根
        :param decimal: 差的精度要求
        :return: 不满足返回False，满足返回True
        """
        # 首先计算平方
        squre = b_p.big_product(s_d, s_d)
        # 然后计算差值
        sub = b_s_a.big_subtraction(squre, self.n)
        # 如果是负数，去掉负号
        if sub[0] == '-':
            sub = sub[1:]
        # 因为是比较大小
        if '.' not in sub:
            sub += '.0'
        # 开始比较大小
        d_index = sub.index('.')
        if d_index > 1:  # 因为1e(-decimal)整数部分只有一位1.0，0.1，0.01，0.001……等等
            return False
        elif d_index == 1:
            if int(sub[0]) > 1:
                return False
            elif int(sub[0]) == 1:
                if decimal != 0:
                    return False
                else:  # 和1.0比较大小
                    if list(set(sub[2:])) == ['0']:
                        return True
                    else:
                        return False
            else:
                if decimal == 0:
                    return True
                # 考虑到需要开方的数，可能比较小，此时精度要在这个的基础上更小。
                # 也就是对于0.0002，0.05这样的整数部分为0的，计算其小数点后面连续为0的个数
                # 判断小数点后连续为0的个数
                count_zero = 0  # 判断差值中小数点之后，连续为0的个数
                for h in sub[2:]:
                    if h != '0':  # 只要出现其他的数字，就判断连续为0的个数是否满足需求的精度
                        if count_zero >= self.l + decimal + self.change:  # 需要加上开方的数原来自身的精度或者
                            return True
                        else:
                            return False
                    else:  # 小数点出现后，只要为0就开始加1
                        count_zero += 1

    def get_result(self, s_result, str_s):
        """
        将算法得到的算数平方根，转换为最终的结果，一是扩大倍数，二是截取需要的长度
        :param s_result: 待处理的算数平方根
        :param str_s: 如果为‘p’:控制的是平方的精度，不对得到的平方根进行截取，如果为‘s’：需要对平方根进行截取
        :return: 最终的结果
        """
        # 编程便利性
        if '.' not in s_result:
            s_result += '.0'
        d_index = s_result.index('.')  # 获取小数点位置
        s_result += '0' * (self.change + self.d)  # 防止小数点往后移动时出现没有数字的情况
        # 如果需要扩大倍数
        if self.change:
            s_result = s_result.replace('.', '')
            if str_s == 's':  # 需要对结果进行截取
                if s_result[0] == '0':
                    last_result = s_result[d_index:(d_index + self.change)] \
                                    + '.' + s_result[(d_index + self.change):][:self.d]  # 截取
                else:
                    last_result = s_result[:(d_index + self.change)] \
                                    + '.' + s_result[(d_index + self.change):][:self.d] # 截取
            else:
                if s_result[0] == '0':
                    last_result = s_result[d_index:(d_index + self.change)] \
                                    + '.' + s_result[(d_index + self.change):]
                else:
                    last_result = s_result[:(d_index + self.change)] \
                                    + '.' + s_result[(d_index + self.change):]
        else:
            # 需要判断整数部分是不是为0
            if s_result[0] == '0':
                # 需要从小数点后第一个不为0的数字，开始提取self.d个数字
                last_result = s_result[:2]
                count = 0
                start = 0
                d = s_result[2:]
                while count < self.d and start < len(d) - 1:
                    last_result += d[start]
                    if d[start] != '0':
                        count += 1
                    else:
                        if count:
                            count += 1
                    start += 1
            else:
                # 直接提取小数点后self.d个数字
                if str_s == 's':
                    last_result = s_result[:(self.d + 2)]  # 算上前面的整数部分和小数点
                else:
                    last_result = s_result

        # 对于开方的数为完全平方数的情况，得到的结果后面肯定会有连续的0，为了结果的美观，去要去掉
        for k in range(len(last_result) - 1, -1, -1):
            if last_result[k] == '.':
                return last_result[: k]
            elif last_result[k] != '0':
                return last_result[: (1 + k)]

    def s_direct(self):
        """
        利用直接法获得平方根，
        :return: 字符串形式的算数平方根
        """
        # 首先确定整数位上的数字
        first_n = int(self.n[0])
        if first_n == 9:
            start_n = '3.'
        elif 4 <= first_n < 9:
            start_n = '2.'
        elif 1 <= first_n < 4:
            start_n = '1.'
        else:
            start_n = '0.'

        # 判断当前解是否满足条件，保证正确性，此时多保留几位
        while not eval('self.control_%s' % self.s)(start_n, self.l + self.d + self.change):
            # 试错法获取下一个数字
            for i in range(0, 11):
                # 添加数字后
                new_sqrt = start_n + str(i)
                # 计算平方
                product = b_p.big_product(new_sqrt, new_sqrt)
                # 比较结果
                compare_result = self.compare_number(product)
                # 如果大于，说明上一个值是对的
                if compare_result == 1:
                    start_n += str(i - 1)
                    break
                elif compare_result == 0:
                    return self.get_result(new_sqrt, self.s)
                # 添加1-9都小于，说明需要添加的就是数字9
                if i == 10:
                    start_n += str(9)
        return self.get_result(start_n, self.s)

    # 利用二分法计算算数平方根
    def s_dichotomy(self):
        """
        利用二分法计算算数平方根
        :return: 最终的结果
        """
        min_num = '0'  # 二分法开始的最小值
        max_num = '4'  # 二分法开始的最大值
        middle_num = '2.'  # 二分法开始的中间值
        # 判断当前解是否满足条件，保证正确性，此时多保留几位
        if self.s == 'p':
            leave_count = self.d + self.l + self.change
        elif self.s == 's':
            leave_count = self.d + self.l + self.change + self.add
        # 依然是根据精度判断
        while not self.control_p(middle_num, leave_count):
            # 注意因为中间值的精确度小的话，会导致每次的middle_num 不变，因此下面的精度要稍微大点
            middle_num = str(b_d.big_division(b_s_a.big_addition(min_num, max_num), '2', leave_count * 3))
            # 计算乘积
            product = b_p.big_product(middle_num, middle_num)
            # 判断大小
            compare_result = self.compare_number(product)
            if compare_result == 1:
                # 大值变小
                max_num = middle_num
            elif compare_result == -1:
                # 小值变大
                min_num = middle_num
            else:
                return self.get_result(middle_num, self.s)
        return self.get_result(middle_num, self.s)

    # 利用牛顿迭代法计算算数平方根
    def s_newton(self):
        """
        利用牛顿迭代计算算数平方根
        :return: 最终的结果
        """
        start_num = '1'
        # 判断当前解是否满足条件，保证正确性，此时多保留几位
        if self.s == 'p':
            leave_count = self.d + self.l + self.change
        elif self.s == 's':
            leave_count = self.d + self.l + self.change + self.add
        # 依然是根据精度判断
        while not self.control_p(start_num, leave_count):
            # a = (a + (self.n/a)) /2
            # 保留位数也要稍微大点
            start_num = b_d.big_division(
                str(b_s_a.big_addition(start_num,
                                       str(b_d.big_division('%s' % self.n,
                                                            start_num, leave_count * 3)))), '2', leave_count * 3)

        return self.get_result(start_num, self.s)




