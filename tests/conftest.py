import pytest
from pyspark.sql import SparkSession
import os
import yaml
from src.utility.read_db import read_db
from src.utility.read_file import read_file


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
    # print("read_data")
    spark=spark_session
    config=read_config
    # print("spark is ",spark)
    # print("config is ",config)
    source_config=config["source"]
    target_config=config["target"]
    if source_config['type']=='database':
        source_df = read_db(config=source_config, spark=spark)

    else:
        source_df=read_file(config=source_config,spark=spark)
        print("Source data")

    if target_config['type']=='database':
        target_df = read_db(config=target_config, spark=spark)
    else:
        target_df=read_file(config=target_config,spark=spark)
        print("Target data")

    return source_df, target_df
