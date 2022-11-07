import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('C:\Kodilla\learning-git-12\police.csv')
#################################################################################

data= df.pivot_table(values='id' , index='race', columns='signs_of_mental_illness',aggfunc='count' )
print(data)
#################################################################################

data['percent'] = data[True] / data.apply(sum,axis=1)
print(data)
#################################################################################

data_10 = df.pivot_table(index='date', values='manner_of_death',aggfunc='count').plot(kind='bar')

plt.legend()
plt.xlabel('amount of dead people')
plt.ylabel('Period')
plt.show()
############################################################################

data_0 = df.pivot_table(index='state', values='manner_of_death',aggfunc='count' )
data_1= pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population', header=0)
d = pd.DataFrame(data_1[0])


left=pd.DataFrame({'Stan':d['State'] , "key": d['Rank in states & territories, 2019']  })
right=pd.DataFrame({'Liczba ludności na 1.07.2019': d['Population estimate, July 1, 2019 [2]'] , "key": d['Rank in states & territories, 2019'] })
right_2=pd.DataFrame({'Liczba zgonów': data_0['manner_of_death'], "key": d['Rank in states & territories, 2019']})

table = pd.merge(left,right,how='right',on='key')
table_2 = pd.merge(table,right_2,how='right',on='key')
table_2['Liczba zgonów na 1000'] = (table_2['Liczba zgonów'] / table_2['Liczba ludności na 1.07.2019'] )*1000
print(table_2)