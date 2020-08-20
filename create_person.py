import sys,os
import cognitive_face as CF
import sqlite3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


classid=sys.argv[1]
personGroupId=classid.lower()
Key = 'ec5f3015dee74f15a8c864ab1783b740'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)


if len(sys.argv) is not 1:
    res = CF.person.create(personGroupId, str(sys.argv[1]))
    print(res)
    print(sys.argv)
    extractId = str(sys.argv[2])
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM "+classid+ " WHERE ROLL = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE "+classid+" SET personID = ? WHERE ROLL = ?",(res['personId'], extractId))
    connect.commit()                                                            # commiting into the database
    connect.close()
    print ("Person ID successfully added to the database")
    os.system("python add_person_faces.py "+classid+" "+extractId)