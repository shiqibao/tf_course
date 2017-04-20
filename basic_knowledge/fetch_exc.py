# -*- coding:gb2312 -*-
import tensorflow as tf
x1 = tf.constant(3.0)
x2 = tf.constant(2.0)
x3 = tf.constant(5.0)

intermed = tf.add(x2, x3)
mul = tf.multiply(x1, intermed)
#在run中使用[]获取多个tensor
with tf.Session() as sess:
    result = sess.run([mul,intermed])
    print result