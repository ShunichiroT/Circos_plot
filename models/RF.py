from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from scipy.stats import pearsonr
import pandas as pd
import numpy as np
import shap


def RF(train, test, params):
    
    estimators = params[0]
    features_max = params[1]
    sample_max = params[2]
    shapley_num = params[3]
    get_interaction = params[4]
    
    #Split the data sets into x and y here as specified in the original code
    train_x, train_y = train.iloc[:,:-1], train.iloc[:,-1]
    test_x, test_y = test.iloc[:,:-1], test.iloc[:,-1]
    
    #Develop & evaluate a model here as specified in the original code
    rf = RandomForestRegressor(n_estimators = estimators, random_state = 0, max_samples=sample_max, max_features=features_max)
    rf.fit(train_x, train_y)
    
    predicted = rf.predict(test_x)
    predicted_train = rf.predict(train_x)

    ## Calculate the metrics
    actual_test = test_y.values.tolist()
    mse = mean_squared_error(actual_test, predicted)
    r = pearsonr(actual_test, predicted)[0]
    
    if get_interaction == True:
        explainer = shap.TreeExplainer(rf)
        interaction_sample = pd.DataFrame(abs(explainer.shap_interaction_values(shap.sample(test_x, shapley_num))).sum(axis=0))
        interaction_sample = interaction_sample.where(np.triu(np.ones(interaction_sample.shape)).astype(bool))
        np.fill_diagonal(interaction_sample.values, np.nan)
        
        interaction_sample.index = interaction_sample.columns = test_x.columns
        interaction_sample = interaction_sample.stack(dropna=True).reset_index(drop=False)
        interaction_sample.columns = ['from','to','value']
    else:
        interaction_sample = pd.DataFrame()
    
    return r, mse, pd.DataFrame(rf.feature_importances_).T, interaction_sample, predicted, predicted_train

    