---
We are going to create a python function that ask the user for some information. We will use the information given by the user to create our prompt.

We will be interacting with user input we are going to use the terminal to interact with our program. The try it button below will run your code inside the terminal .

First, lets create a function that takes a list of movies and put it in a nice box. As we dont have our movie list yet, we are goign to create a sample list. 
```python
sample=["One life","Two","Potato Pie and Life"]
```
{Try It!|terminal}(python3 moflix.py)


We are going to need to create a function that takes an argument which is our movie list. That function should return the movie list in a nice Box. 
![sample](sample.png)
Our box should change base on the number of movies and the length of the items that need to fit in the box. We are going to create our function called `InBox` that first tries to get the length of the biggest element in our list. 
```python
def InBox(x):
  #this gives you the longest string
  biggest = max(x, key = len)
  #THIS gets you the length of the biggest string
  biggest=len(biggest)
```
{Try It!|terminal}(python3 moflix.py)


Now for the top of our box we are going to start and end with `+` . Then for the content in the middle we will fill it with `-`. This technique will be used for both our top and bottom. 
```python
print("+" + "-" * (biggest + 2) + "+")
```
{Try It!|terminal}(python3 moflix.py)


We want to focus on the middle part now. We will use a for loop to iterate through all our items. We'll start off with a `|` and then add our movie title. We'll then add additional whitespaces `" "` to match the length of the longest element.
```python 
for i in x:
    print("| " + i + (" "*(biggest-len(i))) + " |")
```
{Try It!|terminal}(python3 moflix.py)


Then we will go outside our for loop and add the same code we used to create the top layer, in order to create our bottom layer. 




