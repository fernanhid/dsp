# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

from datetime import datetime

date_start_dt = datetime.strptime(date_start, "%m-%d-%Y")
data_stop_dt = datetime.strptime(date_stop, "%m-%d-%Y")

x = date_start_dt - data_stop_dt
'Days Between: %r' %abs(x.days)


####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start_dt = datetime.strptime(date_start, "%m%d%Y")
data_stop_dt = datetime.strptime(date_stop, "%m%d%Y")

x = date_start_dt - data_stop_dt
'Days Between: %r' %abs(x.days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

date_start_dt = datetime.strptime(date_start, "%d-%b-%Y")
data_stop_dt = datetime.strptime(date_stop, "%d-%b-%Y")

x = date_start_dt - data_stop_dt
'Days Between: %r' %abs(x.days)
