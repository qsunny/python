# -*- codiing:utf-8 -*-
import os
from pprint import pprint
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

"""
自定义层
"""


class MyDenseLayer(tf.keras.layers.Layer):
    """自行实现层的最佳方式是扩展 tf.keras.Layer 类并实现：

    __init__：您可以在其中执行所有与输入无关的初始化
    build：您可以在其中获得输入张量的形状，并可以进行其余初始化
    call：您可以在其中进行前向计算
    """

    def __init__(self, num_outputs):
        super(MyDenseLayer, self).__init__()
        self.num_outputs = num_outputs

    def build(self, input_shape):
        self.kernel = self.add_weight("kernel",
                                      shape=[int(input_shape[-1]),
                                             self.num_outputs])

    def call(self, inputs):
        return tf.matmul(inputs, self.kernel)


class ResnetIdentityBlock(tf.keras.Model):
    """
    模型：组合层
    机器学习模型中有许多有趣的层状物都是通过组合现有层来实现的。例如，ResNet 中的每个残差块都是卷积、批次归一化和捷径的组合。层可以嵌套在其他层中。
    """

    def __init__(self, kernel_size, filters):
        super(ResnetIdentityBlock, self).__init__(name='')
        filters1, filters2, filters3 = filters

        self.conv2a = tf.keras.layers.Conv2D(filters1, (1, 1))
        self.bn2a = tf.keras.layers.BatchNormalization()

        self.conv2b = tf.keras.layers.Conv2D(filters2, kernel_size, padding='same')
        self.bn2b = tf.keras.layers.BatchNormalization()

        self.conv2c = tf.keras.layers.Conv2D(filters3, (1, 1))
        self.bn2c = tf.keras.layers.BatchNormalization()

    def call(self, input_tensor, training=False):
        x = self.conv2a(input_tensor)
        x = self.bn2a(x, training=training)
        x = tf.nn.relu(x)

        x = self.conv2b(x)
        x = self.bn2b(x, training=training)
        x = tf.nn.relu(x)

        x = self.conv2c(x)
        x = self.bn2c(x, training=training)

        x += input_tensor
        return tf.nn.relu(x)


block = ResnetIdentityBlock(1, [1, 2, 3])


if __name__ == "__main__":
    # In the tf.keras.layers package, layers are objects. To construct a layer,
    # simply construct the object. Most layers take as a first argument the number
    # of output dimensions / channels.
    layer = tf.keras.layers.Dense(100)
    # The number of input dimensions is often unnecessary, as it can be inferred
    # the first time the layer is used, but it can be provided if you want to
    # specify it manually, which is useful in some complex models.
    layer = tf.keras.layers.Dense(10, input_shape=(None, 5))

    # To use a layer, simply call it.
    layer(tf.zeros([10, 5]))

    # Layers have many useful methods. For example, you can inspect all variables
    # in a layer using `layer.variables` and trainable variables using
    # `layer.trainable_variables`. In this case a fully-connected layer
    # will have variables for weights and biases.
    pprint(layer.variables)

    # The variables are also accessible through nice accessors
    # pprint(layer.kernel), pprint(layer.bias)

    # 自定义层
    layer = MyDenseLayer(10)
    _ = layer(tf.zeros([10, 5]))  # Calling the layer `.builds` it.
    # print([var.name for var in layer.trainable_variables])

    block = ResnetIdentityBlock(1, [1, 2, 3])
    _ = block(tf.zeros([1, 2, 3, 3]))
    pprint(block.layers)

    # pprint(len(block.variables))

    pprint(block.summary())

    """
    但是，在很多时候，由多个层组合而成的模型只需要逐一地调用各层。为此，使用 tf.keras.Sequential 只需少量代码即可完成：
    """
    my_seq = tf.keras.Sequential([tf.keras.layers.Conv2D(1, (1, 1),
                                                         input_shape=(
                                                             None, None, 3)),
                                  tf.keras.layers.BatchNormalization(),
                                  tf.keras.layers.Conv2D(2, 1,
                                                         padding='same'),
                                  tf.keras.layers.BatchNormalization(),
                                  tf.keras.layers.Conv2D(3, (1, 1)),
                                  tf.keras.layers.BatchNormalization()])
    pprint(my_seq(tf.zeros([1, 2, 3, 3])))
    pprint(my_seq.summary())





