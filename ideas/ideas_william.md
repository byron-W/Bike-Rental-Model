# Team Member: William McCarty
# Ideas
- Types of modeling we can work towards for solving our business problem after I write out the analytic one.
- [https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares](Ordinary Least Squares) 
- [https://scikit-learn.org/stable/modules/neighbors.html](Nearest Neighbors)
- Depending on whether or not we need classification or prediction, both options allow us to easily switch from one or the other.

-input/outputs for the analytic question
Output is easy, we need to build a model that can reliably predict rider demand
By doing so we can determine days which we can put stock in for maintenance without loss of potential customers.  Due specifically to not having enough bikes needed for high demand days.

### Correlation Matrix Update###

A possibility we should convert rainfall from mm to cm(To match snowfall measurements). So I did that before creating the new corr Matrices.

I also created a filtered one, which I will have to cite the professors provided code again.

This filtered one will be on a second slide after the first containing the unfiltered.  

Presentation notes:

- While analyzing our data we also created a correlation matrix of our feature set. 
- Correlation matrices as you know are just a matrix that contains correlation coefficients for each pair of variables.  These coefficients correspond to a magnitude and direction of correlation between the variables.
- Positive meaning as one increases so does the other, negative meaning as one increases the other decreases.
- We used these matrix representations to examine possible multicolinearity of our variables.  If one variable highly correlates with another it can mean it has no or unexpected effects on our models.
- This first one is a bit hard to grapple with the details due to its size so I ran it through a filter threshold based on Professor Russo's provided code. 
- Here you can see that Temperature and Dew Point temperature are highly correlated and thus are detrimental to any statistical inferences and predictions we might make with our models.
- So we decided to drop Dew point from our future model, among others like Seasons, as temperature and solar radiation are quantitative values that also change similarly with Seasons and are easier to model with than categorical data.
- #####HOW TO TRANSITION TO END SLIDE########
- 
 ##################NOTES ON MY SPEECH HERE###############################



#########################################################################

###On the Linear Regression Model###
- We should probably start building test inputs to see if we can mess with our model a bit.
- Testing things like if the temperature is 100 degrees in each of the seasons (I don't remember if he removed the one-hot encoded Seasons Column before making the model)
- Seeing how well our model works when we are extrapolating. I.E testing with data values outside our min/max values for each column.
- Then probably consider things like, well how easily can the business take these measurements each day?  Some of them are likely not easily applicable during day-to-day operations.
- If our model does not do well or makes no sense for inputs of data we've seen in more current years(the high variation of temperature, wind speeds, etc. changing due to climate change)  We may need to consider other models.
###################################
I'll look more into the models this week, and see how I can help with the next status presentation.
However Byron seems to have taken the reins so I'll try to follow his lead if he has an idea where he wants to go with this.
##################################
###Additions to liaer regression notes#####





#####Things Brad and Venus can do for background research####
-Research the typical number of bikes that can be maintained in one day by a business
-The average time it takes to do typical maintenance on a bike, gets us the hours it takes to get bikes ready.
-the average or median value of number of bikes that need maintenance per day.
- Figuring this out allows us to determine how long the bikes will be out of commission.
- If we aren't just building one model, we have to build the model that predicts likelihood of a bike needing maintenance.
###############################################################################
Status Presentation 2 Script notes
-Begin algorithm selection slides
- Everything under the sun, the whole nine yards, the full monty, everything including the kitchen sink, great idioms, and our method for algorithm selection.
- 
 For our finalists we determined these 5 are our best bet due to our metric selection process as shown earlier.
 Why are these good options for use on our dataset?
- SVR/NuSVR, resistance to overfitting, allowing it to handle new data better than others, is also great at minimizing the effect of outliers on the model.
- Random Trees Regressor like ExtraTrees and GradientBoosting Regressor, -Better handling of non-linear relationships in datasets, while also reducing overfitting.



###SKLEARN METRICS PAGE FOR EVALUATING OUR MODEL####
-https://scikit-learn.org/stable/modules/model_evaluation.html
- https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview
