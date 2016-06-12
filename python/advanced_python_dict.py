#Q6
import pandas as pd
data = pd.read_csv('faculty.csv', skipinitialspace = True)
data['last_name'] = data.name.apply(lambda x: x.split()[-1])
last_names = set(data.last_name)

q6_data = data[['degree', 'title', 'email', 'last_name']]

name_dict = {}
for name in last_names:
    x = data[data.last_name == name]
    for index, row in x.iterrows():
        name_dict.setdefault(row['last_name'], []).append(row[['degree', 'title', 'email']].tolist())
                                                   
sorted(name_dict.items())[:3]

#Q7
import pandas as pd
data = pd.read_csv('faculty.csv', skipinitialspace = True)
data['name_format'] = data.name.apply(lambda x: (x.split()[0], x.split()[-1]))

q7_dict = data[['degree', 'title', 'email', 'name_format']].set_index('name_format').T.to_dict('list')
sorted(q7_dict.items())[:3]

#Q8
import pandas as pd
data = pd.read_csv('faculty.csv', skipinitialspace = True)
data['last_name_format'] = data.name.apply(lambda x: (x.split()[-1], x.split()[0]))

q8_dict = data[['degree', 'title', 'email', 'last_name_format']].set_index('last_name_format').T.to_dict('list')
q8_dict.items()[:3]
