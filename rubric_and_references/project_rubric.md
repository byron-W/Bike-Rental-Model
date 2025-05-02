# Introduction
This is the rubric for your project paper. I strongly recommend you read over it prior to starting the project, and then repeatedly throughout the semester. I also recommend that you put this into a table, and add columns for things like page numbers where you met the rubric criteria or for the name of a team member responsible for ensuring the rubric criteria is met. The rubric is meant to guide you through how to do a paper like this if you ever want to publish, and also for ensuring that you have demonstrated the knowledge you learned in class. I will rely on this rubric completely when grading your final reports, and I will also use it to guide my questions and comments during your project check-ins.

# Point Values
Total paper points = 300 points
Overall paper (30), introduction (35), business question (40), analytic question (40), data prep and exploration (50), model building and testing (50), evaluation and discussion (35) references (20). 

---  
---  

# Overall Paper Flow and Format (30 points)

## Logical Flow
- Document reads cohesively, as if written by one person.  
- Analytic process is presented step-by-step, following a clear story thread from the business problem to evaluation and conclusion without gaps.  
- Paragraphs and sections build logically, avoiding unnecessary repetition and ensuring smooth transitions between sections (objective, methods, results, implications).

## Figures and Tables
- All visuals are discussed in the text sections and contribute to the narrative.  
- At a minimum, must include diagrams such as fishbone, black box, as well as plots showing data characteristics and model results.  
- Should also include flow diagrams and other visuals to assist with understanding.  
- Must include a table of contents, a data dictionary, a table showing the algorithm steps for the final chosen approach, and a table showing model training and testing results.    
- Visuals are labeled, relevant, and improve understanding, showing a coherent relationship between diagrams.

## Readability
- Descriptions are clear, avoiding excessive technical jargon and redundancy.  
- Provides sufficient explanations for less familiar methods, avoiding over-explanation of common concepts.  
- Headings are used for each section.  
- Free of grammatical and typographical errors, with consistent formatting and logical organization.    
---  
---  

# Individual sections (points given for each section)

## Introduction (35 points)
- Summary of your whole paper (hint: write this last)  
- Clearly states the purpose or main objective of the study.  
- Concisely describes data mining techniques, algorithms, and methodologies.  
- Briefly mentions pre-processing, modeling, and evaluation techniques.  
- Summarizes specific results and explains how findings address research objectives.  
- Discusses the significance and practical or theoretical implications of the findings.  
- Demonstrates the importance of the research question.  
- Highlights unique contributions to the field.
- Demonstrates the following learning goals:   
    - Understand the CRISP-DM approach and how the data mining process is structured around it  
    - Understand and articulate the who, what, why and how of your study


## Business question and background (40 points)
- Introduces the topic with necessary background information.  
- Provides a review of relevant literature, properly cited, highlighting successes and shortcomings of each study and how each relates to this study  
- Describes how this study builds upon prior similar studies.  
- Explains the relevance and importance of the study area.  
- Clearly identifies the problem or research gap.  
- Establishes the study’s context.  
- Clearly defines the study's objectives and boundaries.  
- Describes this research’s significance and potential impact.  
- Includes a table summarizing prior related literature.
- Demonstrates the following learning goals:   
    - Learn what the business problem is and why it is important to the data mining process
    - Understand and articulate the who, what, why and how of the business question

## Analytic question (40 points)
- Articulates the research problem and objectives.  
- Explains the methods, tools, and algorithms used with sufficient detail.  
- Includes relevant visuals to clarify processes.  
- Demonstrates the appropriateness of chosen methods for the problem.  
- Mentions any customizations or innovations.  
- Links theoretical methods to their practical application in the study.  
- Highlights new methods or improvements over existing approaches.  
- Introduces novel techniques or applications, avoiding redundancy with existing literature.  
- Includes flow diagram of research, fishbone diagram, table of potential algorithms with pros and cons, any other diagram or table you feel is relevant.
- Demonstrates the following learning goals:   
    - Understand the importance of the analytic problem to data understanding and modeling  
    - Learn how to decompose the business problem into quantitative key factors and desired output  
    - Learn how to develop the conceptual (black box) model from the key factors, desired output and modeling approach  
    - Know the terms feature and target, and how they are related  
    - Understand and articulate the who, what, why and how of your study

