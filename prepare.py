from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import acquire
import pandas as pd
import numpy as np


#function for doing train test split on any dataset
def tts(df):
    '''
    assigning the column of the dataframe that you want to stratify by
    '''
    x=input('stratify=')
    '''
    removing your test data from the data
    '''
    train_validate, test=train_test_split(df, 
                                 train_size=.8, 
                                 random_state=8675309, 
                                 stratify=df[x])
    '''
    splitting the remaining data into the train and validate groups
    '''            
    train, validate =train_test_split(train_validate, 
                                      test_size=.3, 
                                      random_state=8675309, 
                                      stratify=train_validate[x])
    return train, validate, test


def prep_telco():
    telco=acquire.get_telco_data()
    '''
    dropping unnecessary columns
    '''
    telco.drop(columns=(['contract_type_id', 'payment_type_id', 
                         'internet_service_type_id']), inplace=True)
    '''
    setting the customer ids to the index and dropping the column
    '''
    telco= telco.set_index('customer_id')
    '''
    adding dummies for modeling
    '''
    dummy_var=(pd.get_dummies(telco[['gender', 'partner', 'dependents', 'phone_service', 
                                    'multiple_lines', 'online_security', 'online_backup', 
                                    'device_protection', 'tech_support', 'streaming_tv', 
                                    'streaming_movies', 'paperless_billing', 
                                    'contract_type', 'internet_service_type', 
                                    'payment_type']], drop_first=True))
    telco=pd.concat([telco, dummy_var], axis=1)
    return telco