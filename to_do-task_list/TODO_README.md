# This file will hold all requirements listed in canvas for each status presentation

Our topic: Rental Riders

A bike rental company with a fleet of 4,000 bikes wants to optimize its operations by predicting daily rental demand. Accurate forecasts would enable the company to implement a rotating maintenance schedule while ensuring sufficient bike availability for customers each day. Since servicing typically takes one day and can only be conducted on operational days, the company needs a reliable prediction model to balance maintenance needs with customer satisfaction.

## Status Presentation 1:
1. Business problem slide: state the business question, provide a little background about why it is important
2. Background slide: describes prior literature supporting the importance of this problem and how it affects people
3. Analytic problem slide: showing fishbone diagram. Every entry on the fishbone must be supported by a literature reference, and I will check to ensure they are legit
4. Data summary slide: name of dataset, citation information for dataset, summary of the following: data file / structure type, # rows, # features, target name (if any).
5. Data features list: do not, under any circumstances, try to squeeze in an image of the full table. Just list the feature names. Recommendation: group them into their data types (e.g., integers, floats, categories, etc.). Be prepared to talk about what each one means, because I will ask during your presentation.
6. Data cleaning slide: here you address the issues with your data and how you dealt with them. The list of potential issues can be found in our class slides.
7. Feature selection and engineering: describe how you selected your final feature set for the model. Also talk about how you created new features, e.g., PCA components, combined features, split features, derived features, etc. 

## Status Presentation 2:
1. Model concept slide: showing black box diagram. Your inputs and output must be stated in terms of measurement units (see slides on this). Your reasons for selecting this set of features should come from feature selection and engineering. Your target should come from the business problem and be reflected in the fishbone diagram. Your model approach will be selected at this time based on the data and business problem and go into the box.
2. Modeling background slide: describe prior literature related to past efforts to model this problem. Best way to show this is with a table that shows the paper reference (title, date, authors), type of model used, and a short comment about how their approach differs from what you plan to do. If the table is too big for one slide, add more slides. 
3. Algorithm selection slide: your selection must be based on the things we talked about in class related to data characteristics and problem type. Describe one or more that you selected, and others that you rejected, and reasons for each. 
4. Hyperparameter slide: describe the hyperparameters you want to adjust for each algorithm you will use and the value ranges. Have some reasoning for your choices.
5. Metrics slide: talk about the metrics you will use for your model. Also discuss what metrics were used in the references on the model background slide. Include a discussion of what value you expect from your metrics (e.g., what % of accuracy) and support this with logic and/or literature.
6. Initial results: you should have run your model at least once now, so talk about your initial results (metrics), hyperparameter values and how you plan to improve the results in terms of the things we discussed: hyperparameter optimization, ensembles, regularization, transfer learning, gradient descent.

## Status Presentation 3:
1. Final results summary slide: these should be the results after you made the improvements discussed above. For every metric, show the average training and test results side by side in a table. Add slides for things like confusion matrix, AUC/ROC, etc.
2. Improvements slide: show improvements of your results over your initial model results.
3. Analytic results slide: here you talk a little more about the model results: what worked, what didn't, what you could do better.
4. Evaluation slide: finally, you need to answer the question. Do not use your analytic results as your answer, you need to derive some real-world actionable advice or answer to the question. When you do this slide, ask yourself the same question that I will ask you during your presentation: Does what you wrote here answer the question?
5. Next steps: conclude with some thoughts on how someone might use your work as the basis for advancing the science.
6. References slide: list all the references from your slides. Note, this does not have to be all the references you used in your paper.

<p>GitHub also provides a way to set up Projects, that provide a way to track tasks and a project plan template. In your repository, look along the menu at the top and you'll see 'Projects' which should have a '1' after it. Click on that to find these resources.