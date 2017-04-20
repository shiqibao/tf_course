# -*- coding:gb2312 -*-
import tensorflow as tf
#使用变量实现一个简单的计数器

#创建一个变量,初始化为标量0
state = tf.Variable(0, name="counter")

#创建1个op,其作用是state加1
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

#启动图后,变量必须经过初始化op
#首先增加一个初始化op到图中

init_op = tf.initialize_all_variables()
#启动图
with tf.Session() as sess:
    #初始化变量op
    sess.run(init_op)
    #打印state初始值
    print sess.run(state)
    #重复执行计数器3次,运行update op
    for _ in range(3):
        r = sess.run(update)
        print r