import pandas as pd
import numpy as np

def base_line_predict(X_test, X_train, y_train, numeric_class = False):
    """
    Возвращает среднюю классу цену 
    """
    if numeric_class == True:
        a_mean = y_train.loc[X_train[X_train['class'] == 0].index].mean()
        b_mean = y_train.loc[X_train[X_train['class'] == 1].index].mean()
        c_mean = y_train.loc[X_train[X_train['class'] == 2].index].mean()
        d_mean = y_train.loc[X_train[X_train['class'] == 3].index].mean()
    else:
        a_mean = y_train.loc[X_train[X_train['class'] == 'a'].index].mean()
        b_mean = y_train.loc[X_train[X_train['class'] == 'b'].index].mean()
        c_mean = y_train.loc[X_train[X_train['class'] == 'c'].index].mean()
        d_mean = y_train.loc[X_train[X_train['class'] == 'd'].index].mean()
    y_pred = pd.Series(index = X_test.index)
    if numeric_class == True:
        y_pred.loc[X_test[X_test['class'] == 0].index] = a_mean
        y_pred.loc[X_test[X_test['class'] == 1].index] = b_mean
        y_pred.loc[X_test[X_test['class'] == 2].index] = c_mean
        y_pred.loc[X_test[X_test['class'] == 3].index] = d_mean
    else:
        y_pred.loc[X_test[X_test['class'] == 'a'].index] = a_mean
        y_pred.loc[X_test[X_test['class'] == 'b'].index] = b_mean
        y_pred.loc[X_test[X_test['class'] == 'c'].index] = c_mean
        y_pred.loc[X_test[X_test['class'] == 'd'].index] = d_mean
    return y_pred