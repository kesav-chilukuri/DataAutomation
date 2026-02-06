import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_session():
    spark=SparkSession.builder.master("local[1]").appName("DataAutomation").getOrCreate()
    return spark
    spark.stop()

@pytest.fixture(scope="module")
def read_config():

@pytest.fixture(scope="module")
def read_data(spark_session,read_config):
