# Databricks notebook source

# COMMAND ----------
# Print a start message and describe the notebook's purpose
print("Starting Databricks notebook smoke test...")

# COMMAND ----------
# Check that a Spark session is active and print the Spark version
try:
    spark_version = spark.version
    print(f"Spark session is active. Version: {spark_version}")
except Exception as e:
    raise AssertionError("No active Spark session found. Ensure this notebook is attached to a cluster.") from e

# COMMAND ----------
# Create a small sample DataFrame and display it
import pyspark.sql.functions as F
from pyspark.sql import Row

# Define sample data
sample_data = [Row(id=1, value="foo"), Row(id=2, value="bar")]
df = spark.createDataFrame(sample_data)

# Display the DataFrame (Databricks notebooks render display automatically)
display(df)

# COMMAND ----------
# Assert that the DataFrame contains the correct number of rows
expected_rows = 2
actual_rows = df.count()
assert actual_rows == expected_rows, f"Expected {expected_rows} rows, but got {actual_rows}."

# COMMAND ----------
# Print a final success message
print("Databricks notebook smoke test completed successfully!")
