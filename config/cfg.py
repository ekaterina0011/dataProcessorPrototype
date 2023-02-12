import yaml


class Config:
    def __init__(self, config_path):
        with open(config_path) as cp:
            read_data = yaml.load(cp, Loader=yaml.FullLoader)
            self.url = read_data['data_source']['url']
            self.batch_size = read_data['data_source']['batch_size']