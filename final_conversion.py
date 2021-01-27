import cv2
import glob
import os
import errno
def getshape(path):
    pwd=os.getcwd()
    img=cv2.imread(pwd+path[0:-3]+"jpg")
    if img is None:
        return -1,-1
    return img.shape[0:2]

def bboxYoloToCoco(x1,y1,x2,y2,string):
    height,width=getshape(string)
    if height==-1:
        return -1,-1,-1,-1
    x1,y1,x2,y2=float(x1),float(y1),float(x2),float(y2)
    x2=x2*width
    y2=y2*height
    x1=(x1*width)-(x2/2)
    y1=(y1*height)-(y2/2)
    return int(x1),int(y1),int(x1+x2),int(y1+y2)
    
def write_in_file(s,path):
    pwd=os.getcwd()
    file1 = open(pwd+path,"a+")#append mode 
    file1.write(s+"\n")
    file1.close() 



a=os.getcwd()
#annotations file path
path =a+ "/person-dataset/*.txt" 
print(path)
files = glob.glob(path)
concatination=""
string=""
for name in files:
    try:
        split=name.split("/")
        #images directory apth
        string="/person-dataset-images/"+split[-1]
        concatination+=string[0:-3]+"jpg"
        #concontination+=" "
        with open(name) as f:
            for line in f:
                if(line=="\n"):
                    break
                concatination+=" "
                data=line.split()
                if len(data)<=4:
                    continue
                class_id=data[0]
                x1=data[1]
                y1=data[2]
                x2=data[3]
                y2=data[4]
                x_min,y_min,x_max,y_max=bboxYoloToCoco(x1,y1,x2,y2,string)
                if x_min==-1:
                    continue
                concatination+=str(x_min)+","+str(y_min)+","+str(x_max)+","+str(y_max)+","+class_id
            #final yolo annotaion file path
            write_in_file(concatination,"/persons_annotations.txt")
            concatination=""
                
    except IOError as exc: #Not sure what error this is
        if exc.errno != errno.EISDIR:
            raise
