# Hypothyroid Prediction
  
Hypothyroid diseases (underactive thyroid) is a condition in which the body doesn't produce enough of important thyroid 
hormones. The condition may lead to various symptoms at late ages.  More information about the disease is available at 
https://www.mayoclinic.org/diseases-conditions/hypothyroidism/symptoms-causes/syc-20350284 . 

## The Data  

The data was from:  http://archive.ics.uci.edu/ml/datasets/thyroid+disease. I used "allhypo.data" for the analysis. 
"allhypo.names" contains the column names of the data. Include the info about primary data processing in the Jupyter notebook list below. 
* Data processing File: Hypothyroid_Get_Data.ipynb

The data contains several categorical data and several thyroid 
hormone measurements. Several thyroid hormone (T3, TT4, FTI) levels are reduced in disease samples. 

![thyroid hormones](https://user-images.githubusercontent.com/35440469/42401663-bd7c9cce-8144-11e8-8a03-0a0d4e3df302.png)

There are 4 class samples in the data set as 'negative'(class 0), 'primary hypothyroid'(class 1), 'compensated hypothyroid' 
(class 2) and 'secondary hypothyroid' (class 3). There are only two instances of class 3. The porject was mainly focus on class 0, class 1 and 2 classification.  


## The model performance 
I have tested several models. Only listed (1) Gaussian Naive Bayes (GaussianNB) and (2) XGBoost method here.  XGBoost perfomed signicantly better on class 1 and class 2 F1 score 0.95, 0.98 for XGBoost vs 0.92, 0.68 for GaussianNB. Only Numeric data were used in GaussianNB model, while both numeric and categorical data were used in XGBoost model.  

The Goal is to make a web application that performs reasonally fast. XGBoost doesn't require too much computation power and should be good choice for the app on both the performance and speed.   

