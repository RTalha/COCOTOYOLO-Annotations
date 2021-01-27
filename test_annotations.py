import cv2
import os
pwd = os.getcwd()
f=open('persons_annotations.txt','r+')
for line in f:
    line = line.split()
    print(line[0])
    img = cv2.imread(os.path.join(pwd,line[0]))
    bboxes = line[1:]
    for box in bboxes:
        x1,y1,x2,y2,c=box.split(',')
        img=cv2.rectangle(img,(int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 3)
    cv2.imshow(line[0],img)
    key = cv2.waitKey(5000) & 0xFF

    if key == ord("q"):
        break
    cv2.destroyAllWindows() 
