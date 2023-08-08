#CODIO SOLUTION BEGIN
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

#CODIO SOLUTION END