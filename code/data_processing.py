import pandas as pd
from sklearn.preprocessing import StandardScaler # for scaling data
from sklearn.preprocessing import PowerTransformer

def prepData(df):
    # dropping all days that aren't functioning (only 12)
    df = df.drop(df[df['Functioning Day'] == 'No'].index)
    
    # creating a precipitation feature that acts as an interaction between rain and snow
    df['Precipitation (cm)'] = (df['Rainfall(mm)'] / 10) + df['Snowfall (cm)']
    
	# dropping features
    df = df.drop(['Dew point temperature(C)', 'Hour', 'Holiday', 'Functioning Day'], axis = 1)
    
    # One-hot Encoding Seasons
    df = pd.get_dummies(df, columns=['Seasons'], drop_first=True, prefix='', prefix_sep='')

    # Converting booleans to integers
    df = df.astype({col: int for col in df.select_dtypes('bool').columns})

    agg_dict = {
		'Rented Bike Count' : 'sum',
		'Temperature(C)' : 'mean',
		'Humidity(%)' : 'mean',
		'Wind speed (m/s)': 'mean',
		'Visibility (10m)' : 'mean',
		'Solar Radiation (MJ/m2)' : 'max',
        'Precipitation (cm)' : 'sum',
		'Rainfall(mm)' : 'sum', # taking the sum of precipitation makes the data more meaningful because we have a lot of hours without it, making it too imbalanced if we avg, this might help
		'Snowfall (cm)' : 'sum',
		'Spring' : 'first',
		'Summer' : 'first',
		'Winter' : 'first'
	}
    df = df.groupby('Date').agg(agg_dict) # turning hourly data into daily data
    
    # Creating interaction features for each season
    season_cols = ["Spring", "Summer", "Winter"]  
    for col in season_cols:
        df[f"{col}_Temp"] = df[col] * df["Temperature(C)"] 
    return df

def transformData(Xtrain, Xtest, ytrain, ytest):
	# Taking out our non-numerical features from the scaler
    scale_columns = ['Temperature(C)', 'Humidity(%)', 'Wind speed (m/s)', 'Visibility (10m)', 'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)','Precipitation (cm)']
    no_scale = ['Spring', 'Summer', 'Winter', 'Spring_Temp', 'Summer_Temp', 'Winter_Temp']

	# Separating numerical data from the rest
    no_scale_train = Xtrain[no_scale]
    no_scale_test = Xtest[no_scale]
    train_to_scale = Xtrain[scale_columns]
    test_to_scale = Xtest[scale_columns]

	# normalizing features skewed distributions (or at least attempting to)
    precip_transformer = PowerTransformer('yeo-johnson')
    train_to_scale.loc[:, 'Precipitation (cm)'] = precip_transformer.fit_transform(train_to_scale[['Precipitation (cm)']]).ravel()
    test_to_scale.loc[:, 'Precipitation (cm)'] = precip_transformer.transform(test_to_scale[['Precipitation (cm)']]).ravel()
    
    snow_transformer = PowerTransformer('yeo-johnson')
    train_to_scale.loc[:, 'Snowfall (cm)'] = snow_transformer.fit_transform(train_to_scale[['Snowfall (cm)']]).ravel()
    test_to_scale.loc[:, 'Snowfall (cm)'] = snow_transformer.transform(test_to_scale[['Snowfall (cm)']]).ravel()

    rain_transformer = PowerTransformer('yeo-johnson')
    train_to_scale.loc[:, 'Rainfall(mm)'] = rain_transformer.fit_transform(train_to_scale[['Rainfall(mm)']]).ravel()
    test_to_scale.loc[:, 'Rainfall(mm)'] = rain_transformer.transform(test_to_scale[['Rainfall(mm)']]).ravel()

	# standardizing all features
    scaler = StandardScaler()
    scaled_x_train = scaler.fit_transform(train_to_scale)
    scaled_x_test = scaler.transform(test_to_scale)

    # converting scaled data into dataframes to concat
    scaled_x_train = pd.DataFrame(scaled_x_train, index=Xtrain.index, columns=train_to_scale.columns)
    scaled_x_test = pd.DataFrame(scaled_x_test, index=Xtest.index, columns=test_to_scale.columns)
    
    # concating the non-numerical data with the numerical
    Xtrain = pd.concat([scaled_x_train, no_scale_train], axis=1).to_numpy()
    Xtest = pd.concat([scaled_x_test, no_scale_test], axis=1).to_numpy()
    return Xtrain, Xtest, ytrain, ytest
