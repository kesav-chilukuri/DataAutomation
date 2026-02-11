import os

import pytest
from pyspark.sql import SparkSession
import os
import yaml

@pytest.fixture(scope="session")
def spark_session():
    spark=SparkSession.builder.master("local[1]").appName("DataAutomation").getOrCreate()
    print("spark session created")
    return spark
    spark.stop()

@pytest.fixture(scope="module")
def read_config(request):
    dir_path = request.node.fspath.dirname
    config_file = os.path.join(dir_path, "config.yml")
    print("read_config")
    with open(config_file,'r') as f:
        config_data=yaml.safe_load(f)
    return config_data


@pytest.fixture(scope="module")
def read_data(spark_session,read_config):
    print("read_data")
    spark=spark_session
    config=read_config
    print("spark is ",spark)
    print("config is ",config)
    print('=='*50)
    print("source data",config['source'])
    print('==' * 50)
    print("Target data", config['target'])