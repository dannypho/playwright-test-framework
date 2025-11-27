import yaml
import os

class ConfigReader:
    _config = None
    
    @staticmethod
    def get_config():
        if ConfigReader._config is None:
            config_path = os.path.join(
                os.path.dirname(__file__), 
                '..', 
                'config', 
                'config.yaml'
            )
            with open(config_path, 'r') as file:
                ConfigReader._config = yaml.safe_load(file)
        return ConfigReader._config
    
    @staticmethod
    def get(key):
        return ConfigReader.get_config().get(key)
    
    @staticmethod
    def get_base_url():
        return ConfigReader.get('base_url')
    
    @staticmethod
    def get_browser():
        return ConfigReader.get('browser')
    
    @staticmethod
    def is_headless():
        return ConfigReader.get('headless')
    
    @staticmethod
    def get_timeout():
        return ConfigReader.get('timeout')