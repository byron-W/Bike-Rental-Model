# Introduction

DESCRIPTION: The dataset contains count of public bicycles rented per hour in the Seoul Bike Sharing System, with
corresponding weather data and holiday information. Currently Rental bikes are introduced in many urban cities for the
enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right
time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major
concern. The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes.
The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall,
Rainfall), the number of bikes rented per hour and date information.

MODELING TIPS: The dataset has marked one column as the target: functioning day. I'm not sure this makes sense: you
probably want to know how many bike rentals are predicted based on the other factors. Functioning day is basically whether
or not the bike rental shop was open that day. You could in theory delete all of the rows with the 'no' category for that
column. But, don't people sometimes book rentals in advance? In that case, wouldn't the weather on a day where
'functioning day' = 'no' affect the number of bikes rented the next 'yes' day? Could it be used as a lagging variable?

<img width="1020" alt="image" src="https://github.com/user-attachments/assets/679bd2ea-a757-4fc0-a690-b7cc09dc471a" />