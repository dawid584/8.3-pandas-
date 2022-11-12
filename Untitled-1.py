import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('police.csv')


data= df.pivot_table(values='id' , index='race', columns='signs_of_mental_illness',aggfunc='count' )
print(data)


data['percent'] = data[True] / data.apply(sum,axis=1)
print(data)



df['date'] = pd.to_datetime(df['date'])
df['week_days'] = df['date'].dt.day_name()
week_days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ile_dni = df['week_days'].value_counts().reindex(week_days)
ile_dni.plot(kind="bar")
df.head()


plt.legend()
plt.xlabel('Days')
plt.ylabel('Accidents')
plt.show()

data_0 = df.pivot_table(index='state', values='manner_of_death',aggfunc='count' )
table_3= pd.DataFrame(data_0)

data_1= pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population', header=0)
table_2 = pd.DataFrame(data_1[0])

data_2= pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations', header=2)
table_1= pd.DataFrame(data_2[0])
table_1 = table_1['Unnamed: 3'].iloc[9:][:69]
table_2 =table_2['Population estimate, July 1, 2019 [2]']
table_3 =table_3['manner_of_death']
len_1 = len(table_1)
len_2 = len(table_2)
len_3 = len(table_3)
list_1 =[]
list_2 =[]
list_3 =[]

for i in range(len_1):
   list_1.append(i)
for i in range(len_2):
   list_2.append(i)
for i in range(len_3):
   list_3.append(i)
dictionary = {'kod stanu': table_1 , 'key': list_1 }
dictionary= pd.DataFrame(dictionary)
dictionary_2 = {'Wielkość populacji': table_2 , 'key': list_2  }
dictionary_2 = pd.DataFrame(dictionary_2)
state_table= pd.merge(dictionary ,dictionary_2 , how='inner' ,on='key')
dictionary_3 = {'ilość wypadków-zgonów': table_3, 'key': list_3}
dictionary_3 = pd.DataFrame(dictionary_3)
state_table= pd.merge(state_table ,dictionary_3 , how='inner' ,on='key')
state_table['Ilość zgonów na 1000']= (state_table['ilość wypadków-zgonów']/state_table['Wielkość populacji'])*1000
print(state_table)
