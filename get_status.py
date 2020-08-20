import cognitive_face as CF
import sys
classid=sys.argv[1]
personGroupId=classid.lower()

Key = '385ea9eb10ec4d5daf823ad62780fa6e'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.get_status(personGroupId)
print (res)
