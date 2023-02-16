from datetime import datetime


class Provider:
    def __init__(self, config):

        self.target_table = config.target_table
        self.db_mode = config.db_mode
        self.db_properties = config.db_properties
        self.request_history_table = config.request_history_table
        self.data_source = config.data_source
        self.date = config.date
        self.batch_size = config.batch_size
        self.db_url = config.db_url

    def insert(self, spark_session, dataframe):
        self.save_data(dataframe)
        self.save_request_hist(spark_session)


    def save_data(self, dataframe) :
        dataframe.write.jdbc(
            url=self.db_url,
            table=self.target_table,
            mode=self.db_mode,
            properties=self.db_properties
        )
    def save_request_hist (self, spark_session):

        df = spark_session.createDataFrame(
          [{
                "data_source": self.data_source,
                "batch_size": self.batch_size,
                "load_dttm": datetime.now()
             }]
        )

        df.write.jdbc(
            url=self.db_url,
            table=self.request_history_table,
            mode=self.db_mode,
            properties=self.db_properties
        )
