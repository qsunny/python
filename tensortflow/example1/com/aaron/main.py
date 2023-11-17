# -*- codiing:utf-8 -*-
import os
import tensorflow as tf
from pprint import pprint


import tensorflow as tf

"""
文档 https://www.tensorflow.org/tutorials/quickstart/beginner?hl=zh-cn

conda create --name tensortflow python=3.9 -y
pip install tensorflow-cpu
pip install --upgrade tensorflow
python -m pip show scikit-learn
python -c "import sklearn; sklearn.show_versions()"
pip install pomegranate

pip install -U scikit-learn
In order to check your installation you can use
python -m pip show scikit-learn  # to see which version and where scikit-learn is installed
python -m pip freeze  # to see all packages installed in the active virtualenv
python -c "import sklearn; sklearn.show_versions()"

"""


if __name__ == "__main__":
    # Simple hello world using TensorFlow

    pprint(tf.add(1, 2).numpy())
    hello = tf.constant('Hello, TensorFlow!')
    pprint(hello.numpy())

    mnist = tf.keras.datasets.mnist

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10)
    ])

    predictions = model(x_train[:1]).numpy()
    pprint(predictions)

    # tf.nn.softmax函数将这些logits转换为每个类的概率
    tf.nn.softmax(predictions).numpy()

    # 使用losses.SparseCategoricalCrossentropy为训练定义损失函数，它会接受logits向量和True索引，并为每个样本返回一个标量损失
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    # 这个未经训练的模型给出的概率接近随机（每个类为1 / 10），因此初始损失应该接近 - tf.math.log(1 / 10)~ = 2.3
    lr = loss_fn(y_train[:1], predictions).numpy()
    pprint(lr)

    # 在开始训练之前，使用Keras Model.compile配置和编译模型。将optimizer类设置为adam，将loss设置为您之前定义的loss_fn函数，并通过将metrics
    # 参数设置为accuracy来指定要为模型评估的指标。
    model.compile(optimizer='adam',
                  loss=loss_fn,
                  metrics=['accuracy'])

    # 使用Model.fit方法调整您的模型参数并最小化损失
    model.fit(x_train, y_train, epochs=5)

    # Model.evaluate方法通常在"Validation-set"或"Test-set"上检查模型性能
    model.evaluate(x_test, y_test, verbose=2)

    # 如果您想让模型返回概率，可以封装经过训练的模型，并将softmax附加到该模型
    probability_model = tf.keras.Sequential([
      model,
      tf.keras.layers.Softmax()
    ])
    pprint(probability_model(x_test[:5]))