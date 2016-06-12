#1. 

from collections import Counter

data = pd.read_csv('faculty.csv', skipinitialspace = True)
list_ = [i.split() for i in data.degree]
degrees = [o.replace('.', '') for i in list_ for o in i]

Counter(degrees).items()

#2. 
data = pd.read_csv('faculty.csv', skipinitialspace = True)
data['title'] = data.title.apply(lambda x: x.replace('is', 'of'))
data.title.value_counts()

#3. 
[i for i in data.email]

#4. 
data = pd.read_csv('faculty.csv', skipinitialspace = True)
data['mail_types'] = [i.split('@')[1] for i in data.email]
data.mail_types.value_counts()
