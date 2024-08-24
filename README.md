# Student Performance Prediction Model

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Student Performance Prediction Model** repository! This project is a machine learning model that predicts student scores based on the number of hours studied. It was created as part of my application for the FOSS club at [Your College Name].

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model Overview](#model-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project is focused on building a linear regression model to predict student performance based on the hours studied. The model was developed using Python and Flask and is intended to serve as a practical demonstration of my skills in data science and machine learning.

## Dataset

The dataset used in this project includes the following columns:

| Hours Studied | Scores |
|---------------|--------|
| 2.5           | 21     |
| 5.1           | 47     |
| 3.2           | 27     |
| 8.5           | 75     |
| 3.5           | 30     |
| 1.5           | 20     |
| 9.2           | 88     |
| 5.5           | 60     |
| 8.3           | 81     |
| 2.7           | 25     |
| 7.7           | 85     |
| 5.9           | 62     |
| 4.5           | 41     |
| 3.3           | 42     |
| 1.1           | 17     |
| 8.9           | 95     |
| 2.5           | 30     |
| 1.9           | 24     |
| 6.1           | 67     |
| 7.4           | 69     |
| 2.7           | 30     |
| 4.8           | 54     |
| 3.8           | 35     |
| 6.9           | 76     |
| 7.8           | 86     |
| 4.2           | 49     |
| 9.5           | 90     |
| 5.8           | 63     |
| 2.3           | 23     |
| 4.7           | 50     |

> **Note**: This dataset is sourced from [Kaggle's Student Study Hours Dataset](https://www.kaggle.com/datasets/himanshunakrani/student-study-hours).

## Model Overview

The model was built using the following steps:

1. **Data Collection**: The dataset was sourced from [Kaggle's Student Study Hours Dataset](https://www.kaggle.com/datasets/himanshunakrani/student-study-hours).
2. **Data Preprocessing**: The data was cleaned and prepared for modeling.
3. **Modeling**: A linear regression model was trained to predict student scores.
4. **Deployment**: The model was deployed as a web application using Flask.
5. **Evaluation**: The model was evaluated using metrics such as Mean Absolute Error (MAE) and R² score.

### Key Features

- **Simple and Intuitive**: Easy-to-understand linear regression model.
- **Web Interface**: Users can input study hours through a web interface and receive predicted scores.
- **Educational**: Aimed at beginners looking to understand basic machine learning concepts and web development using Flask.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   
       git clone https://github.com/kevin-babu-dotcom/StudentScoreModel.git
2. Navigate to the repository
   
       cd StudentScoreModel
3. Install the required dependencies:

        pip install -r requirements.txt
4. Create a virtual environment (optional but recommended):

         python -m venv venv
         venv\Scripts\activate`
5. Install the required dependencies:
        
        pip install -r requirements.txt
## Usage

To use the model, follow these steps:

1. Run the Flask Application: Make sure you are in the project directory, then run:

        python app.py
2. Access the Web Application: Open your web browser and go to http://127.0.0.1:5000/.

3. Input Study Hours: On the web page, enter the number of study hours in the input field and submit the form to get the predicted score.

