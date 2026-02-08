import os
from ML_Project.utils import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from ML_Project.config.configuration import ConfigurationManager
from ML_Project.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up

    def train_test_splitting(self):  # Fixed method name typo
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets
        train, test = train_test_split(
            data, 
            test_size=self.config.test_size,
            random_state=self.config.random_state
        )

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
