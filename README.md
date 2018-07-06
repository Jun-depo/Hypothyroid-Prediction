# Hypothyroid Prediction
  
Hypothyroid diseases (underactive thyroid) is a condition in which the body doesn't produce enough of important thyroid 
hormones. The condition may lead to various symptoms at late ages.  More information about the disease is available at 
https://www.mayoclinic.org/diseases-conditions/hypothyroidism/symptoms-causes/syc-20350284 . 

## The Data  

The data was from:  http://archive.ics.uci.edu/ml/datasets/thyroid+disease. I used "allhypo.data" for the analysis. 
"allhypo.names" contains the column names of the data. The data contains several categorical data and several thyroid 
hormone measurements. Several hormone levels are reduced in disease samples.   

There are 4 class samples in the data set as 'negative'(class 0), 'primary hypothyroid'(class 1), 'compensated hypothyroid' 
(class 2) and 'secondary hypothyroid' (class 3). There are only two instances of class 3. The porject was mainly focus on class
0, class 1 and 2 classification.  

The data was cleaned and scaled as in the "hypothyroid_data_processing.ipynb" file.   

## The neural Network model

The neural Network classifier (sklearn.neural_network.MLPClassifier) was initially trained on the splited training data set.  
The result was decent.  Try to improved the model, I tried random forest, logistic regression and Naive Bayes. That didn't 
seem to improve the result too much.  The data is highly unbalanced with 7.9% total class 1, 2 and 3 instances (220). The model 
seems to fit more towards class 0 negativeon-disease instances (92.1%).  I recontructed more balanced data under the similar 
situation for a different project (###link), trained the model with balanced data, that significantly improved the model 
performance. 

I separated samples of each classes. I combined randomly selected 436 class 0 instances, and all class 1 and 2 instances (218) 
at 2: 1 ratio. The data set is much more balanced, sightly bias toward class 0 to reflect the bias in the original data set. 
There are only 2 instances of class 3 , not further analysed in the project.  
¶
Since overall f1-score (calculated from precision and recall) is largely driven by large number instances of class 0. Therefore,
is not a good parameter for measuring model's performance in term of predicting diseases. ¶   
