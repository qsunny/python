# -*- codiing:utf-8 -*-
import os
from pprint import pprint
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

"""
https://tensorflow.google.cn/tutorials/keras/text_classification?hl=zh-cn
基本文本分类

训练数据集
https://tensorflow.google.cn/tutorials/keras/text_classification?hl=zh-cn#%E4%B8%8B%E8%BD%BD_imdb_%E6%95%B0%E6%8D%AE%E9%9B%86

"""

if __name__ == "__main__":
    print(tf.__version__)

    # 下载IMDB数据集到您的机器上（如果您已经下载过将从缓存中复制）
    imdb = keras.datasets.imdb

    (train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
    print("Training entries: {}, labels: {}".format(len(train_data), len(train_labels)))
    print(train_data[0])
    len(train_data[0]), len(train_data[1])

    # 创建一个辅助函数来查询一个包含了整数到字符串映射的字典对象
    # 一个映射单词到整数索引的词典
    word_index = imdb.get_word_index()

    # 保留第一个索引
    word_index = {k:(v+3) for k,v in word_index.items()}
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2  # unknown
    word_index["<UNUSED>"] = 3

    reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

    def decode_review(text):
        return ' '.join([reverse_word_index.get(i, '?') for i in text])


    pprint(decode_review(train_data[0]))

    train_data = keras.preprocessing.sequence.pad_sequences(train_data,
                                                            value=word_index["<PAD>"],
                                                            padding='post',
                                                            maxlen=256)

    test_data = keras.preprocessing.sequence.pad_sequences(test_data,
                                                           value=word_index["<PAD>"],
                                                           padding='post',
                                                           maxlen=256)

    print(len(train_data[0]), len(train_data[1]))
    print(train_data[0])

    # 构建模型
    # 输入形状是用于电影评论的词汇数目（10,000 词）
    vocab_size = 10000

    model = keras.Sequential()
    model.add(keras.layers.Embedding(vocab_size, 16))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(16, activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))

    pprint(model.summary())

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    x_val = train_data[:10000]
    partial_x_train = train_data[10000:]

    y_val = train_labels[:10000]
    partial_y_train = train_labels[10000:]

    # 以512个样本的mini - batch大小迭代40个epoch来训练模型。这是指对x_train和y_train张量中所有样本的的40次迭代。
    # 在训练过程中，监测来自验证集的10, 000个样本上的损失值（loss）和准确率（accuracy）
    history = model.fit(partial_x_train,
                        partial_y_train,
                        epochs=40,
                        batch_size=512,
                        validation_data=(x_val, y_val),
                        verbose=1)

    # 评估模型
    # 我们来看一下模型的性能如何。将返回两个值。损失值（loss）（一个表示误差的数字，值越低越好）与准确率（accuracy
    results = model.evaluate(test_data,  test_labels, verbose=2)

    print(results)

    # model.fit()返回一个History对象，该对象包含一个字典，其中包含训练阶段所发生的一切事件
    history_dict = history.history
    pprint(history_dict.keys())

    # 有四个条目：在训练和验证期间，每个条目对应一个监控指标。我们可以使用这些条目来绘制训练与验证过程的损失值（loss）和准确率（accuracy），以便进行比较

    acc = history_dict['accuracy']
    val_acc = history_dict['val_accuracy']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']

    epochs = range(1, len(acc) + 1)

    # “bo”代表 "蓝点"
    plt.plot(epochs, loss, 'bo', label='Training loss')
    # b代表“蓝色实线”
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

    plt.clf()  # 清除数字

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.show()













