# -*- codiing:utf-8 -*-
import os
from pprint import pprint
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


"""
https://tensorflow.google.cn/tutorials/customization/custom_training_walkthrough?hl=zh-cn
自定义训练

鸢尾花分类问题
鸢尾属约有 300 个品种，但我们的程序将仅对下列三个品种进行分类：
山鸢尾
维吉尼亚鸢尾
变色鸢尾
训练数据集
wget --no-check-certificate \
    https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv \
    -O /tmp/iris_training.csv

"""


def pack_features_vector(features, labels):
  """Pack the features into a single array."""
  features = tf.stack(list(features.values()), axis=1)
  return features, labels


def loss(model, x, y, training):
  # training=training is needed only if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  y_ = model(x, training=training)

  return loss_object(y_true=y, y_pred=y_)


def grad(model, inputs, targets):
  with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, targets, training=True)
  return loss_value, tape.gradient(loss_value, model.trainable_variables)


if __name__ == "__main__":
    # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    print("TensorFlow version: {}".format(tf.__version__))
    print("Eager execution: {}".format(tf.executing_eagerly()))

    train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"

    train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url),
                                               origin=train_dataset_url)

    print("Local copy of the dataset file: {}".format(train_dataset_fp))

    # column order in CSV file
    column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    feature_names = column_names[:-1]
    label_name = column_names[-1]

    print("Features: {}".format(feature_names))
    print("Label: {}".format(label_name))
    """
    0: 山鸢尾
    1: 变色鸢尾
    2: 维吉尼亚鸢尾
    """
    class_names = ['Iris setosa', 'Iris versicolor', 'Iris virginica']
    batch_size = 32

    train_dataset = tf.data.experimental.make_csv_dataset(
        train_dataset_fp,
        batch_size,
        column_names=column_names,
        label_name=label_name,
        num_epochs=1)

    features, labels = next(iter(train_dataset))

    # print(features)

    plt.scatter(features['petal_length'],
                features['sepal_length'],
                c=labels,
                cmap='viridis')

    plt.xlabel("Petal length")
    plt.ylabel("Sepal length")
    plt.show()

    train_dataset = train_dataset.map(pack_features_vector)
    features, labels = next(iter(train_dataset))

    # print(features[:5])
    """
    tf.keras.Sequential 模型是层的线性堆叠。该模型的构造函数会采用一系列层实例；
    在本示例中，采用的是 2 个密集层（各自包含10个节点）,以及 1 个输出层（包含 3 个代表标签预测的节点。
    第一个层的 input_shape 参数对应该数据集中的特征数量，它是一项必需参数：
    """
    model = tf.keras.Sequential([
      tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(4,)),  # input shape required
      tf.keras.layers.Dense(10, activation=tf.nn.relu),
      tf.keras.layers.Dense(3)
    ])

    predictions = model(features)
    tf.nn.softmax(predictions[:5])
    print("Prediction: {}".format(tf.argmax(predictions, axis=1)))
    print("    Labels: {}".format(labels))

    loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    l = loss(model, features, labels, training=False)
    print("Loss test: {}".format(l))

    optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)

    loss_value, grads = grad(model, features, labels)

    print("Step: {}, Initial Loss: {}".format(optimizer.iterations.numpy(),
                                              loss_value.numpy()))

    optimizer.apply_gradients(zip(grads, model.trainable_variables))

    print("Step: {},         Loss: {}".format(optimizer.iterations.numpy(),
                                              loss(model, features, labels, training=True).numpy()))

    ## Note: Rerunning this cell uses the same model variables

    # Keep results for plotting
    train_loss_results = []
    train_accuracy_results = []

    num_epochs = 201

    for epoch in range(num_epochs):
        epoch_loss_avg = tf.keras.metrics.Mean()
        epoch_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

        # Training loop - using batches of 32
        for x, y in train_dataset:
            # Optimize the model
            loss_value, grads = grad(model, x, y)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

            # Track progress
            epoch_loss_avg.update_state(loss_value)  # Add current batch loss
            # Compare predicted label to actual label
            # training=True is needed only if there are layers with different
            # behavior during training versus inference (e.g. Dropout).
            epoch_accuracy.update_state(y, model(x, training=True))

        # End epoch
        train_loss_results.append(epoch_loss_avg.result())
        train_accuracy_results.append(epoch_accuracy.result())

        if epoch % 50 == 0:
            print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch,
                                                                        epoch_loss_avg.result(),
                                                                        epoch_accuracy.result()))

    fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
    fig.suptitle('Training Metrics')

    axes[0].set_ylabel("Loss", fontsize=14)
    axes[0].plot(train_loss_results)

    axes[1].set_ylabel("Accuracy", fontsize=14)
    axes[1].set_xlabel("Epoch", fontsize=14)
    axes[1].plot(train_accuracy_results)
    plt.show()

    test_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv"

    test_fp = tf.keras.utils.get_file(fname=os.path.basename(test_url),
                                      origin=test_url)

    test_dataset = tf.data.experimental.make_csv_dataset(
        test_fp,
        batch_size,
        column_names=column_names,
        label_name='species',
        num_epochs=1,
        shuffle=False)

    test_dataset = test_dataset.map(pack_features_vector)

    # 根据测试数据集评估模型
    test_accuracy = tf.keras.metrics.Accuracy()

    for (x, y) in test_dataset:
        # training=False is needed only if there are layers with different
        # behavior during training versus inference (e.g. Dropout).
        logits = model(x, training=False)
        prediction = tf.argmax(logits, axis=1, output_type=tf.int32)
        test_accuracy(prediction, y)

    print("Test set accuracy: {:.3%}".format(test_accuracy.result()))

    tf.stack([y, prediction], axis=1)

    """
    0: 山鸢尾
    1: 变色鸢尾
    2: 维吉尼亚鸢尾
    """
    # 使用经过训练的模型进行预测
    predict_dataset = tf.convert_to_tensor([
        [5.1, 3.3, 1.7, 0.5, ],
        [5.9, 3.0, 4.2, 1.5, ],
        [6.9, 3.1, 5.4, 2.1]
    ])

    # training=False is needed only if there are layers with different
    # behavior during training versus inference (e.g. Dropout).
    predictions = model(predict_dataset, training=False)

    for i,  logits in enumerate(predictions):
        class_idx = tf.argmax(logits).numpy()
        p = tf.nn.softmax(logits)[class_idx]
        name = class_names[class_idx]
        print("Example {} prediction: {} ({:4.1f}%)".format(i, name, 100 * p))


