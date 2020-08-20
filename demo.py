import os,shutil,sys
classid="IT2015"#sys.argv[1]
croppedFol = 'F:\Autoattendance-Cognitive-master-Copy\Cropped_faces'
if os.path.exists(croppedFol):
    shutil.rmtree(croppedFol)
os.makedirs(croppedFol)
os.system("python train.py " + classid.lower())
os.system("python detect.py "+classid)
os.system("python spreadsheet.py "+classid)
os.system("python identify.py " + classid)
