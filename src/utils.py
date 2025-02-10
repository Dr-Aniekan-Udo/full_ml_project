import os
import sys
import dill

import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

def save_model(file_path, model):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as model_object:
            dill.dump(model,model_object)

    except Exception as e:
        raise CustomException(e,sys)