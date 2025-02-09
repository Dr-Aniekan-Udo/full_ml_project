'''import os and sys to allow you to use the system tools 
and  the exception and logger files as well'''

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# the pandas for dataframe
# sklearn for splitting data
# dataclass to create class variable

# let's create a class to handle input of data 
# with a dataclass decorator which we will only define variables

@dataclass
class DataIngestionConfig:
    # create path to store your raw, training, and test data inside a folder called artifact
    # This can also be done in a separate file maybe call it data_config, but let's do it here for easy understanding
    train_data_path: str = os.path.join('artifact', "train.csv")
    test_data_path: str = os.path.join('artifact', "test.csv")
    raw_data_path: str = os.path.join('artifact', "raw_data.csv")

# Now let's define our data ingestion class
class DataIngestion:
    def __init__(self):
        #initilized our new class with the dataingestionconfig
        self.ingestion_config=DataIngestionConfig()
    
    # create a function that contains the location of the data to ingest i.e local cloud, mongodb, etc
    # and reads it to a dataframe format to make it easy to split
    def initiate_data_ingestion(self):
        logging.info('Enters the data Ingestion method and component')
        try:
            df = pd.read_csv('notebooks\data\stud.csv')
            # it could also be read from other data source depending on what is provided
            logging.info('Finish Reading the csv dataset into dataframe')

            # write a script to make a directory if it doesn't exist
            # dirname gets the directory name with respect to the path passed as arguement
            # exist_ok ensures the folder is not deleted and recreate if it already existed 
            
            logging.info('saving the raw data')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # save the initial data to raw data path created earlier
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set,test_set=train_test_split(df, test_size=0.2,random_state=42)

            logging.info('saving the train test data as csv')

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header=True)

            logging.info('Data ingestion completed')
            
            # return the deliverables from this function
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                # this will be used in the data transformation stage
            )
        except Exception as e:
            raise CustomException(e,sys)
        
