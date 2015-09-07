# edx

This repository contains the source code for the edx course [Introduction to computer science](https://www.edx.org/course/cs-all-introduction-computer-science-harveymuddx-cs005x)

Table Of Contents
* Python Variable
* Python Data Structures
* Python Classes and Objects
* Mid Term
* End Terms


Blockquote Check


> # This is a heading inside of a blockquote.
>
> Here’s the text of paragraph 1 in the blockquote
>
> > > Here’s a quote within a quote
>
> Here’s the text of paragraph 2 in the blockquote


Code check

```
import time
map1={}
def fib(n):
    if n in map1:
        return map1[n]
    if n==0 or n ==1:
        map1[n]=n
        return n
    else:
        val=fib(n-1)+fib(n-2)
        map1[n]=val
        return val
start_time = time.time()
        
for i in range(100):
    print fib(i),        
print ''    
print("--- %s seconds ---" % (time.time() - start_time))
    
```

Inline code

In order the set a varaible do `a = 5`, it will set 5 as a  values

This is a url <http://www.example.com>

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Head oveer to sample page to sample text [Sample](https://github.com/joed7/edx/blob/master/sample.md)
