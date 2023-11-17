#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
A simple example demonstrating Spark SQL Hive integration.
Run with:
  ./bin/spark-submit examples/knowledge/main/python/sql/hive.py
"""
from __future__ import print_function

# $example on:spark_hive$
from os.path import join, abspath

from pyspark.sql import SparkSession
# $example off:spark_hive$


if __name__ == "__main__":
    # $example on:spark_hive$
    # warehouse_location points to the default location for managed databases and tables
    warehouse_location = abspath('spark-warehouse')

    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL Hive integration example") \
        .config("spark.sql.warehouse.dir", warehouse_location) \
        .enableHiveSupport() \
        .getOrCreate()

    # Queries are expressed in HiveQL
    spark.sql("select * from test_product.t_ware_price limit 10").show()
    # +---+-------+
    # |key|  value|
    # +---+-------+
    # |238|val_238|
    # | 86| val_86|
    # |311|val_311|
    # ...

    # Aggregation queries are also supported.
    spark.sql("SELECT COUNT(*) FROM test_product.t_ware_price").show()
    # +--------+
    # |count(1)|
    # +--------+
    # |    500 |
    # +--------+

    sqlDF = spark.sql("select id,product_id,property_id,property_name,property_value,other_value,create_time from ods.t_product_property limit 1000")
    stringsDS = sqlDF.rdd.map(lambda row: "属性名: %s, 属性值: %s " % (row.property_name, row.property_value))
    for record in stringsDS.collect():
        print(record)

    spark.stop()
