# Hypothyroid Prediction
  
Hypothyroid diseases (underactive thyroid) is a condition in which the body doesn't produce enough of important thyroid 
hormones. The condition may lead to various symptoms at late ages.  More information about the disease is available at 
https://www.mayoclinic.org/diseases-conditions/hypothyroidism/symptoms-causes/syc-20350284 . 

## The Data  

The data was from:  http://archive.ics.uci.edu/ml/datasets/thyroid+disease. I used "allhypo.data" for the analysis. 
"allhypo.names" contains the column names of the data. Include the info about primary data processing in the Jupyter notebook list below. 
* Hypothyroid_Get_Data.ipynb

The data contains several categorical data and several thyroid 
hormone measurements. Several thyroid hormone (T3, TT4, FTI) levels are reduced in disease samples. 

![thyroid hormones](https://user-images.githubusercontent.com/35440469/42401663-bd7c9cce-8144-11e8-8a03-0a0d4e3df302.png)

There are 4 class samples in the data set as 'negative'(class 0), 'primary hypothyroid'(class 1), 'compensated hypothyroid' 
(class 2) and 'secondary hypothyroid' (class 3). There are only two instances of class 3. The porject was mainly focus on class 0, class 1 and 2 classification.  

The data was cleaned and scaled as in the "hypothyroid_data_processing.ipynb" file.   

## The neural network model

The neural network classifier (sklearn.neural_network.MLPClassifier) was initially trained on the splited training data set.  
The result was decent.  Try to improved the model, I tried random forest, logistic regression and Naive Bayes. That didn't 
seem to improve the result too much.  The data is highly unbalanced with 7.9% total class 1, 2 and 3 instances (220). The model seems to fit more towards class 0 disease-negative instances (92.1%).  I reconstructed more balanced data under the similar situation for a different project (###link), trained the model with the more balanced data, that significantly improved the model performance. 

The same approach was used here. I separated samples of each classes from the data. I recombined randomly selected 436 class 0 instances (out of 2580 instances), and all class 1 and 2 instances (218) at 2: 1 ratio. The data set is much more balanced, sightly bias toward class 0 to reflect the bias in the original data set. There are only 2 instances of class 3, not further analyzed in the project.  

## The model performance 
Since overall average f1-score (calculated from precision and recall) is largely driven by the large number instances of class 0. Therefore, it is not a good for measuring model's performance in predicting the diseases. I calculated weighted average f1-scores of class 1 and 2 to reflect measurement of disease prediction. By this measurement, the score on test data of the model trained on balanced data is 0.06 better than the one trained on unbalanced data (0.91 vs 0.85, see bar 5 and 6 in the following figure), indicating significant improvement in predicting hypothyroid diseases. Both models have high overall average f1-scores, indicating good overall performances.  

![hypothroid classification f1-scores](https://user-images.githubusercontent.com/35440469/42402327-0f74319c-8148-11e8-97d4-aef9a5a26aa3.png)

### The code files:
hypothyroid_data_processing.ipynb ---
(processing, cleaning and scaling the data).

hypothyroid_model_unbalanced_data.ipyn ---
(the code for neural network model trained on the unbalanced data).¶

Thyroid models-balanced data.ipynb ---
(the code for neural network model trained on the balanced data).¶   
