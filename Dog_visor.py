from PIL import Image
import numpy as np
import os

def simulate_dog_vision(input_path):
    # Load the image
    img = Image.open(input_path).convert('RGB')
    img_array = np.array(img)

    # Scientifically-informed transformation matrix
    transform_matrix = np.array([
        [0.625, 0.375, 0.0],
        [0.7,   0.3,   0.0],
        [0.0,   0.0,   1.0]
    ])

    # Apply the transformation
    dog_vision_array = np.tensordot(img_array, transform_matrix.T, axes=1)
    dog_vision_array = np.clip(dog_vision_array, 0, 255).astype('uint8')
    dog_vision_img = Image.fromarray(dog_vision_array)

    # Construct output path with "-t" suffix
    folder, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}-t{ext}"
    output_path = os.path.join(folder, output_filename)

    # Save and show
    dog_vision_img.save(output_path)
    dog_vision_img.show()

# Example usage
simulate_dog_vision('yourFileName.png')       #change with your file name
