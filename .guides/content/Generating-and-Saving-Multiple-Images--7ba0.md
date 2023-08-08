Now that we can get the url for the 3 images we are going to save them in different files. The button below after the try it button are setups to open the following file names:
* image_name1.jpg
* image_name2.jpg
* image_name3.jpg

Now remember that we previously have a technique we previously used to save our image.
we are going to use that save the 3 images
```python
img_data = requests.get(image_url1).content
with open('image_name1.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(image_url2).content
with open('image_name2.jpg', 'wb') as handler:
    handler.write(img_data)
img_data = requests.get(image_url3).content
with open('image_name3.jpg', 'wb') as handler:
    handler.write(img_data)
```


{Try it!}(python3 imageGen.py 1)
[Click here to get image 1](close_file image_name1.jpg panel=1; open_file image_name1.jpg panel=1) 
[Click here to get  image 2](close_file image_name1.jpg panel=1; open_file image_name2.jpg panel=1) 
[Click here to get image 3](close_file image_name2.jpg panel=1; open_file image_name3.jpg panel=1) 

If you click on every single click here buttons and you got a different image then you are on the right track. Since we are using python lets start by cleaning up our code a bit. Making our code look a little more clean.  

For starters in order to better see the change that our code worked we are going to switch the prompt from  ninja cat to ninja birds. We are going to remove everything the first time we mention `img_data = requests.get(image_url1).content`. 


```python
prompt="digital art of ninja bird "
```
Now that we have standard style to name our it makes its easy for us to use python function like enumerate to loop through and create our file. All we have to do is simply, change the values from 1 to 2 to 3. 
```python
for i, image_url in enumerate([image_url1, image_url2, image_url3], start=1):
    img_data = requests.get(image_url).content
    with open(f'image_name{i}.jpg', 'wb') as handler:
        handler.write(img_data)
```

{Try it!}(python3 imageGen.py 2)
[Click here to get image 1](close_file image_name1.jpg panel=1; open_file image_name1.jpg panel=1) 
[Click here to get  image 2](close_file image_name1.jpg panel=1; open_file image_name2.jpg panel=1) 
[Click here to get image 3](close_file image_name2.jpg panel=1; open_file image_name3.jpg panel=1)

Just like that you more than half the lines of code you needed to store the different files. Using this code it should be pretty easy to replicate and save more than 3 pictures. Reminder that `n` has a max value of 10. 

|||guidance 
The following is the sample code that should work for the last page 
```python
import os
import openai
import secret
import requests
openai.api_key=secret.api_key

response = openai.Image.create(
  prompt="digital art of ninja bird ",
  n=3,
  size="256x256"
)

image_url1 = response['data'][0]['url']
image_url2 = response['data'][1]['url']
image_url3  = response['data'][2]['url']

for i, image_url in enumerate([image_url1, image_url2, image_url3], start=1):
    img_data = requests.get(image_url).content
    with open(f'image_name{i}.jpg', 'wb') as handler:
        handler.write(img_data)
```
|||
You've successfully learned how to generate multiple images with OpenAI DALL-E and store them as separate files using Python. You have also learned how to clean up your code by using loops and variables.

Now you can easily generate and save up to 10 images per API call, by setting the 'n' parameter and using the provided code sample. Remember that you can use more descriptive prompts to get better results, and feel free to experiment with the 'n' parameter and the prompt to generate a variety of creative images for your projects.

{Check It!|assessment}(multiple-choice-3723583746)
