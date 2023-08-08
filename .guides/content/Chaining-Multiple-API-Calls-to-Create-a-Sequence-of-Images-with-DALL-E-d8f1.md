----
In the previous lessons, we have learned how to generate images using OpenAI's DALL-E API by defining specific conditions or constraints in our prompts. Today, we will take a step further and learn how to chain multiple API calls together to create a sequence of images. This technique can significantly enhance the creativity and complexity of the outputs we can generate.

### Benefits of Chaining
Chaining API calls allows us to generate multiple images in a sequence based on a set of prompts. This technique has several benefits:

**Storytelling**: By chaining prompts, we can create a sequence of images that tell a story. This can be useful in a variety of applications, from creating storyboard visuals to generating illustrative examples for educational content.

**Progressive image generation**: Chaining allows us to generate images that progressively change based on our sequence of prompts. This can be used to simulate movement, transformation, or progression over time.

**Exploring different variations**: By chaining a series of related prompts, we can generate a set of images that show different interpretations or variations of the same concept. This can help us understand how DALL-E interprets and responds to different prompts.
```python
import os
import openai
import requests
import secret

openai.api_key=secret.api_key

# Set the prompts
prompts = ["robot dog in a lab", "robot dog exploring the city", "robot dog watching the sunset"]

# Generate and save the images
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
    with open(f"robot_dog_journey_{i+1}.jpg", 'wb') as handler:
        handler.write(img_data)
```
{ Try it! | background}(bash bash.sh)

After clicking the `Try it` make sure to be give it a few more seconds so that the images can be generated even though we see the message that the code was executed.
[Click here to refresh your image 1](close_file robot_dog_journey_1.jpg panel=1; open_file robot_dog_journey_1.jpg panel=1) 
[Click here to refresh your image 2](close_file robot_dog_journey_2.jpg panel=1; open_file robot_dog_journey_2.jpg panel=1) 
[Click here to refresh your image 3](close_file robot_dog_journey_3.jpg panel=1; open_file robot_dog_journey_3.jpg panel=1)

In this example, we first define a list of prompts. Each prompt represents a different stage of the "robot dog's journey".

We then loop over each prompt in the list. For each prompt, we call the DALL-E API to generate an image that corresponds to that stage of the journey. We specify prompt as the prompt, `n=1` to generate one image per prompt, and `size="256x256"` to specify the size of the generated image.

From the API response, we extract the URL of the generated image. We then use the `requests` library to download the image from this URL.

Finally, we save each image with a unique filename that includes the index of the prompt in the list. This allows us to view the images in the order they were generated, effectively seeing the robot dog's journey unfold in sequence.

By chaining these API calls together, we can generate a sequence of images that tell a visually compelling story. This approach can be extended and adapted to generate sequences of images for a wide range of applications.

{Check It!|assessment}(multiple-choice-3284974171)

