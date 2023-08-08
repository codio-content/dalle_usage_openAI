Now, let's see how you can use Python's `asyncio` and `aiohttp` libraries to make asynchronous API calls to DALL-E:

The code we are working with in the `async.py` file creates multiple tasks, each one responsible for generating an image and saving it. 
These tasks will run concurrently, which can speed up the total execution time compared to running them sequentially. Please be aware that OpenAI's API might have rate limits depending on your plan, so please be cautious about making too many concurrent requests. We are going to do just two big Try It button at the end, in order not to waste a ton of our tokens. 

### Coding


**fetch_and_save_image function**: This function is designed to download and save the image from the given URL. The function takes a session (aiohttp's ClientSession), a URL, and a path to save the image. We use aiohttp's `get()` function to make a GET request to the URL, and then use `resp.read()` to read the response content (image data) asynchronously. We then open the file at the given path and write the image data to it.
```python3
async def fetch_and_save_image(session, url, path):
    try:
        async with session.get(url) as resp:
            img_data = await resp.read()
            with open(path, 'wb') as handler:
                handler.write(img_data)
    except Exception as e:
        print(f"Unexpected error: {e}")
```
**fetch_image function:** This function makes a request to OpenAI's API to generate an image for the given prompt. The function takes a prompt and an index as input. It calls `openai.Image.create()` to generate an image and gets the image URL from the response. It then creates an aiohttp `ClientSession` and calls `fetch_and_save_image()` to download and save the image.
```python
async def fetch_image(prompt, i):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256"
        )

        # Get the image URL from the response
        image_url = response['data'][0]['url']

        # Download and save the image
        async with aiohttp.ClientSession() as session:
            await fetch_and_save_image(session, image_url, f"robot_dog_journey_{i+1}.jpg")
    except openai.api_errors.APIError as e:
        # This will catch any error returned by the OpenAI API
        print(f"API error: {e}")

    except Exception as e:
        # This is a catch-all for any other exceptions
        print(f"Unexpected error: {e}")
```



**main function:** This function creates an `asyncio` task for each prompt, adds them to a list, and then runs them concurrently using `asyncio.gather()`. This means that it will start all the tasks at the same time, and then wait for all of them to finish. This is where the asynchronous magic happens - rather than processing each prompt one by one, it starts processing all of them at once, which can significantly speed up the total execution time. It also measures the execution time by recording the time before and after the tasks are run, and then subtracts the start time from the end time.

```python
async def main():
    start_time = time.time()  # Start measuring execution time

    tasks = []
    for i, prompt in enumerate(prompts):
        tasks.append(fetch_image(prompt, i))

    await asyncio.gather(*tasks)

    end_time = time.time()  # End measuring execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
```

Your whole code outline in `async.py` should look like the following code. Additionally, to run the main function we have added `asyncio.run(main())` at the end of our code. 
```python 
import os
import openai
import aiohttp
import asyncio
import secret
import time

openai.api_key = secret.api_key

# Set the prompts
prompts = ["robot dog in a lab", "robot dog exploring the city", "robot dog watching the sunset"]

async def fetch_and_save_image(session, url, path):
    try:
        async with session.get(url) as resp:
            img_data = await resp.read()
            with open(path, 'wb') as handler:
                handler.write(img_data)
    except Exception as e:
        print(f"Unexpected error: {e}")

async def fetch_image(prompt, i):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="256x256"
        )

        # Get the image URL from the response
        image_url = response['data'][0]['url']

        # Download and save the image
        async with aiohttp.ClientSession() as session:
            await fetch_and_save_image(session, image_url, f"robot_dog_journey_{i+1}.jpg")
    except openai.api_errors.APIError as e:
        # This will catch any error returned by the OpenAI API
        print(f"API error: {e}")

    except Exception as e:
        # This is a catch-all for any other exceptions
        print(f"Unexpected error: {e}")

async def main():
    start_time = time.time()  # Start measuring execution time

    tasks = []
    for i, prompt in enumerate(prompts):
        tasks.append(fetch_image(prompt, i))

    await asyncio.gather(*tasks)

    end_time = time.time()  # End measuring execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

# Run the main function
asyncio.run(main())
```
 Use the Try It buttons below to check and compare the sync vs async time.
{Try it sync| terminal}(python3 sync.py 59)
{ Try it async | terminal}(python3 async.py 13)


Please note that the `openai.Image.create` function is a blocking operation and doesn't support async. The code above assumes that this function is asynchronous, which is not correct. To truly parallelize this, you'd need an async-compatible OpenAI library or use something like Python's `concurrent.futures` to run the blocking parts in a separate thread.

{Check It!|assessment}(multiple-choice-3012950608)
