from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration

def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
        #report_page_file_path=Configuration().get_data_validation_config()
        #print(report_page_file_path)
    except Exception as e:
        logging.info(f"{e}")
        print(e)




if __name__=="__main__":
    main()
