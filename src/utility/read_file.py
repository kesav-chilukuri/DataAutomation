def read_file(config,spark):
    path =config['path']
    type =config['type'].lower()
    schema=config['schema']
    options=config['options']
    exclude_cols=config['exclude_cols']

    if type=='csv':
        df=spark.read.csv(path=path,header=options["header"])
    elif type=='parquet':
        df=spark.read.parquet(path=path)
    elif type=='json':
        df=spark.read.json(path=path,multiline=options["multiline"])
    elif type=='avro':
        df=spark.read.format('avro').load(path=path)
    return df
