
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


#import data from csv

results=pd.read_csv('./csv_db/final.csv',sep=',', error_bad_lines=False, index_col=False)
#removing unique and unwanted columns for eda/ml purposes

results.drop(['university', 'page_no',  'exam_held_on',
        'result_date','c2_or','c4_or','c5_tw','c5_or','c5','c6','c6_tw', 'c6_or'],1,inplace =True)

# view columns of data set 
print(results.columns)
# creating integer based columns list and converting string based integer to integer
int_col = ['c1_th', 'c1_tw', 'c1_or', 'c1_in', 'c2_th', 'c2_tw',
       'c2_in', 'c3_th', 'c3_tw', 'c3_or', 'c3_in', 'c4_th', 'c4_tw',
                 'c4_in','sem_1', 'sem_2', 'sem_3',
       'sem_4', 'sem_5', 'sem_6','sem_7', 'sem_8', 'cgpi']
                                                                                                                                                                                                          
#to view all  columns

pd.set_option('display.max_columns', None)


for x in ['c1_th', 'c1_tw', 'c1_or', 'c1_in', 'c2_th', 'c2_tw',
           'c2_in', 'c3_th', 'c3_tw', 'c3_or', 'c3_in', 'c4_th', 'c4_tw',
           'c4_in','sem_3', 'sem_4', 'sem_5', 'sem_6', 'sem_7', 'sem_8', 'cgpi','college_code']:
    
    #print(x)                                              

    results[x] = results[x].apply(lambda i: i.replace('[','').replace(']','').replace("'","").replace("(","").replace(")","")) 


    if x == 'college_code':
        results[x].replace('(?<![\w\d])NAME(?![\w\d])(:)','',regex=True, inplace = True)
        
    
    if x != 'college_code':
        results[x].replace('[^0-9.]','',regex=True, inplace = True)
        results[x]=pd.to_numeric(results[x])
 

 #to remove characters from string of numbers

for x in ['department', 'college_code', 'elective', 'result', 'c1',
       'c2', 'c3', 'c4']:
    
    
    
    #print(x)                                              
    results[x].replace('[^0-9: A-z]','',regex=True, inplace = True)
     
    results[x] = results[x].apply(lambda i: i.replace('[','').replace(']','').replace("'","").replace("(","").replace(")","")) 



departments= results.department.unique()
results.fillna(0,inplace=True) 
# to find the null replace them with the zeros and drop sem marks with zeros
for x in [ 'sem_3',
       'sem_4', 'sem_5', 'sem_6', 'sem_7', 'sem_8', 'cgpi']:
        results = results[(results[x]>3) & (results['c1_or']<50)]


        
# creating new data frame of passed students 

passed = results[results['result']=='P']

colleges = results['college_code'].unique()

# filling the null values with respective colleges mean 

# for i in ['c1_th', 'c1_tw', 'c1_or', 'c1_in', 'c2_th', 'c2_tw',
#        'c2_or', 'c2_in', 'c3_th', 'c3_tw', 'c3_or', 'c3_in', 'c4_th', 'c4_tw',
#        'c4_or', 'c4_in', 'c5_tw','c5_or',]:
#     for x in colleges:
#         #print(passed[i].loc[passed['college_code']==x].mean(),str(x),i)
#         passed.fillna((0),inplace=True)


# creating new dataset for diploma students 

diploma = passed[passed['sem_1']=="['Diploma']"]

regular = passed[passed['sem_1']!="['Diploma']"]
#to remove characters from string of numbers

for x in ['sem_1','sem_2']:
    regular[x].replace('[^0-9.]','',regex=True, inplace = True)
    regular[x] = regular[x].apply(lambda i: i.replace('[','').replace(']','').replace("'","").replace("(","").replace(")","")) 
    regular[x]=pd.to_numeric(regular[x])
     

regular.to_csv("./csv_db/regular.csv")
diploma.to_csv("./csv_db/diploma.csv")



data= pd.read_csv('./csv_db/final.csv')

data =  regular.filter(['department', 'college_code',
                        'sem_1','sem_2', 'sem_3', 'sem_4', 'sem_5', 
                        'sem_6', 'sem_7', 'sem_8'], axis=1)

final = pd.get_dummies(data,columns=['department', 'college_code'],drop_first=False)

X = final.drop('sem_8',1)
y = final['sem_8']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=13)
regressor = Ridge()
  
#regressor = LinearRegression()  
regressor.fit(X_train, y_train) #training the algorithm
y_pred = regressor.predict(X_test)
print('maximum Error : ' +str( max_error(y_test,y_pred)))
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(90)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R Squared :', r2_score(y_test, y_pred))
print(df1.head(3))
df1.plot(kind='bar',figsize=(10,8))
#print(X_test.columns)

X_test.to_csv('./csv_db/template.csv',index = False)
outfile = open('regression_model_regular','wb')
pickle.dump(regressor,outfile)
outfile.close()
plt.show()


mean_df = regular.groupby(['college_code','department']).mean()
mean_df.reset_index(inplace=True)
mean_df.to_csv('./csv_db/mean_df.csv',index =False)

max_df = regular.groupby(['college_code','department']).max()
max_df.reset_index(inplace=True)
max_df.to_csv('./csv_db/max_df.csv',index =False)


min_df = regular.groupby(['college_code','department']).min()
min_df.reset_index(inplace=True)
min_df.to_csv('./csv_db/min_df.csv',index =False)


