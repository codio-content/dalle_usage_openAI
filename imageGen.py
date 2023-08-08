import os
import openai
import requests
import secret

openai.api_key=secret.api_key

# Set the prompts
prompts = ["robot dog in a lab", "robot dog exploring the city", "robot dog watching the sunset"]

# Generate and save the images
for i, prompt in enumerate(prompts):
    try:
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

    except requests.exceptions.RequestException as e:
        # This will catch any general network error
        print(f"Network error: {e}")

    except openai.api_errors.APIError as e:
        # This will catch any error returned by the OpenAI API
        print(f"API error: {e}")

    except Exception as e:
        # This is a catch-all for any other exceptions
        print(f"Unexpected error: {e}")