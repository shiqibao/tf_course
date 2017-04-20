# -*- coding:gb2312 -*-
import tensorflow as tf
#第一步
#构建图

#创建一个常量op,产生1个1行2列的矩阵,这个op称为1个节点
#加到默认图中
#构造器的返回值就是该op的返回值
matrix1 = tf.constant([[3, 3]])
#创建另一个常量op,产生2x1矩阵
matrix2 = tf.constant([[2],[2]])
#创建一个矩阵乘法matmul op。并将matrix1,matrix2作为输入
#返回值就是乘法op的返回值
product = tf.matmul(matrix1, matrix2)

#第二步
#执行图

#启动默认图
sess = tf.Session()
#调用sess的run方法来执行矩阵乘法op,传入product作为方法的参数
#product代表乘法op的输出,传入它是向run方法表明,我们希望取回矩阵乘法op的输出

#执行过程是自动的,会话负责传递op所需全部输入,op通常是并发执行的
#当函数调用run方法的时候,触发了图中三个op（2常量op,1乘法op）的执行
result = sess.run(product)
print result

#任务完成,关闭会话
sess.close()