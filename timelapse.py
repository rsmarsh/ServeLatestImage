from picamera import PiCamera
import time
import json

def updateJsonFile(image_name):
    jsonFile = open("stats.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()

    data["totalCaptures"] = image_count
    data["latestImage"] = image_path+image_name

    jsonFile = open("stats.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

image_path = 'captures/'
image_id = 0
image_count = 0
delay_between_captures = 3
camera = PiCamera()
# camera.rotation = 180

while True:
    image_id = image_id+1
    image_count = image_count+1

    image_name = 'IMG'+str(image_id)+'.jpg'
    camera.capture(image_path+image_name)
    
    print('img '+str(image_id)+ ' captured as '+str(image_name))
    updateJsonFile(image_name)
        
    time.sleep(delay_between_captures)
