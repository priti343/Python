#patten   to   string
from re import*
re = match('a','a').group()
print(re)
re1 = match('a|b','b').group()
print(re1)
re2 = match('abc','abcd').group()
print(re2)
re3 = match('[abc]','abcd').group()
print(re3)
re4= match('[abc]+','bcd').group()
print(re4)
re5 = match('[abc]+','ccccc').group()
print(re5)
re6 = match('[abc]{5}','ababcbbaba').group()
print(re6)
re7 = match('[a-z]+','python').group()
print(re7)

