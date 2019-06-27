### 数学中的数


#### 1、圆周率Pi： 


#### 2、自然对数e： 

#### 3、无理数根号2：[sqrt_2.py](https://github.com/Anfany/Playing_Math_with_Python3/blob/master/number/sqrt_2.py)

   * 直接法
   
  采用试错的方法从0-9中选取一个数字添加到当前的数中，如果当前的数的平方大于2，则选中前一个数字。如果均小于2，则选中数字9添加到当前的数中。直到该数满足条件。此法获得的平方根的每一个数字都是准确的。
   
   * 二分法
  
```
min=0，max=2， product=1
当product与2的差不满足精度时：
     middle = (min + max) /2
     product  = middle * middle
     如果 product > 2:
         max = middle
     如果 product < 2:
          min = middle
```
 因为此法是通过控制乘积与2的差的精度来计算的，因此得到的平方根最后面的几个数字是不准确的。
   
   * 牛顿迭代法
  
  
   
   * 数对比值法
   
   初始数对s=[a,b]=[1,1]，通过a=a+b,b=2a+b不断的构造下一个数对[a,b]，而b与a的比值则无限接近根号2。对于根号2而言，数对序列就是```[1,1]，[2,3]，[5,7]，[12,17]，[29,41]，[70,99]，……```
   
   关于后面两种方法的详细说明，[参见](https://github.com/Anfany/Playing_Math_with_Python3/blob/master/computer)
   
