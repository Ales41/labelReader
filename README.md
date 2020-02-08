

 vehicle number plate detection and ocr using YOLO .

# Demonstration
<p align="center">
<img src="https://user-images.githubusercontent.com/14065974/41622209-bcca5a84-73c3-11e8-84e7-00eae15f3011.gif" alt="Demonstration" height="450">
</p>

# The Approach

The identifier's approach is straightforward:

1. Determine if a number plate is in the picture
2. Identify where that number plate is
3. Crop out the relevant asset
4. Read characters in the cropped picture


### Details

LabelReader uses the [Yolov3 algorithm](https://pjreddie.com) for object detection. The user can choose between the following to interact with the algorithm:
* [Darknet](https://github.com/AlexeyAB/darknet)  (Fast, C Implementation) 
* [Keras-Yolov3](https://github.com/qqwweee/keras-yolo3) (Python Implementation) 

A pretrained model is provided in the repo
link : "https://drive.google.com/open?id=1-48BHxaXTEZv3nwZEN7jAbdPLi2x40v7". 
download the model and copy it to the directory
for custom training follows this tutorial "https://medium.com/@manivannan_data/how-to-train-yolov2-to-detect-custom-objects-9010df784f36"
### Setup
if you are already installed Anaconda python you can skip this step
https://www.anaconda.com/distribution/

conda create -n plateocr pip python=3.7
pip install -r requirements.txt
apt-get install tesseract-ocr 




# Getting Started

Run the main script
python main.py




