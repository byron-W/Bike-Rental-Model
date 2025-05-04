import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler # for scaling data
from sklearn.preprocessing import PowerTransformer

def prepData(df):
    # dropping all days that aren't functioning (only 12)
    df = df.drop(df[df['Functioning Day'] == 'No'].index)

    df.rename(columns={
        'Wind speed (m/s)' : 'Wind Speed(m/s)',
        'Solar Radiation (MJ/m2)' : 'Solar Radiation(MJ/m2)'}, inplace=True)

	# dropping features
    df.drop(['Dew point temperature(C)', 'Hour', 'Holiday', 'Visibility (10m)', 'Snowfall(cm)', 'Functioning Day'], axis = 1, inplace=True)
    
    # One-hot Encoding Seasons
    df = pd.get_dummies(df, columns=['Seasons'], drop_first=False, prefix='', prefix_sep='')
    
    # Creating Weekend vs Weekday
    df['Weekend'] = df['Date'].dt.weekday.apply(lambda x: 1 if x >= 5 else 0)

    # Converting booleans to integers
    df = df.astype({col: int for col in df.select_dtypes('bool').columns})

    agg_dict = {
		'Rented Bike Count' : 'sum',
		'Temperature(C)' : 'mean',
		'Humidity(%)' : 'mean',
		'Wind Speed(m/s)': 'mean',
		'Solar Radiation(MJ/m2)' : 'max',
		'Rainfall(mm)' : 'sum', # taking the sum of rain makes the data more meaningful because we have a lot of hours without it, making it too imbalanced if we avg, this might help
		'Spring' : 'first',
		'Summer' : 'first',
        'Autumn' : 'first',
		'Winter' : 'first',
        'Weekend' : 'first'
	}
    df = df.groupby('Date').agg(agg_dict) # turning hourly data into daily data

    # # Creating interaction features for each season
    season_cols = ["Summer"]  
    for col in season_cols:
        df[f"{col}*Temp"] = df[col] * df["Temperature(C)"] 
    return df

def transformData(Xtrain, Xtest, ytrain, ytest):
	# Taking out our non-numerical features from the scaler
    scale_columns = ['Temperature(C)', 'Humidity(%)', 'Wind Speed(m/s)', 'Solar Radiation(MJ/m2)', 'Rainfall(mm)', 'Summer*Temp']
    no_scale = ['Spring', 'Summer', 'Autumn', 'Winter', 'Weekend']

	# Separating numerical data from the rest
    no_scale_train = Xtrain[no_scale]
    no_scale_test = Xtest[no_scale]
    train_to_scale = Xtrain[scale_columns]
    test_to_scale = Xtest[scale_columns]
    
	# standardizing all features
    scaler = StandardScaler()
    scaled_x_train = scaler.fit_transform(train_to_scale)
    scaled_x_test = scaler.transform(test_to_scale)

    # converting scaled data into dataframes to concat
    scaled_x_train = pd.DataFrame(scaled_x_train, index=Xtrain.index, columns=train_to_scale.columns)
    scaled_x_test = pd.DataFrame(scaled_x_test, index=Xtest.index, columns=test_to_scale.columns)
    
    # concating the non-numerical data with the numerical
    Xtrain = pd.concat([scaled_x_train, no_scale_train], axis=1)
    Xtest = pd.concat([scaled_x_test, no_scale_test], axis=1)
    return Xtrain, Xtest, ytrain, ytest