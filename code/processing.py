import pandas as pd

def prepData(df):
    # dropping all days that aren't functioning (only 12)
    df = df.drop(df[df['Functioning Day'] == 'No'].index)

	# dropping features
    df.drop(['Hour', 'Functioning Day', 'Holiday', 'Dew point temperature(C)', 'Visibility (10m)', 'Snowfall (cm)', 'Humidity(%)'], axis = 1, inplace=True)

    # renaming to make things prettier
    df.rename(columns={
        'Wind speed (m/s)' : 'Wind Speed(m/s)',
        'Solar Radiation (MJ/m2)' : 'Solar Radiation(MJ/m2)'}, inplace=True)

    # one-hot Encoding Seasons
    df = pd.get_dummies(df, columns=['Seasons'], drop_first=False, prefix='', prefix_sep='')

    # Converting booleans to integers
    df = df.astype({col: int for col in df.select_dtypes('bool').columns})

    # Creating Weekend vs Weekday
    df['Weekend'] = df['Date'].dt.weekday.apply(lambda x: 1 if x >= 5 else 0)

    agg_dict = {
		'Rented Bike Count' : 'sum',
		'Temperature(C)' : 'mean',
		'Wind Speed(m/s)': 'mean',
		'Solar Radiation(MJ/m2)' : 'max', # there's no sun at night so taking average would skew this
		'Rainfall(mm)' : 'sum', # there's a lot of hours with no rain so taking the sum works better here
        'Spring' : 'first',
		'Summer' : 'first',
        'Autumn' : 'first',
		'Winter' : 'first',
        'Weekend' : 'first'
	}
    df = df.groupby('Date').agg(agg_dict) # turning hourly data into daily data

    # creating interaction feature for each Summer * Temperature
    df["Summer*Temp"] = df["Summer"] * df["Temperature(C)"] 
    return df