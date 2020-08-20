import os
import time,datetime
classid=["IT2015"]
time_period=['0829','0945','1044','1141','1210','1440','2235']
d=datetime.datetime.now()
current_time=d.strftime("%H%M")
current_second=d.strftime("%S")
for y in classid:
        os.system("python spreadsheet.py "+y)
for x in time_period:
    #print(x+'  '+current_time)
    if x==current_time:
        for y in classid:
            for i in range(1):
                os.system("python detect.py "+y)
            time.sleep(6)
        for y in classid:
            os.system("python train.py " + y)
            os.system("python identify.py "+y)
    elif x>current_time:
        while(x!=current_time and current_time<'1500' and current_time>'0800'):
            if(current_second!='00'):
                print(current_second)
                pause=60-int(current_second)
                print(pause)
                current_second=d.strftime("%S")
                time.sleep(pause)
                d=datetime.datetime.now()
                current_second=d.strftime("%S")
                current_time=d.strftime("%H%M")
                if(x==current_time):
                    for y in classid:
                        for i in range(1):
                            os.system("python detect.py "+y)
                            time.sleep(6)
                    for y in classid:
                        os.system("python train.py " + y)
                        os.system("python identify.py "+y)
                    break
                time.sleep(60)
                d=datetime.datetime.now()
                current_time=d.strftime("%H%M")
        #print(current_time)

            
