import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import OneHotEncoder

column_names = ['age', 'sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication', 'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid', 'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH measured', 'TSH', 'T3 measured', 'T3', 'TT4 measured', 'TT4', 'T4U measured', 'T4U', 'FTI measured', 'FTI', 'TBG measured', 'TBG', 'referral source', 'classes']

train_ave = pd.read_json('fillna_training_average.json', lines=True)

def data_processing(data_path, train_df_ave_path):
    
    """
    This function process hypothroid data, transform data in more standard fashion to eliminate possible uneven data processing between development and test data inferences.

    Input:
    data_path:  the path to the location of the data
    train_df_ave_path: path to json file that contains training data average for numeric columns.  The average number is used to fill the missing value.   
    """
    column_names = ['age', 'sex', 'on thyroxine', 'query on thyroxine', 'on antithyroid medication', 'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid', 'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH measured', 'TSH', 'T3 measured', 'T3', 'TT4 measured', 'TT4', 'T4U measured', 'T4U', 'FTI measured', 'FTI', 'TBG measured', 'TBG', 'referral source', 'classes']
   
    df =pd.read_csv(data_path, header=None, names=column_names)
    df_class = df["classes"].str.split('.\|', 1, expand=True).rename(columns={0:'classes', 1:'id?'})
    df["classes"] = df_class["classes"]
    
    #both 'TBG', 'TBG measured' columns contain only single value for each column
    df.drop(labels=['TBG', 'TBG measured'], axis=1, index=None, columns=None, level=None, inplace=True, errors='raise')     

    # create dictionary for replacing missing value as np.nan, "f" as 0, "t" as 1, "F" as 0, "M" as 1
    repl = {"?": np.nan, "f":0, "t": 1, "F": 0, "M":1}
    df.replace(to_replace=repl, value=None, inplace=True, limit=None, regex=False, method='pad')
    # assign sex unknown to 2 
    df.loc[np.isnan(df["sex"]), 'sex'] = 2
    
    # rename different hypothyroid class to int 0, 1, 2, 3
    rename_class_labels = {'negative': 0, 'primary hypothyroid': 1, 'compensated hypothyroid':2, 'secondary hypothyroid': 3 }
    df['classes'].replace(to_replace=rename_class_labels, inplace=True)
    
    # change ref_source to numeric labels
    ref_source = {'other': 0, 'SVI': 1, 'SVHD': 2, 'SVHC': 3, 'STMW': 4}
    df['referral source'].replace(to_replace=ref_source, value=None, inplace=True, limit=None, regex=False, method='pad') 
    
    # change numeric data type from string to float
    tofloat_columns = ["age", "sex", "TSH", "T3", "TT4", "T4U", "FTI"]
    df[tofloat_columns] = df[tofloat_columns].astype(np.float32)
    # filling numeric columns nan values with average values of  columns
    fillna_columns = ['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']
    
    train_ave = pd.read_json(train_df_ave_path, lines=True)
    for i in fillna_columns: 
        df.loc[np.isnan(df[i]), i] = train_ave[i][0].astype(np.float32)
        
    df['TSH_ln'] = np.log(df['TSH'])
        
    return df
    
    
def get_Xy(df, feature_cat, feature_num): 
    
    onehot_encoder = OneHotEncoder(sparse=False, n_values=np.load('onehot_encoder_n_value_.npy'), handle_unknown='ignore')
    
    X_cat = onehot_encoder.fit_transform(df[feature_cat])
    X_num = df[feature_num].values
    
    X = np.concatenate((X_num, X_cat), axis=1) 
    y = df['classes'].values.astype(int)
    return X, y  