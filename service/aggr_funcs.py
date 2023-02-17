import statistics
import pyspark.sql.functions as sqlf
class Aggr_Data:
    def __init__(self, spark_session,df,data_source,load_dttm):
        self.df= df
        self.spark_session=spark_session
        self.data_source = data_source
        self.load_dttm = load_dttm


        if self.data_source == 'dessert' and self.load_dttm is not None:
            self.df2 = df.filter((df.data_source == 'dessert') & (df.load_dttm == self.load_dttm))
            self.df2.createOrReplaceTempView("aggr")

        elif self.data_source == 'dessert' and self.load_dttm is None:
            self.df2 = df.filter(df.data_source == 'dessert')
            self.df2.createOrReplaceTempView("aggr")

        elif self.data_source == 'food' and self.load_dttm is not None:
            self.df2 = df.filter((df.data_source == 'food') & (df.load_dttm == self.load_dttm))
            self.df2.createOrReplaceTempView("aggr")

        elif self.data_source == 'food' and self.load_dttm is None:
            self.df2 = df.filter(df.data_source == 'food')
            self.df2.createOrReplaceTempView("aggr")

        elif self.data_source is None and self.load_dttm is not None:
            self.df2 = df.filter(df.load_dttm == self.load_dttm)
            self.df2.createOrReplaceTempView("aggr")

        elif self.data_source is None and self.load_dttm is not None:
            self.df2.createOrReplaceTempView("aggr")

        df3 = self.spark_session.sql("select * from aggr")
        df3.agg({'aggr.batch_size': 'min'}).show()
        df3.agg({'aggr.batch_size': 'max'}).show()
        df3.agg({'aggr.batch_size': 'avg'}).show()
        df3.agg({'aggr.batch_size': 'stddev'}).show()
        df3.agg({'aggr.batch_size': 'count'}).show()

        df3.write.mode('append').csv('./mycsv')