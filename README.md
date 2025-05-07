# Daily Bike Demand Prediction Using Robust Regression

## Overview
This project forecasts bike rental demand using primarily weather and some time-based features. Built as part of a course on data science and data mining.
## Dataset
- Source: [UCI Machine Learning Repository](https://doi.org/10.24432/C5F62R)
- Features: Temperature, Humidity, Wind Speed, etc.
- Target: Rented Bike Count
## Models Used
- Huber Regressor
- Extra Trees Regressor
## Evaluation
- Best RMSE: **3256.63**
- Best R²: **0.8895**
- Visualizations of model performance in `\final_model\`
## Files
- `\code\`: Exploration of data and modeling
- `\data\`: Dataset and data dictionary
- `\final_report\`: Detailed final report
- `\final_model\`: Final model with visualizations
- `requirements.txt`: List of dependencies
## Running the model
1. Clone the repository
```bash
git clone https://github.com/byron-W/CDS-303
cd CDS-303/final_model
```
2. Install dependencies
`pip install -r requirements.txt`
3. Launch Jupyter Notebook:
`jupyter model.ipynb`

**DISCLAIMER:** Initially this was a repository for the group project in my CDS303 Data-Mining class, but since I did all the exploration, modeling, and overall coding for our group, this is the model based off that work. 