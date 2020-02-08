

 vehicle number plate detection and ocr using YOLO .

# Demonstration
<p align="center">
<img src="https://drive.google.com/open?id=12WOtxsVp-8fZhbOFICzuteW6Zu9goOzf" alt="Demonstration" height="450">
</p>

# The Approach

The identifier's approach is straightforward:

1. Determine if a number plate is in the picture
2. Identify where that number plate is
3. Crop out the relevant asset
4. Read characters in the cropped picture


### Details

1. LabelReader uses the [Yolov3 algorithm](https://pjreddie.com) for object detection. The user can choose between the following to interact with the algorithm:
* [Darknet](https://github.com/AlexeyAB/darknet)  (Fast, C Implementation) 
* [Keras-Yolov3](https://github.com/qqwweee/keras-yolo3) (Python Implementation) 

2. A pretrained model can be downloaded
3. Link : "https://drive.google.com/open?id=1-48BHxaXTEZv3nwZEN7jAbdPLi2x40v7". 
4. Download the model and copy it to the directory
5. For custom training follows this tutorial "https://medium.com/@manivannan_data/how-to-train-yolov2-to-detect-custom-objects-9010df784f36"
### Setup
1. If you are already installed Anaconda python you can skip this step
https://www.anaconda.com/distribution/

2. conda create -n yolo pip python=3.7
3. conda activate yolo
4. pip install -r requirements.txt
5. apt-get install tesseract-ocr 
6. ./darknet




# Getting Started

Run the main script
1. python main.py




