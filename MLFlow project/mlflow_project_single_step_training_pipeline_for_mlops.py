# -*- coding: utf-8 -*-
"""MLflow project - single step training pipeline for MLOps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10-VnVkoHRPcGmKb6qcaJQuh0c9eWAeMs

#MLflow project - single step training pipeline for MLOps with git versioning
"""

#!pip install mlflow

import mlflow
import warnings
from mlflow import projects

print(mlflow.__version__)

# Defining multiple sets of experimentation parameters for training purpose.
parameters = [
    {"n_estimator":35},
    {"n_estimator":40},
    {"n_estimator":45}
]
ml_project_uri = "https://github.com/joshir199/MLflow-project-for-Regression-Model.git"

# training regression model MLproject for different sets of parameters
# in a unified way for continuous training and experimentation pipeline
for params in parameters:
  print(" running params value: ", params)
  reg_project_run = mlflow.run(ml_project_uri, parameters=params)
  print(" project running status: ", reg_project_run.get_status())
  print("mlflow run id: ", reg_project_run.run_id)

# This model training can be done using Multi-step items defined in a sequential
# manner for steps like, Load data, ETL, ML definition and ML training.