import logging

logging.basicConfig(level = logging.INFO, 
                    format = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s',
                    handlers=[
                        logging.StreamHandler()
                    ])

def getLogger(name):
    return logging.getLogger(name)
