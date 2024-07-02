import logging
import os
from datetime import date

class Logger:

    def __init__(self) -> None:
        self.name = date.today().strftime("%m-%d-%y") + '-NewsSearcherLog.log' 
        self.filename = os.path.join(os.getcwd(), self.name)
        logging.basicConfig(filename=self.filename,level=logging.NOTSET, format='%(asctime)s - %(levelname)s - %(message)s')


    def register_info(self, message):
        logging.info(message)


    def register_warn(self, message):
        logging.warning(message)

    
    def register_exception(self, message):
        logging.exception(message)




    







        