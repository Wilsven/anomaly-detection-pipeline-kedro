# Building and Managing an Isolation Forest Anomaly Detection Pipeline with Kedro

## Overview

Anomaly (fraud) detection pipeline on credit card transaction data using Isolation Forest machine learning model and Kedro framework

## Objective

Develop a data science pipeline to detect anomalous (fradulent) credit card transactions with the use of:

- **Isolation Forest** machine learning model - For unsupervised anomaly detection
- **Kedro** - An open-source Python framework for creating reproducible, maintainable, and modular data science code. This framework helps to accelerate data pipelining, enhance data science prototyping, and promote pipeline reproducibility.

## Motivation

- Explore how unsupervised anomaly detection works, and better understand the concept and implementation of isolation forest
- Leverage Kedro framework to optimally structure data science pipeline projects

## Data

The [credit card transaction data](https://github.com/Fraud-Detection-Handbook/simulated-data-transformed) is obtained from the collaboration between Worldline and Machine Learning Group. It is a realistic simulation of real-world credit card transactions and has been designed to include complicated fraud detection issues.

## General Pipeline Structure

![Alt text](/docs/images/01_DS_Pipeline_Overview.png?raw=true)

## Anomaly Detection Pipeline Structure

![Alt text](/docs/images/05_Anomaly_Detection_Pipeline_Blueprint.png?raw=true)

## Kedro Pipeline Structure

![Alt text](/docs/images/kedro-pipeline.png?raw=true)

## Steps

1. Change path to project directory in command line
2. Initialize Conda virtual environment (create one if not done so)
   ```bash
   conda activate <YOUR_ENV>
   ```
3. Execute a pipeline
   ```bash
   kedro run
   ```
