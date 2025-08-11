#Change here 
###============###
#DATA_PATH = r'C:\Users\uqstomur\OneDrive - The University of Queensland\Documents\Result\TeoNAM'

#MODEL = ['rrBLUP','BayesB','RKHS','RF','SVR','MLP']

#INPUT = 'Predicted_result_test_all.csv'

###============###


import pandas as pd
import os
from sklearn.metrics import mean_squared_error
import scipy.stats


# Function to calculate the metrics
def metric(data):
    mse = mean_squared_error(data.loc[:,'actual'],data.loc[:,'ensemble'])
    r = scipy.stats.pearsonr(data.loc[:,'actual'], data.loc[:,'ensemble'])[0]
    
    return pd.Series(dict(Pearson = r, MSE = mse))

def ensemble(train, test, effect, MODEL):
    # Load prediction result from individual prediction models
    result_train = train
    result_test = test
    
    result_test['ensemble'] = result_test.iloc[:,-len(MODEL)+1:].mean(axis=1)
    result_train['ensemble'] = result_train.iloc[:,-len(MODEL)+1:].mean(axis=1)
    
    record = result_test.loc[:,list(result_test.columns[1:6])+['ensemble']].groupby(list(result_test.columns[1:5]), as_index=False).apply(metric).reset_index(drop=True)
    record = record.rename(columns={"Pearson": "Pearson correlation"})
    record['type'] = 'ensemble'
    
    effect = pd.concat([effect.iloc[:,:5],
                        effect.iloc[:,5:].abs().div(effect.iloc[:,5:].abs().sum(axis=1),axis=0)
                       ], axis=1)
    
    effect_ensemble = pd.DataFrame()
    cnt = 0
    for kkk in range(len(MODEL)):
        selected = effect[effect['type']==MODEL[kkk]].reset_index(drop=True)
        if selected.shape[0] != 0:
            if effect_ensemble.shape[0] == 0:
                effect_ensemble = selected
                cnt += 1
            else:
                effect_ensemble.iloc[:,5:] += selected.iloc[:,5:] 
                cnt += 1
    
    effect_ensemble.iloc[:,5:] = effect_ensemble.iloc[:,5:] / cnt
    effect_ensemble['type'] = 'ensemble'
        
    return result_train, result_test, record, effect_ensemble

