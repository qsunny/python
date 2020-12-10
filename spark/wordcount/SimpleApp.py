"""SimpleApp.py"""
from pyspark.sql import SparkSession

logFile = "file:///E:/soft/spark-3.0.1-bin-hadoop3.2/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.sparkContext.textFile(logFile).cache()

numAs = logData.filter(logData.contains('a')).count()
numBs = logData.filter(logData.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()