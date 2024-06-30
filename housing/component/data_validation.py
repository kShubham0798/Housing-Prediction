from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os,sys
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection



class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        

    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if training and test file is available")
            is_train_file_exists=False
            is_test_file_exists=False

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exists=os.path.exists(train_file_path)  ## Gives bool o/p
            is_test_file_exists=os.path.exists(test_file_path)    ## Gives bool o/p

            is_available= is_train_file_exists and is_test_file_exists  ## Gives bool o/p

            logging.info(f"is train and test file exists? -> {is_available}")
            
            if not is_available:
                training_file=self.data_ingestion_artifact.train_file_path
                testing_file=self.data_ingestion_artifact.test_file_path
                message=f"Training file: {training_file} or Testing file: {testing_file} is not preset"
                logging.info(message)
                raise Exception("Training or Testing file is not available")
            
            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def validate_dataset_schema(self) ->bool:
        try:
            validation_status=False
            # Number of columns, columns name, 
            # check the value of ocean proximity
            # acceptable values     <1H OCEAN
            # INLAND
            # ISLAND
            # NEAR BAY
            # NEAR OCEAN

            validation_status=True
            
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e
        
## data_drift -> Data drift is a change in the statistical properties and characteristics of the input data.
# Drift is the change over time in the statistical properties of the data that was used to train a machine learning model. 
# This can cause the model to become less accurate or perform differently than it was designed to. 

    def save_data_drift_report(self):
        try:
            profile=Profile(section=[DataDriftProfileSection()])
        except Exception as e:
            raise HousingException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
    
        
    def is_data_drift_found(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e

    
    def initiate_data_validate(self):
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()
        except Exception as e:
            raise HousingException(e,sys) from e
        