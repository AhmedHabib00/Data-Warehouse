from pyspark.sql import SparkSession

def main():
    # Initialize a Spark session
    spark = SparkSession.builder \
        .appName("SimpleSparkJob") \
        .getOrCreate()

    # Read data from HDFS
    df = spark.read.csv("hdfs://namenode/tmp/test.csv", header=True, inferSchema=True)

    # Show the initial DataFrame
    print("Initial DataFrame:")
    df.show()

    # Perform some transformations
    # For example, filtering employees with a salary greater than 60000
    filtered_df = df.filter(df.salary > 600)

    # Show the transformed DataFrame
    print("Filtered DataFrame (salary > 600):")
    filtered_df.show()

    # Write the result back to HDFS
    filtered_df.write.csv("hdfs://namenode/tmp/filtered_employees.csv", header=True)

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()

