import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path,'../conf/config.ini')

class ConfigUtils:
    def __init__(self,config_path=config_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_path,'utf-8')

    @property
    def host_path(self):
        value = self.config.get('default','host')
        return value

    @property
    def apikey(self):
        value = self.config.get('default', 'apikey')
        return value

config = ConfigUtils()
