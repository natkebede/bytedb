from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    sc = spark.sparkContext

    lines = sc.textFile("/opt/spark-data/input.txt")
    counts = lines.flatMap(lambda line: line.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile("/opt/spark-data/output")

    spark.stop()
