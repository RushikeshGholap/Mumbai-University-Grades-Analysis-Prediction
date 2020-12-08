
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import Ridge
from sklearn import metrics
from sklearn.metrics import r2_score,max_error
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt 
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import pickle



diploma = pd.read_csv('./csv_db/diploma.csv')


data_dip =  diploma.filter(['department', 'college_code',
                        'sem_3', 'sem_4', 'sem_5', 
                        'sem_6', 'sem_7', 'sem_8'], axis=1)
final_dip = pd.get_dummies(data_dip,columns=['department', 'college_code'],drop_first=False)
X_dip = final_dip.drop('sem_8',1)
y_dip = final_dip['sem_8']
X_train_dip,X_test_dip,y_train_dip,y_test_dip = train_test_split(X_dip,y_dip,test_size=0.33,random_state=13)
regressor_dip = Ridge() 

#regressor_dip = LinearRegression()  
regressor_dip.fit(X_train_dip, y_train_dip) #training the algorithm
y_pred_dip = regressor_dip.predict(X_test_dip)
print('maximum Error : ' +str( max_error(y_test_dip,y_pred_dip)))
df_dip = pd.DataFrame({'Actual': y_test_dip, 'Predicted': y_pred_dip})
df1_dip = df_dip.head(90)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test_dip, y_pred_dip))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test_dip, y_pred_dip))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test_dip, y_pred_dip)))
print('R Squared :', r2_score(y_test_dip, y_pred_dip))
print(df1_dip.head(3))
df1_dip.plot(kind='bar',figsize=(10,8))

X_test_dip.to_csv('./csv_db/Diploma_template.csv',index = False)
outfile = open('regression_model_diploma','wb')
pickle.dump(regressor_dip,outfile)
outfile.close()
plt.show()

min_df_dip = diploma.groupby(['college_code','department']).min()
min_df_dip.reset_index(inplace=True)
min_df_dip.to_csv('./csv_db/min_df_dip.csv',index =False)

mean_df_dip = diploma.groupby(['college_code','department']).mean()
mean_df_dip.reset_index(inplace=True)
mean_df_dip.to_csv('./csv_db/mean_df_dip.csv',index =False)

max_df_dip = diploma.groupby(['college_code','department']).max()
max_df_dip.reset_index(inplace=True)
max_df_dip.to_csv('./csv_db/max_df_dip.csv',index =False)



