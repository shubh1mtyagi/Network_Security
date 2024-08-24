from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


## we required config and artifact
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

## for reading the data library we required these are my essential library
import os
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List

from dotenv import load_dotenv
## creating the object of dot env
load_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)
## this is my main class
class DataIngestion:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
## i have to define some method inside the dataingestion
## creating one more method
    def export_collection_as_dataframe(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
## creating a feature store to store the important info 
    def export_data_into_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
## creating method to split the data
    def split_data_as_train_test(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
## creating the master method
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)



