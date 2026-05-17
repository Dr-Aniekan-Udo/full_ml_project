# Student Performance Predictor
**Category:** Machine Learning  
**Tech Stack:** Python, Scikit-learn, CatBoost, XGBoost, Pandas, NumPy, Seaborn, Matplotlib  
**Status:** Complete  
**Thumbnail:** assets/thumbnail.png
## Overview
An end-to-end machine learning project that predicts student math scores based on demographic and educational factors. The project analyzes how variables like gender, ethnicity, parental education, lunch type, and test preparation course affect student performance across math, reading, and writing subjects.
## Features
- **Complete ML Pipeline**: Modular architecture with data ingestion, transformation, and model training components
- **Exploratory Data Analysis**: Comprehensive EDA with visualizations showing score distributions and demographic correlations
- **Automated Preprocessing**: sklearn pipelines for numerical scaling and categorical one-hot encoding
- **Multi-Model Training**: Supports CatBoost, XGBoost, and scikit-learn algorithms
- **Custom Exception Handling**: Robust error handling with detailed logging throughout the pipeline
- **Model Persistence**: Saves trained preprocessor and models as pickle files for reuse
## Dataset
The dataset contains 1,000 student records with the following features:
- **Gender**: Male/Female
- **Race/Ethnicity**: Group A through E
- **Parental Education**: High school, some college, bachelor's, master's, etc.
- **Lunch Type**: Standard or free/reduced
- **Test Preparation**: Completed or none
- **Target Variable**: Math score (0-100)
**Data Source**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
## Key Insights from EDA
- Female students perform better overall, while male students score higher in math
- Students with standard lunch perform significantly better than those with free/reduced lunch
- Test preparation courses improve scores across all subjects
- Group D and E students show higher average performance
## Getting Started
### Prerequisites
- Python 3.8+
- uv (recommended) or pip
### Installation
```bash
# Clone the repository
git clone https://github.com/Dr-Aniekan-Udo/full_ml_project.git
cd full_ml_project
# Install dependencies
pip install -r requirements.txt
# or with uv
uv sync
# Install the package
pip install -e .
Run the Pipeline
# Run the training pipeline
python src/pipeline/train_pipeline.py
# Run prediction (after training)
python src/pipeline/predict_pipeline.py
Explore the Notebooks
# Run Jupyter to explore EDA and model training
jupyter notebook notebooks/
Project Structure
full_ml_project/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       # Train/test split and data loading
│   │   ├── data_transformation.py  # Preprocessing pipeline (scaling, encoding)
│   │   └── model_trainer.py        # Model training with multiple algorithms
│   ├── pipeline/
│   │   ├── predict_pipeline.py     # Inference pipeline
│   │   └── train_pipeline.py       # End-to-end training workflow
│   ├── exception.py                # Custom exception classes
│   ├── logger.py                   # Logging configuration
│   └── utils.py                    # Utility functions (model save/load)
├── notebooks/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb   # Exploratory data analysis
│   └── 2. MODEL TRAINING.ipynb            # Model comparison and selection
├── artifact/
│   ├── raw_data.csv                # Original dataset
│   ├── train.csv                   # Training split
│   ├── test.csv                    # Test split
│   └── preproccessor.pkl           # Saved preprocessing pipeline
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
└── README.md
Model Pipeline
1. 
Data Ingestion: Loads CSV, performs train/test split (80/20), saves to artifact folder
2. 
Data Transformation: 
- 
Numerical features: median imputation + StandardScaler
- 
Categorical features: most frequent imputation + OneHotEncoder + scaling
3. 
Model Training: Compares multiple algorithms (CatBoost, XGBoost, sklearn models)
4. 
Prediction: Loads preprocessor and trained model for inference
Tech Stack Details
Component	Technology
ML Framework	Scikit-learn
Gradient Boosting	CatBoost, XGBoost
Data Processing	Pandas, NumPy
Visualization	Seaborn, Matplotlib
Environment	Python 3.8+
License
MIT
