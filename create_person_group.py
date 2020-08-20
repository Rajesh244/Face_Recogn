import cognitive_face as CF
import sys
classid="IT2015"#sys.argv[1]
personGroupId=classid.lower()

Key = 'ec5f3015dee74f15a8c864ab1783b740'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)

#CF.person_group.delete('test05')
personGroups = CF.person_group.lists()
print(personGroups)
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print (personGroupId + " already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId)
print (res)
