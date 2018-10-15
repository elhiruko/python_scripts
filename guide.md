# Guide


+++
Just installed keras on the laptop



This markdown guide is for automated python scripts

# Script list

* Regular expressions
  Idea is to use re.compile for doing these tasks
  
>>> phonereg = re.compile(r'\d\d')
>>> phonereg.search('123 is the 234 is 23 is 345')
<_sre.SRE_Match object at 0x7f1b717e46b0>
>>> mo=phonereg.search('123 is the 234 is 23 is 345')
>>> mo.group()
'12'
>>> help('re.findall')

>>> 
>>> mo=phonereg.findall('123 is the 234 is 23 is 345')
>>> mo
['12', '23', '23', '34']
>>> 
 

* File Management

* time 
 Time module
 import time as time
 time.sleep(seconds)


* 
