# -*- coding:gb2312 -*-
import tensorflow as tf
#ʹ��placeholderΪfeed��������ռλ��
x1 = tf.placeholder("float")
x2 = tf.placeholder("float")
y = tf.multiply(x1, x2)

with tf.Session() as sess:
    result = sess.run(y,feed_dict={x1:7,x2:2})
    print result