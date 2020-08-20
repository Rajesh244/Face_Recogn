import cognitive_face as CF
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

classid="IT2015"#sys.argv[1]
personGroupId=classid.lower()
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

Key = 'ec5f3015dee74f15a8c864ab1783b740'
CF.Key.set(Key)

res = CF.person_group.train(personGroupId)
print (res)
