
Write a function `chain()` that takes a list of prompts and generates images based on the prompts. The function should use chaining to generate the images. The function should save the images to the current directory, using the following convention: `test{i+1}.jpg`, where `i` is the index of the prompt in the list. Please make sure the images are `256x256`.

For example, if the list of prompts is `["A cat", "A dog", "A bird"]`, the function should generate three images:

- `test1.jpg`: An image of a cat
- `test2.jpg`: An image of a dog
- `test3.jpg`: An image of a bird
The function should be able to handle any number of prompts in the list


{Try it!|terminal}(python3 exerc.py)

[Click here to refresh your image 1](close_file test1.jpg panel=1; open_file test1.jpg panel=1) 
[Click here to refresh your image 2](close_file test2.jpg panel=1; open_file test2.jpg panel=1) 
[Click here to refresh your image 3](close_file test3.jpg panel=1; open_file test3.jpg panel=1)
|||guidance
import os
import openai
import requests
import secret

openai.api_key=secret.api_key



# Generate and save the images
def chain(prompts):
  for i, prompt in enumerate(prompts):
    response = openai.Image.create(
      prompt=prompt,
      n=1,
      size="256x256"
    )

    # Get the image URL from the response
    image_url = response['data'][0]['url']

    # Download and save the image
    img_data = requests.get(image_url).content
    with open(f"test{i+1}.jpg", 'wb') as handler:
        handler.write(img_data)
|||

{Check It!|assessment}(code-output-compare-3899860473)