import os
import sys
from exception import CustomException
from logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
#just giving input to dataingestion component and now data ingestion component 
# where to save the train data and test data 
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifact","train.csv")  
    test_data_path: str=os.path.join("artifact","test.csv")
    raw_data_path: str=os.path.join("artifact","data.csv")

class dataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("/home/farhan/Documents/mlproject/Notebook/data/stud.csv")
            logging.info('read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("train_test_split Initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            logging.info("ingestion of the data is completed")


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=dataIngestion()
    obj.initiate_data_ingestion()
            



