import yaml


class Config:
    def __init__(self, config_path):
        with open(config_path) as cp:# контекстный менеджер
            read_data = yaml.load(cp, Loader=yaml.FullLoader)

            self.food_url = read_data['uploader']['food']['url']
            self.food_min_batch_size = read_data['uploader']['food']['max_batch_size']
            self.food_max_batch_size = read_data['uploader']['food']['max_batch_size']
            self.food_table = read_data['uploader']['food']['table']

            self.dessert_url = read_data['uploader']['dessert']['url']
            self.dessert_min_batch_size = read_data['uploader']['dessert']['max_batch_size']
            self.dessert_max_batch_size = read_data['uploader']['dessert']['max_batch_size']
            self.dessert_table = read_data['uploader']['dessert']['table']

            self.db_mode = read_data['db_connect']['mode']
            self.db_url = read_data['db_connect']['url']
            self.db_properties = read_data['db_connect']['properties']


