import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

music_data=pd.read_csv('music.csv')
x=music_data.drop(columns=['genre'])
y=music_data['genre']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=DecisionTreeClassifier()
model.fit(x_train,y_train)

age=int(input("Enter your age :"))
gender=input("Enter your gender(m/w)) :")


if gender=='m':
    gend=1
else :
    gend=0
list=model.predict([[age,gend]])
for i in list:
    prediction=i;
print("Would you like to hear {} music ?".format(prediction))

