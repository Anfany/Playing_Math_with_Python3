### 数学中的数


#### 1、圆周率Pi： 


#### 2、自然对数e： 

#### 3、无理数根号2：[sqrt_2.py](https://github.com/Anfany/Playing_Math_with_Python3/blob/master/computer/sqrt_2.py)

   * **直接法**
   
  采用试错的方法从0-9中选取一个数字添加到当前的数中，如果当前的数的平方大于2，则选中前一个数字。如果均小于2，则选中数字9添加到当前的数中。直到该数满足条件。
   
   * **二分法**
  
```
min=0，max=2， product=1
当product与2的差不满足精度时：
     middle = (min + max) /2
     product  = middle * middle
     如果 product >2:
         max = middle
     如果 product < 2:
          min = middle
```
   
   * **牛顿迭代法**
   
   * **数对比值法**
   
   
   
