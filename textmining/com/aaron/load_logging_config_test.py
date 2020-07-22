import yaml
import logging
from logging import config
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
print(rootPath)

with open(rootPath+"/aaron/config.yaml", 'rt') as f:
    config_data = yaml.safe_load(f.read())
    config.dictConfig(config_data)

if __name__ == "__main__":
    logging.debug("================")
    logging.error("Some serious error occurred.")
    logging.warning('Function you are using is deprecated.')
