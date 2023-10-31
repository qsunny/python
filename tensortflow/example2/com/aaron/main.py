# -*- codiing:utf-8 -*-
import os
from pprint import pprint
# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

"""
https://www.tensorflow.org/tutorials/keras/classification?hl=zh-cn
基本分类：对服装图像进行分类
pip install matplotlib
训练数据集
https://github.com/zalandoresearch/fashion-mnist
http://yann.lecun.com/exdb/mnist/

"""


def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)


def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


if __name__ == "__main__":
    print(tf.__version__)
    fashion_mnist = tf.keras.datasets.fashion_mnist

    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    pprint(train_images.shape)
    pprint(len(train_labels))
    pprint(train_labels)
    pprint(test_images.shape)
    pprint(len(test_labels))

    # 在训练网络之前，必须对数据进行预处理。如果您检查训练集中的第一个图像，您会看到像素值处于0到255之间
    plt.figure()
    plt.imshow(train_images[1])
    plt.colorbar()
    plt.grid(False)
    plt.show()

    # 将这些值缩小至0到1之间，然后将其馈送到神经网络模型。为此，请将这些值除以
    # 255。请务必以相同的方式对训练集和测试集进行预处理
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

    # 构建神经网络需要先配置模型的层，然后再编译模型
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    """
    训练模型
        训练神经网络模型需要执行以下步骤：        
        将训练数据馈送给模型。在本例中，训练数据位于 train_images 和 train_labels 数组中。
        模型学习将图像和标签关联起来。
        要求模型对测试集（在本例中为 test_images 数组）进行预测。
        验证预测是否与 test_labels 数组中的标签相匹配。
    """
    model.fit(train_images, train_labels, epochs=10)

    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

    print('\nTest accuracy:', test_acc)

    probability_model = tf.keras.Sequential([model,
                                             tf.keras.layers.Softmax()])

    predictions = probability_model.predict(test_images)

    pprint(predictions[0])
    pprint(np.argmax(predictions[0]))
    pprint(test_labels[0])

    # 我们来看看第0个图像、预测结果和预测数组。正确的预测标签为蓝色，错误的预测标签为红色。数字表示预测标签的百分比（总计为100）
    i = 0
    plt.figure(figsize=(6, 3))
    plt.subplot(1, 2, 1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(1, 2, 2)
    plot_value_array(i, predictions[i],  test_labels)
    plt.show()


    i = 12
    plt.figure(figsize=(6, 3))
    plt.subplot(1, 2, 1)
    plot_image(i, predictions[i], test_labels, test_images)
    plt.subplot(1, 2, 2)
    plot_value_array(i, predictions[i], test_labels)
    plt.show()

    # 让我们用模型的预测绘制几张图像。请注意，即使置信度很高，模型也可能出错。
    # Plot the first X test images, their predicted labels, and the true labels.
    # Color correct predictions in blue and incorrect predictions in red.
    num_rows = 5
    num_cols = 3
    num_images = num_rows * num_cols
    plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
    for i in range(num_images):
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
        plot_image(i, predictions[i], test_labels, test_images)
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
        plot_value_array(i, predictions[i], test_labels)
    plt.tight_layout()
    plt.show()


    # 使用训练好的模型
    # 最后，使用训练好的模型对单个图像进行预测
    # Grab an image from the test dataset.
    img = test_images[1]

    pprint(img.shape)
    # tf.keras模型经过了优化，可同时对一个批或一组样本进行预测。因此，即便您只使用一个图像，您也需要将其添加到列表中：
    # Add the image to a batch where it's the only member.
    img = (np.expand_dims(img, 0))

    print(img.shape)

    # 现在预测这个图像的正确标签：
    predictions_single = probability_model.predict(img)

    print(predictions_single)

    plot_value_array(1, predictions_single[0], test_labels)
    _ = plt.xticks(range(10), class_names, rotation=45)
    plt.show()

    # keras.Model.predict会返回一组列表，每个列表对应一批数据中的每个图像。在批次中获取对我们（唯一）图像的预测：
    pprint(np.argmax(predictions_single[0]))
