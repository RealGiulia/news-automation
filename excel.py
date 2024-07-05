""" Class for handling excel manipulation """

import os
import pandas as pd
from datetime import date
from logger import Logger

class Excel:

    def __init__(self):
        self.dir = date.today().strftime("%m-%d-%y") + '-News.xlsx' 
        self.filename = os.path.join(os.getcwd(), self.dir)
        self.log =  Logger()
        

    def insert_data(self, data: list):
        try:
            df = pd.DataFrame(data,set_index=False)
            df.to_excel(self.filename)
        except Exception as error:
            self.log.register_exception("Could not insert data on excel file. Error %s")
