# -*- coding:gb2312 -*-
import tensorflow as tf
#��һ��
#����ͼ

#����һ������op,����1��1��2�еľ���,���op��Ϊ1���ڵ�
#�ӵ�Ĭ��ͼ��
#�������ķ���ֵ���Ǹ�op�ķ���ֵ
matrix1 = tf.constant([[3, 3]])
#������һ������op,����2x1����
matrix2 = tf.constant([[2],[2]])
#����һ������˷�matmul op������matrix1,matrix2��Ϊ����
#����ֵ���ǳ˷�op�ķ���ֵ
product = tf.matmul(matrix1, matrix2)

#�ڶ���
#ִ��ͼ

#����Ĭ��ͼ
sess = tf.Session()
#����sess��run������ִ�о���˷�op,����product��Ϊ�����Ĳ���
#product����˷�op�����,����������run��������,����ϣ��ȡ�ؾ���˷�op�����

#ִ�й������Զ���,�Ự���𴫵�op����ȫ������,opͨ���ǲ���ִ�е�
#����������run������ʱ��,������ͼ������op��2����op,1�˷�op����ִ��
result = sess.run(product)
print result

#�������,�رջỰ
sess.close()