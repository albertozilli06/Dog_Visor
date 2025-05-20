# Dog_Visor
Dog Vision Simulator
This is a small Python script that simulates how dogs perceive colors.

It was inspired by a real-world observation: dogs often miss toys that are brightly colored (to us) when they’re on the grass — especially red or pink ones. That’s because dogs are dichromatic and don’t see red and green the way we do.

The program applies a simple color transformation matrix based on how canine cones respond to light. The output image shows an approximation of how a dog would see the original scene.

How to Use

Install dependencies:
pip install pillow

Run the script:
python dog_vision.py your_image.jpg/png

The transformed image will be saved in the same folder, with -t added to the filename.
