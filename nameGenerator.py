import pandas as pd
import random

colNames = ['LastName']
colNames1 = ['FirstName', 'Sex', 'Blank']

data = pd.read_csv('lastNames.csv', names=colNames)
data1 =  pd.read_csv('Names.csv', names=colNames1)

FirstName = data1.FirstName.tolist()
LastName = data.LastName.tolist()
Sex = data1.Sex.tolist()

OutputFirstName = random.choice(FirstName)
OutputLastName  = random.choice(LastName).lower().capitalize()

name = "{} {}".format(OutputFirstName,OutputLastName)
print(name)
