# Team Member: Byron Washington
# Ideas
## SP1
- Find out other papers/projects that have worked on this problem in the past
- With the notes in the xlsx and just thinking about it, functioning holiday seems kind of important
Weather might also affect more than one day. Lets say it snows, it'll probably affect more than one day.
And IF it's rideable the next day, the temperature would have to be high.
I have no clue on how to predict the weather so im just hoping that that factor is outside the scope of the course.
I dont think holiday would be a big factor tho, like think about it. If it's president's day is that really going to affect
me going outside and renting a bike. Not really, and if it did, it would have to be nice.
- slide 125 says "Both the data dictionary and summary statistics tables must be in your materials".
- pca notebook shows that holiday doesn't have much variance at all
- pca notebook also reiterates the correlation between temperature and dew point
## SP2
- I have no clue if we should drop seasons or not/Is winter winter or is winter cold?
Yes seasons is correlated with bike count my guess is that it's only correlated because of the temperature
We should do some exploration and see if people are going out on on weekends vs weekdays
If we can prove that season is only correlated to bike count BECAUSE of temperature, then we can drop it because it introduces colinearity that makes it harder for some regression models
We can use PCA if colinearity is a problem
- Maybe we merge date with hour and just use them in the time series as daily data?
- Find outliers to improve model
- Bayesian Optimization
- bias_var_decomp
- test scalers
- statsmodels for durbin-watson, omnibus pvalue for normality within residuals
- tree models seem to work the best, need to figure out if it's the outliers or colinearity that is causing all the other models to underperform
- test for heteroskedsticity (slide 283)
- reference slide 269
- criterion -> data doesn't follow poisson distribution so no need to check it (check w brad), only criterion we need are ones that involve mse (squared error, friedman, huber)
## SP3
- Rainfall and snowfall changed to binary (do people care how much it's raining or if it's raining or not)
	- Maybe combine into precipitation?
- Boosting
- Stacking
- Solar radiation/Visibility class imbalance (will fixing distribution fix model?)
- Wind speed is slightly skewed right
- Look for interactions between time of day and weather
- Clean up our repository (help others get commits)
	- code/data folder (use jupyter notebooks for visualizations) (all code should be there for a reason (remove old code))
	- code (provide code for visualizations where applicable)
	- references (update)
	- make visualization folder (fishbone, graphs)
- if we're giving the model and hour, then wouldn't that be predicting hourly bike demand and not daily?
	- sum bike count, avg weather, (if it rained/snowed at all that day then 1)