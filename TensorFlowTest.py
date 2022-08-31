import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import cProfile

a = tf.constant([[1, 2],
                 [3, 4]])

# 브로드캐스팅(Broadcasting) 지원
b = tf.add(a, 1)

print(a)
print(b)
print(a*b)

c = np.multiply(a, b)
print(c)