## Data preparation and exploration (50 points)
- Identifies and describes data sources, including origin, collection process, and time frame.  
- Summarizes the dataset, including size, structure, features, and statistics.  
- Explains preprocessing steps and justifies them in the study's context.  
- Describes grouping, segmentation, or stratification and explains their relevance.  
- Demonstrates rigorous application of data analysis methods and addresses challenges.  
- Details feature selection/extraction methods and their impact on model performance.  
- Includes data dictionary with feature name, definition, unit of measurement, range, missing values, sample value.  
- Includes diagrams as needed to describe data exploration and cleaning, supported by full explanations in text, numbered appropriately.
- Demonstrates the following learning goals:   
    - Understand the different types of data and where they come from  
    - Recognize necessary data preprocessing steps   
    - Know how to deal with missing values  
    - Know what imbalanced classes are and how to deal with them  
    - Know what dimension reduction is, how to determine if it is necessary, and how to do it  
    - Know how to spot big differences in ranges across features and how to deal with them  
    - Know why normal distributions are sometimes important and how to deal with non-normal distributions  
    - Know what linearity means and what to do if relationships are not linear  
    - Know how to detect outliers, what they might mean, and how to deal with them  
    - Know how to deal with categorical features  
    - Know how to do feature engineering including what, why and how you might do it  
    - Know how to choose the best features to use in your model  
    - Know how to produce summary statistics and graphs from your data,  
    - Know how to interpret these and  
    - Know how to use the information from these to make your data prep and modeling decisions  

## Model building and testing (50 points)
- Explains why specific models were chosen and aligns them with the problem domain and data characteristics.  
- Describes model implementation, libraries used, and hyperparameter tuning.  
- Details and justifies evaluation metrics (e.g., accuracy, precision, recall).  
- Clearly interprets results from an analytic perspective and links findings to objectives.  
- Compares results across models and scenarios, linking outcomes to methodology and justifying the best performing model.  
- Clearly details process of sweeping the hyperparameter space, including specific hyperparameters and value ranges and reasons for adjusting these. You may use a table to summarize, but there also must be description in the text.  
- Validates conclusions with evidence and robust methodologies.  
- Provides sufficient detail to replicate the modeling process.  
- Acknowledges limitations and describes mitigation steps.  
- Includes black box diagram, algorithm process list (examples provided), table of training and testing results, diagrams showing how algorithm works (for examples, see class slides), fully explained technical reasons for all modeling decisions, plots showing model results.
- Demonstrates the following learning goals:   
    - Know where to find the code for models in scikit-learn  
    - Know the importance of splitting data into training and testing datasets  
    - Know the different types of cross validation and when each type should be used  
    - Know what hyperparameters are and how they are used  
    - Know the different ways to sweep the hyperparameter space (grid, random, etc.), and the benefits of each  
    - Know the different metrics for evaluating different kinds of models, and which ones are appropriate for yours  
    - Know how to set goals and objectives for your models  
    - Be able to produce a table of metrics and results from multiple model configurations, types, and hyperparameter values  
    - Know how to identify model overfitting, what it means and how to address it  
    - Know how to interpret and report the results of model tuning and testing  
    - Know the difference between supervised and unsupervised learning  
    - Know the different supervised learning approaches (regression, classification), which is appropriate for your model and why
    - Know the different unsupervised learning approaches (clustering, association rule mining), which is appropriate for your model and why
    - Know the testing metrics and objectives related to each approach  
    - Know the different algorithms under each approach, and how to determine which is best  
    - Know how your data can help you with your modeling decision  
    - Know the requirements, assumptions and limitations of each algorithm  
    - Know how to produce visualizations from each approach / algorithm type  
    - Be able to describe the optimal model configuration resulting from your testing, including the relationship of the features to the target  
    - If using regression: describe the final regression equation with the model coefficients  
    - If using classification: describe which features were most useful in classifying data points  
    - If using association rules mining: describe which rules rated highest, and what this means
    - If using clustering: describe which attributes were most significant in defining the clusters
    - Know when to use unsupervised learning to prepare data for supervised learning, and be able to cite one example, and discuss whether or not it is appropriate for your model and why
    - Be able to interpret these results in terms of how the model answers the question  

## Evaluation and discussion (35 points) 
- Provides both a high level explanation of the analytic results (using analytic terms) and a discussion of the results (not in analytic terms), in the context of the business problem. This must not be another deep dive into the quantitative results: you should have done that in the prior section. This is a summary, in terms of the business problem.
- Explains the significance of results in the study’s context.  
- Evaluates strengths and limitations, discussing issues like bias or error patterns.  
- Links findings to real-world scenarios and decision-making.  
- Provides actionable advice and answers based on the results
- Discusses the generalizability of results and limitations affecting validity.  
- Identifies areas for future research and suggests methodologies to extend findings.
- Demonstrates the following learning goals:   
    - Know how to interpret the results of your study in terms of the business problem, and communicate these results effectively
    - Know how to answer the business question

## References (20 points) 
- Uses references.bib file  
- References cited properly throughout paper