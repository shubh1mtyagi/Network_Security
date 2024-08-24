import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_evaluation import ModelEvaluation
from networksecurity.components.model_pusher import ModelPusher

## we have to create the configure and artifact file with resepect each and every file
## based on the moduler architecture we want to create two more file congiguration file and artifact file
## first create the skelaton of it

from networksecurity.entity.config_entity import(
    TrainigPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,

)
## here we required the artifact also
from networksecurity.entity.artifact_entity import(
  TrainigPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
  
)
## here we have component configure and artifact we have to take care of this three thing along with constant and utils

## let me create some classes so we are importing trainig_pipeline class

class TrainingPipeline:
    def __init__(self):
        pass
## know start the dataingestion pART
    def start_data_ingestion(self):
        try:## writing my logic
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
## 2 Datavalidation
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
## data transformation
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
## model training
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
## model evaluation
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
##model pusher
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
## creating the master finction
    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    if __name__=='__main__':
        start_trainig()
## whenever i have to execute the trainig pipeline from my master file the method i call is this run pipeline








