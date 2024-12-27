from pyspark.sql import SparkSession


if __name__ == "__main__":
    # 初始化 Spark 会话
    spark = SparkSession.builder.appName("BatchUploadToHDFS").getOrCreate()

    # 定义本地目录路径和目标 HDFS 目录路径
    local_dir = "file:///C:/Users/Administrator/Downloads/spark-master/data/*"
    hdfs_dir = "hdfs://data-master:9000/data/"

    # 读取本地目录中的所有文件
    df = spark.read.text(local_dir)

    # 将数据写入到 HDFS 目录
    df.write.mode("overwrite").text(hdfs_dir)

    # 停止 Spark 会话
    spark.stop()
