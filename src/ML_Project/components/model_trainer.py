import os
import pandas as pd
from ML_Project.utils import logger
from sklearn.linear_model import ElasticNet
import joblib
from ML_Project.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Loading training data...")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        logger.info("Splitting features and target variable...")
        X_train = train_data.drop(columns=[self.config.target_column])
        X_test = test_data.drop(columns=[self.config.target_column])
        
        
        y_train = train_data[self.config.target_column]
        y_test = test_data[self.config.target_column]

        logger.info("Training the ElasticNet model...")
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        model.fit(X_train, y_train)

        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        logger.info(f"Saving the trained model to {model_path}...")
        joblib.dump(model, model_path)    