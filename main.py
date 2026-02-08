from ML_Project.utils import logger
from ML_Project.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from ML_Project.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from ML_Project.entity.config_entity import DataValidationConfig  # Keeping this import for potential future use
from ML_Project.config.configuration import ConfigurationManager
from ML_Project.components.datatransformation import DataTransformation # Importing here to avoid circular imports          
        


def run_pipeline():
    STAGE_NAME = "Data Ingestion Stage"
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = "Data Validation Stage"
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Data Transformation Stage"
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()  # Fixed method name typo        
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


if __name__ == "__main__":
    run_pipeline()
