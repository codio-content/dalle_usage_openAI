import os
import importlib
from PIL import Image

# load the student's script
student_script = importlib.import_module('exerc')

def test_chain():
    # Define the prompts for the test
    prompts = ["cat", "dog", "bird"]

    # Delete the existing image files if they exist
    for i in range(len(prompts)):
        if os.path.isfile(f'test{i+1}.jpg'):
            os.remove(f'test{i+1}.jpg')

    # Run the student's function
    try:
        student_script.chain(prompts)

        # Check if the image files were created
        for i in range(len(prompts)):
            assert os.path.isfile(f'test{i+1}.jpg'), f"Image file 'test{i+1}.jpg' was not created"

            # Check if the file is a valid image file
            try:
                img = Image.open(f'test{i+1}.jpg')
                img.verify()
            except (IOError, SyntaxError) as e:
                print(f"File 'test{i+1}.jpg' is not a valid image file: {e}")

            # Check if the image dimensions are as expected
            img = Image.open(f'test{i+1}.jpg')
            assert img.size == (256, 256), f"Image size is {img.size}, but expected (256, 256)"

        print("Test passed!")
    except Exception as e:
        print(f"Test failed: {e}")

# Run the test function
test_chain()
