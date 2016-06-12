import pandas as pd
data = pd.read_csv('faculty.csv', skipinitialspace = True)
data['last_name_format'] = data.name.apply(lambda x: (x.split()[-1], x.split()[0]))

q8_dict = data[['degree', 'title', 'email', 'last_name_format']].set_index('last_name_format').T.to_dict('list')
q8_dict.items()[:3]
