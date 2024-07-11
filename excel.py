""" Class for handling excel manipulation """

import os
import pandas as pd
from datetime import date
from logger import Logger

class Excel:

    def __init__(self, folder: str, log: object):
        self.dir = date.today().strftime("%m-%d-%y") + '-News.xlsx' 
        self.filename = os.path.join(folder, self.dir)
        if not os.path.exists(folder):
            os.mkdir(folder)
        self.log = log
        

    def insert_data(self, data: list):
        try:
            df = pd.DataFrame(data)
            df.to_excel(self.filename)
        except Exception as error:
            self.log.register_exception("Could not insert data on excel file. Error %s")
