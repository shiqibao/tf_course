# -*- coding:gb2312 -*-
import tensorflow as tf
#ʹ�ñ���ʵ��һ���򵥵ļ�����

#����һ������,��ʼ��Ϊ����0
state = tf.Variable(0, name="counter")

#����1��op,��������state��1
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

#����ͼ��,�������뾭����ʼ��op
#��������һ����ʼ��op��ͼ��

init_op = tf.initialize_all_variables()
#����ͼ
with tf.Session() as sess:
    #��ʼ������op
    sess.run(init_op)
    #��ӡstate��ʼֵ
    print sess.run(state)
    #�ظ�ִ�м�����3��,����update op
    for _ in range(3):
        r = sess.run(update)
        print r