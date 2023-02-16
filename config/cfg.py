import random
import yaml

class Config:
    def __init__(self, config_path, data_source, date):
        with open(config_path) as cp:  # контекстный менеджер
            cfgDict = yaml.load(cp, Loader=yaml.FullLoader)

            self.data_source = data_source
            self.date = date
            self.db_mode = cfgDict['db_connect']['mode']
            self.db_url = cfgDict['db_connect']['url']
            self.db_properties = cfgDict['db_connect']['properties']
            self.request_history_table = cfgDict['uploader']['request_history']['table']

            self.spark_app_name = cfgDict['spark']['app_name']
            self.spark_config_key = cfgDict['spark']['config']['key']
            self.spark_config_value = cfgDict['spark']['config']['value']

            if data_source == 'dessert':
                self.api_url = cfgDict['uploader']['dessert']['api_url']
                self.batch_size = random.randint(
                    cfgDict['uploader']['dessert']['max_batch_size'],
                    cfgDict['uploader']['dessert']['max_batch_size']
                )
                self.target_table = cfgDict['uploader']['dessert']['table']
            elif data_source == 'food':
                self.api_url = cfgDict['uploader']['food']['api_url']
                self.batch_size = random.randint(
                    cfgDict['uploader']['food']['max_batch_size'],
                    cfgDict['uploader']['food']['max_batch_size']
                )
                self.target_table = cfgDict['uploader']['food']['table']
            else:
                raise Exception("Wrong data_source parameter")
