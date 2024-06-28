from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",["dataset_download_url","tgz_download_dir","raw_data_dir",
                                                      "ingestion_train_dir","ingestion_test_dir"])


DataValidationConfig=namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformationConfig=namedtuple("DataTransformationConfig",["add_bedroom_per_room","tranformed_train_dir",
                                                                "transformed_test_dir","preprocessed_object_file_path"])

## stored the data transormation pickle file in ====>"preprocessed_object_file_path"
## feature engineering of "ingestion_train_dir" we get a transformed data and it will stored in ===> "tranformed_train_dir"


ModelTrainerConfig=namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

## stored the trained model pickle file in ====>"trained_model_file_path"

ModelEvaluationConfig=namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

## All model in prod is stored in ===>"model_evaluation_file_path" so that we can compare our model with prod model 

ModelPusherConfig=namedtuple("ModelPusherConfig",["export_dir_path"])

## where we export the Model push ===>"export_dir_path"