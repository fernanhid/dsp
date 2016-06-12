## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> REPLACE THIS WITH YOUR RESPONSE


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> REPLACE THIS WITH YOUR RESPONSE


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

>> REPLACE THIS WITH YOUR RESPONSE


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> REPLACE THIS WITH YOUR RESPONSE

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:

>import pandas as pd <br>
>data = pd.read_csv('faculty.csv', skipinitialspace = True)<br>
>data['last_name'] = data.name.apply(lambda x: x.split()[-1])<br>
>last_names = set(data.last_name)<br>

>q6_data = data[['degree', 'title', 'email', 'last_name']]<br>

>name_dict = {}<br>
>for name in last_names:<br>
>    x = data[data.last_name == name]<br>
>    for index, row in x.iterrows():<br>
>        name_dict.setdefault(row['last_name'], []).append(row[['degree', 'title', 'email']].tolist())<br>
                                                   
>name_dict.items()[:3]<br>

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:

>import pandas as pd <br>
>data = pd.read_csv('faculty.csv', skipinitialspace = True) <br>
>data['name_format'] = data.name.apply(lambda x: (x.split()[0], x.split()[-1])) <br>

>q7_dict = data[['degree', 'title', 'email', 'name_format']].set_index('name_format').T.to_dict('list') <br>
>q7_dict.items()[:3] <br>

####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

[('Bellamy',[['Sc.D.','Associate Professor of Biostatistics','bellamys@mail.med.upenn.edu']]),<br>
 ('Bilker', [['Ph.D.', 'Professor of Biostatistics', 'warren@upenn.edu']]),<br>
 ('Bryan', [['PhD', 'Assistant Professor of Biostatistics', 'bryanma@upenn.edu']])] <br>
 
Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

>import pandas as pd<br>
>data = pd.read_csv('faculty.csv', skipinitialspace = True)<br>
>data['last_name_format'] = data.name.apply(lambda x: (x.split()[-1], x.split()[0]))<br>

>q8_dict = data[['degree', 'title', 'email', 'last_name_format']].set_index('last_name_format').T.to_dict('list')<br>
>q8_dict.items()[:3]<br>

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

