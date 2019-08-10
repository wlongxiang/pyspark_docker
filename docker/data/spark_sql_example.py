from pyspark.sql import SparkSession
from pyspark.sql.types import *

import os
if __name__ == '__main__':

    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .getOrCreate()

    # json file
    # The schema is encoded in a string.
    fields = [StructField("name", StringType(), nullable=True),
              StructField("age", StringType(), nullable=True)]
    schema = StructType(fields)
    df = spark.read.json(os.path.join(os.getenv("SPARK_HOME"), "examples/src/main/resources/people.json"), schema=schema)
    df.show()
    df.createOrReplaceTempView("people")
    sqldf = spark.sql("select * from people where age > 20")
    sqldf.show()


    # parquet file
    dfparquet = spark.read.parquet(os.path.join(os.getenv("SPARK_HOME"), "examples/src/main/resources/users.parquet"))
    dfparquet.show()
    # we partition the table by favorite color, it will create a directory accordingly
    dfparquet.write.partitionBy("favorite_color").format("parquet").save("namesPartByColor.parquet")





