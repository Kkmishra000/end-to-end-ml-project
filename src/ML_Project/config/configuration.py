from pathlib import Path
from ML_Project.constants import *
from ML_Project.utils.common import read_yaml, create_directories
from ML_Project.entity.config_entity import DataIngestionConfig 
from ML_Project.entity.config_entity import DataValidationConfig
from ML_Project.entity.config_entity import DataTransformationConfig
from ML_Project.entity.config_entity import ModelTrainerConfig



class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )

        return data_ingestion_config    
    
    def get_data_validation_config(self) -> "DataValidationConfig":
        from ML_Project.entity.config_entity import DataValidationConfig

        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            test_size=self.params.train_test_split,
            random_state=self.params.random_state,
        )

        return data_transformation_config
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        model_trainer_config = self.config.model_trainer

        create_directories([model_trainer_config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(model_trainer_config.root_dir),
            train_data_path=Path(model_trainer_config.train_data_path),
            test_data_path=Path(model_trainer_config.test_data_path),
            model_name=model_trainer_config.model_name,
            alpha=self.params.ElasticNet.alpha,
            l1_ratio=self.params.ElasticNet.l1_ratio,
            target_column=self.schema.TARGET_COLUMN.name
        )

        return model_trainer_config
