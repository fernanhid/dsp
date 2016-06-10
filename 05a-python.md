# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>Python lists and tuples are similar in that they sequence objects however tuples are immutable meaning that they cannot be changed. This allows them to be used as keys in dictionary because it prevents hashing problems, since a list can be changed it could potentially cause problems in hashing a dictionary. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>Python lists, sets, and tuples are ways to sequence objects.<br>
>What makes a set different is: <br>
>
>1. It doesn't contain any duplicate objects <br>
>2. It is unordered <br>
>3. It can only contain immutable objects, therefore it's hashable <br>
>
>Because a set is hashable, selecting an object in a set is faster than a list. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`. <br>

>Python's lambda function creates an anonymous one time function. They are used as a time saving and concise method of embedding functions in other functions without creating a function in the long form. <br>
>
> Sorted Example: <br> 
>data = [('Jarod', 'Lanier'), ('Josh', 'Waitzkin'), ('Ann', 'Makosinski')] <br>
>sorted(data, key = lambda name: name[2]) <br>
>[('Jarod', 'Lanier'), ('Ann', 'Makosinski'), ('Josh', 'Waitzkin')] <br>
>
>2. Appy Function Examples: <br>
>df.column.apply(lambda x: upper(x))<br>


###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>List comprehensions are one liners that allows you to make lists from a previous sequences of objects. <br>
>
>List Comprehension Ex: <br>
>* data = [('Jarod', 'Lanier'), ('Josh', 'Waitzkin'), ('Ann', 'Makosinski')]<br>
>last_names = [name[1] for name in data if len(name[0] >3)] <br>
>
>Map & Filter Example: <br>
>* map(lambda name: name[1], filter(lambda name: len(name[0]) > 3, data))<br>
>
>Just from the lenght of the code you can see that list comprehensions are far more concise and readable than using map and filter functions. <br>
>
>Set Example: <br>
>{number for number in [1,1,1,2,3,4,4,4]} <br>
>{1, 2, 3, 4}
>
>Dictionary Comprehension: <br>
>{name[1]: name[0] for name in data}<br>
>{'Lanier': 'Jarod', 'Makosinski': 'Ann', 'Waitzkin': 'Josh'}


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 <br>

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 <br>

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 <br>

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





