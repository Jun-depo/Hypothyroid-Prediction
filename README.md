# Hypothyroid Prediction
  
Hypothyroid diseases (underactive thyroid) is a condition in which the body doesn't produce enough of important thyroid 
hormones. The condition may lead to various symptoms at late ages.  More information about the disease is available at 
https://www.mayoclinic.org/diseases-conditions/hypothyroidism/symptoms-causes/syc-20350284 . 

### The Data  

The data was from:  http://archive.ics.uci.edu/ml/datasets/thyroid+disease. I used "allhypo.data" for the analysis. 
"allhypo.names" contains the column names of the data. Include the info about primary data processing in the Jupyter notebook list below. 
* Data processing File: Hypothyroid_Get_Data.ipynb

The data contains several categorical data and several thyroid 
hormone measurements. Several thyroid hormone (T3, TT4, FTI) levels are reduced in disease samples. 

![thyroid hormones](https://user-images.githubusercontent.com/35440469/42401663-bd7c9cce-8144-11e8-8a03-0a0d4e3df302.png)

There are 4 class samples in the data set as 'negative'(class 0), 'primary hypothyroid'(class 1), 'compensated hypothyroid' 
(class 2) and 'secondary hypothyroid' (class 3). There are only two instances of class 3. The porject mainly focused on class 0, class 1 and 2 classification.  


### The model performance 
I have tested several models. Only listed (1) Gaussian Naive Bayes (GaussianNB) and (2) XGBoost here. The model performences were measured by f1-scores which accounts for both precision and recall. You can read more about these [here](https://en.wikipedia.org/wiki/F1_score)
* (1) XGBoost(XGB) and GaussianNB (GNB) both performed extremely well on class 0 (no disease) with F1 score 1.00 (XGBoost) vs 0.99 (GaussianNB).
* (2) XGB perfomed slightly better than GNB on class 1 (primary hypothyroid) with F1 score 0.95 (XGB) vs 0.92 (GNB).
* (3) XGB was signicantly better than GNB on class 2 (compensated hypothyroid) with F1 score 0.92 (XGB) vs 0.68 (GNB). 
The result was plotted below

<img src="Class_1_2.png" style="width:700px;height:300px;">

The Goal is to make a web application that performs well and reasonally fast. XGBoost doesn't require too much computation power and should be good choice for the app on both the performance and speed.   

### Which features are more important for the predictions?

I trained the models that took one feature (column) away from the training data, cross-validation to determine if that feature is important for the predicition. If a feature is important for hypothyroid prediction, taking it away causes the model to be less accurate in prediction.   

#### "TSH_ln", "TT4", "FTI" are import for the hypothyroid prediction among numeric columns. See the plot below.   

<img src="Missing numeric feature comparison.png" style="width:700px;height:300px;">

#### "on thyroxine", "thyroid surgery", "TT4 measured" and "referral source" are important categorical features for the prediction.  The result is shown in the graph below. 

<img src="Missing categorical feature comparison.png" style="width:700px;height:600px;">

### How does the model with the 3 numeric and 4 categorical features perform ? 

As mentioned above, the 3 numeric and 4 categorical features are important for the model prediction in a setting that the model prediction becomes less accurate when removing one of these features away. I was curious whether I could build a good model with just these 7 features. XGBoost model trained with 7 features performs quite well, slightly below the model with all features.  See the graph below for illustration.  Therefore, I will try to build an app with 7 feature XGBoost model. 

<img src="XGB_Mini_vs_allfeatures.png" style="width:900px;height:300px;">



### Things to do for an app
* Write a function that uses params obtained from processing training data, to process test data in exactly the same way.  
* Export onehotencoding params that can be used to reconstruct onehot_encoder that encodes test data in the same manner as the training data. 
* use Flask to build a web app.  I will described the app in a separate depository.  
