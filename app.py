from __future__ import print_function

from flask import Flask, render_template, request
import boto3
import pandas as pd
from PIL import Image
import os
import io
from time import sleep

from config import *
from utils.darknet_classify_image import *
from utils.tesseract_ocr import *
import utils.logger as logger
import sys
import time
import re
from operator import itemgetter
PYTHON_VERSION = sys.version_info[0]
OS_VERSION = os.name
import pandas as pd
import cv2

import os,cv2,pytesseract
from flask import Flask, render_template, request,jsonify
from PIL import Image
import ftfy
import json
import re
import io
import csv
import sys
import glob
from flask import send_file


application = app = Flask(__name__)  

UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

 
@app.route('/')  
def file():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        file = request.files['file']
        file.filename = "temp.jpg"
        file.save(file.filename)
      
      
        

        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print(f)

        
        # print(file.filename)
        
        class PlateOCR():
                ''' Finds and determines if given image contains required text and where it is. '''

                def init_vars(self):
                        try:
                                self.DARKNET = DARKNET
                                
                                self.TESSERACT = TESSERACT
                                

                                return 0
                        except:
                                return -1

                def init_classifier(self):
                        ''' Initializes the classifier '''
                        try:
                                if self.DARKNET:
                                # Get a child process for speed considerations
                                        logger.good("Initializing Darknet")
                                        self.classifier = DarknetClassifier()
                                
                                if self.classifier == None or self.classifier == -1:
                                        return -1
                                return 0
                        except:
                                return -1

                def init_ocr(self):
                        ''' Initializes the OCR engine '''
                        try:
                                if self.TESSERACT:
                                        logger.good("Initializing Tesseract")
                                        self.OCR = TesseractOCR()
                                
                                if self.OCR == None or self.OCR == -1:
                                        return -1
                                return 0
                        except:
                                return -1

                def init_tabComplete(self):
                        ''' Initializes the tab completer '''
                        try:
                                if OS_VERSION == "posix":
                                        global tabCompleter
                                        global readline
                                        from utils.PythonCompleter import tabCompleter
                                        import readline
                                        comp = tabCompleter()
                                        # we want to treat '/' as part of a word, so override the delimiters
                                        readline.set_completer_delims(' \t\n;')
                                        readline.parse_and_bind("tab: complete")
                                        readline.set_completer(comp.pathCompleter)
                                        if not comp:
                                                return -1
                                return 0
                        except:
                                return -1

                def prompt_input(self):
                        
                        
                                filename = str(input(" Specify File >>> "))
                        

                from utils.locate_asset import locate_asset

                def initialize(self):
                        if self.init_vars() != 0:
                                logger.fatal("Init vars")
                        if self.init_tabComplete() != 0:
                                logger.fatal("Init tabcomplete")
                        if self.init_classifier() != 0:
                                logger.fatal("Init Classifier")
                        if self.init_ocr() != 0:
                                logger.fatal("Init OCR")
                

                def find_and_classify(self, filename):
                        ''' find the required text field from given image and read it through tesseract.
                            Results are stored in a dicionary. '''
                        start = time.time()
                        

                        #------------------------------Classify Image----------------------------------------#

                        
                        logger.good("Classifying Image")
                        
                        coords = self.classifier.classify_image(filename)
                        #lines=str(coords).split('\n')
                        inf=[]
                        for line in str(coords).split('\n'):
                                if "sign" in line:
                                        continue
                                if "photo" in line:
                                        continue
                                if 'left_x' in line:
                                        info=line.split()
                                        left_x = int(info[3])
                                        top_y = int(info[5])
                                        inf.append((info[0],left_x,top_y))
                        

                        time1 = time.time()
                        print("Classify Time: " + str(time1-start))

                        # ----------------------------Crop Image-------------------------------------------#
                        logger.good("Finding required text")
                        cropped_images = self.locate_asset(filename, self.classifier, lines=coords)
                        print("cropping images")
                        print(cropped_images)
                        
                        
                        time2 = time.time()
                        

                        
                        #----------------------------Perform OCR-------------------------------------------#
                        
                        ocr_results = None
                        
                        if cropped_images == []:
                                logger.bad("No text found!")
                                return None      
                        else:
                                logger.good("Performing OCR")
                                ocr_results = self.OCR.ocr(cropped_images)
                                print(ocr_results)
                                print(filename)
                                k=[]
                                v=[]
                                
                                
                                fil=filename+'-ocr'
                                #with open(fil, 'w+') as f:
                                for i in range(len(ocr_results)):
                                                
                                                                v.append(ocr_results[i][1])
                                                                k.append(inf[i][0][:-1])
                                                                
                                #k.insert(0,'Filename')
                                #v.insert(0,filename)
                                t=dict(zip(k, v))
                                print(t)
                                

                        
                        time3 = time.time()
                        print("OCR Time: " + str(time3-time2))

                        end = time.time()
                        logger.good("Elapsed: " + str(end-start))
                        print(t)
                        return t
                    
                        
                        
                                
                        #----------------------------------------------------------------#

                def __init__(self):
                        ''' Run PlateOCR '''
                        self.initialize()
        if __name__ == "__main__":
                                extracter = PlateOCR()
                                tim = time.time()
                                
                                data=[]
                                
                                result=extracter.find_and_classify(UPLOAD_FOLDER+"/"+file.filename)
                                #print(df1)
                                #df=df.append(df1)
                                      
                                data.append(result)
                                
                                df=pd.DataFrame(data)
                                print(df)
                          
      
                                df.to_html("templates/detail.html")




                
                
       

       

        return render_template('detail.html')




# retrieve file from 'static/images' directory
@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory("static/images", filename)





application.run(host='0.0.0.0',debug=True)



