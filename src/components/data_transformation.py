import os
import sys
from dataclasses import dataclass

# import numpy and pandas to handle the dataframe
import numpy as np
import pandas as pd

# import columntransformer to handle datatransformation process
# import onehot and scaler and any other tranformation you want to perform
# import simple imputer to handle missing data
# import pipeline to enable building a pipeline for all the processes
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# import the exception and logger to handle error and logging
from src.exception import CustomException
from src.logger import logging

# import the save_model function from utils
from src.utils import save_model

# create a dataclass which you will save the preprocessor model
@dataclass
class DataTransformationConfig:
    preprocessor_mod_file_path = os.path.join('artifact',"preproccessor.pkl")

# create a data transformation class which will use pipeline to handle the transformation process
class DataTransformation:
    # initialize with the data class
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    # define the transformation model builder
    def get_data_transformer_model(self):
        # A function to create the data transformer
        try:
            # get your features as numerical and categorical based on how your grouped it in the EDA
            numerical_columns = ['reading_score', 'writing_score'] # math score is not included bcos it's the label to be predicted
            categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            
            # create pipelines for the two types of data
            num_pipeline = Pipeline(
                steps=[
                    # the transformation for numerical data are filling missing values and scaling
                    ("imputer", SimpleImputer(strategy="median")),
                     ("scaler", StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    # the categorical data need filling of missig value with most frequent, and onehotencoding. you can scale it as well
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoding",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                    # with_mean=False prevent error with scaling sparse matrics with a lot of zeros
                ]
            )
            logging.info("numerical and categorical data pipeline created")
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # use column transformer to transform the data based on the two pipeline created
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                    # the two tranformation is grouped into a list 
                    # and the tranformation pipleines given as transformer and column groups given as columns
                ]
            )
            
            logging.info("data pipeline completed")
            
            # return the transformation model as object of this function
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    # define a function to start the transformation process on our dataset saved to the artifact folder during the data ingestion process
    # the train data path and test data path should be the arguments

    def initiate_data_transformation(self,train_path,test_path):
        try:
            # get the ingested datasets into dataframe
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("train and test data read into dataframes")
            
            # get the preprocessor model
            logging.info("obtaining the preprocessor model")

            preprocessing_model = self.get_data_transformer_model()

            # assign the target column to a variable
            target_column = "math_score"

            # separate the target column from the feature in the datasets to prevent transforming the target
            train_input_features=train_df.drop(columns=[target_column],axis=1)
            train_target_feature=train_df[target_column]
            
            test_input_features=test_df.drop(columns=[target_column],axis=1)
            test_target_feature=test_df[target_column]

            logging.info("target and features separated")
            
            # transform the data and return the array created
            
            logging.info("applying the preprocessor model to the dataframe")
            
            train_input_features_array=preprocessing_model.fit_transform(train_input_features)
            test_input_features_array=preprocessing_model.transform(test_input_features)

            # merge the tranformed features with the target array to recreate the complete array of the dataset
            # this is done by concatenating it along the column axis using numpy.c_
            
            train_array = np.c_[train_input_features_array, np.array(train_target_feature)]
            test_array = np.c_[test_input_features_array, np.array(test_target_feature)]

            logging.info("data preprocessing completed")

            logging.info("saving the preprocessed data and preprocessor model")

            save_model(
                # this function is define in the src.utils file
                # assign the preprocessor model path create with dataclass earlier
                # remember the self.data_transformation_config was initialized with it's parent class
                file_path=self.data_transformation_config.preprocessor_mod_file_path,
                model=preprocessing_model
            )

            logging.info("model saving completed")

            return(
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_mod_file_path
            )


        except Exception as e:
            raise CustomException(e,sys)

