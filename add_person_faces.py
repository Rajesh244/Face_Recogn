import sys
import os, time
import cognitive_face as CF
import urllib
import sqlite3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


classid=sys.argv[1]
personGroupId=classid.lower()
Key = 'ec5f3015dee74f15a8c864ab1783b740'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)


def get_person_id():
	person_id = ''
	extractId = str(sys.argv[2])
	connect = sqlite3.connect("Face-DataBase")
	c = connect.cursor()
	cmd = "SELECT * FROM "+classid+" WHERE ROLL = " + extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	connect.close()
	return person_id

if len(sys.argv) is not 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/"+classid+"/" + str(sys.argv[2])+"/")
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
        	print(filename)
        	imgurl = urllib.request.pathname2url(os.path.join(imageFolder, filename))
        	res = CF.face.detect(imgurl[3:])
        	if len(res)!=1:
        		print("No face detected in the image")
        	else:
        		res = CF.person.add_face(imgurl[3:], personGroupId, person_id)
        		print(res)	
        	time.sleep(6)
