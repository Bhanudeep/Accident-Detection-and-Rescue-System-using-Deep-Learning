import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'   
import pathlib
import tensorflow as tf
import cv2
import argparse
import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import warnings
import pymongo
import matplotlib.pyplot as plt
import keras_ocr
from datetime import datetime
import smtplib
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
camerano="camera_01"
def detac():
  warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings
  tf.get_logger().setLevel('ERROR')                               
  gpus = tf.config.experimental.list_physical_devices('GPU')
  for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
  IMAGE_PATHS = 'images/acci.jpg'
  PATH_TO_MODEL_DIR = 'model/exported-models'
  PATH_TO_LABELS = 'model/exported-models/saved_model/label_map.pbtxt'
  MIN_CONF_THRESH = 0.60
  PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR + "/saved_model"
  print('Loading model...', end='')
  start_time = time.time()
  detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)
  end_time = time.time()
  elapsed_time = end_time - start_time
  print('Done! Took {} seconds'.format(elapsed_time))
  category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                      use_display_name=True)
  def load_image_into_numpy_array(path):
      
      return np.array(Image.open(path))
  print('Running inference for {}... '.format(IMAGE_PATHS), end='')
  image = cv2.imread(IMAGE_PATHS)
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  image_expanded = np.expand_dims(image_rgb, axis=0)
  input_tensor = tf.convert_to_tensor(image)
  input_tensor = input_tensor[tf.newaxis, ...]
  detections = detect_fn(input_tensor)
  num_detections = int(detections.pop('num_detections'))
  detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
  detections['num_detections'] = num_detections
  detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
  image_with_detections = image.copy()
  label, _=viz_utils.visualize_boxes_and_labels_on_image_array(
        image_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=MIN_CONF_THRESH,
        agnostic_mode=False)
  # print(label)
  print('Done')
  cv2.imshow('Object Detector', image_with_detections)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  return label
  
def numdet():
  frameWidth = 640    #Frame Width
  franeHeight = 480   # Frame Height
  plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
  minArea = 500
  path = 'images/8.jpg'
  count = 0
  img  = cv2.imread(path)
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)
  for (x, y, w, h) in numberPlates:
      area = w*h
      if area > minArea:
          cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
          cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
          imgRoi = img[y:y+h,x:x+w]
          # cv2.imshow("ROI",imgRoi)
  # cv2.imshow("Result",img)
  # if cv2.waitKey(1) & 0xFF ==ord('s'):
  cv2.imwrite("numberplate/images"+str(count)+".jpg",imgRoi)
def extract():
  pipeline = keras_ocr.pipeline.Pipeline()
  images = [
    keras_ocr.tools.read(img) for img in [
        'numberplate/images0.jpg'
    ]
  ]
  prediction_groups = pipeline.recognize(images)
  stri=str(prediction_groups)
  print(stri[4:13]) # if ap09a2132 then it is [4:13], elseif ap09ae2132 change this line to [4:14] fix this by using filtering i.e removing badchars
  plate_num=stri[4:13] #difference is firs tcase it is a in second one it is ae
  return plate_num
def getdet(regnum):
  mydb = myclient["mydb"]
  mycol = mydb["details"]
  stri=str(regnum)
  i=0
  for x in mycol.find({"regno": stri},{ "_id": 0,"regno": 1, "name": 1, "email":1 }):
      result=json.dumps(x)
  res = json.loads(result)
  name=res["name"]
  email=res["email"]
  print("Details of "+ regnum)
  print(name,email)
  return(name,email)
def putdet(regnum):
  mydb = myclient["mydb"]
  mycol = mydb["matter"]
  matter={"accident report vehicle":regnum}
  mycol.insert_one(matter)
def getcamdet(camerano):
  mydb = myclient["mydb"]
  mycol = mydb["camdetails"]
  cam=str(camerano)
  i=0
  for x in mycol.find({"camerano":cam},{ "_id": 0,"camerano": 1, "location": 1 }):
      result=json.dumps(x)
      res = json.loads(result)
      return res["location"]

def mail(name,email):
  now = datetime.now()
  time=str(now.strftime("%I:%M %p"))
  print(camerano)
  location=getcamdet(camerano)
  content = '\nHi there, your friend '+name+' has met with an accident at  '+time +', at loaction: '+location+"."
  username = "8888888888"
  password = "********"
  sender = "ADRS"
  recipient = str(email)
  mail = smtplib.SMTP("smtp.gmail.com",587)
  mail.ehlo() 
  mail.starttls() 
  mail.ehlo()
  mail.login(username,password)
  header = 'To:' + recipient + '\n' + 'From:' + sender + '\n' + 'Subject: Accident Report \n'
  content = header+content
  mail.sendmail(sender,recipient,content)
  mail.close

detector=detac()
print(detector)
if(detector=='accident'):
  numdet()
  number=extract()
  print(number)
  putdet(number)
  name,email=getdet(number)
  mail(name,email)
else:
  print("no accident has been detected")

