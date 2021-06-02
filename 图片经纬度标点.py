# coding: utf-8
import cv2
import math
# 图片路径
img = cv2.imread('./bistu.jpg')
a = []
b = []

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       # xy = "%d,%d" % (x, y)
        xy='105'
        a.append(x)
        b.append(y)
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img,xy,(x, y), cv2.FONT_HERSHEY_PLAIN,1.0, (0, 0, 0), thickness=1)
        for i in range(event):
            print(x,y)
    cv2.imshow("image", img)
'''
def route_print():                 #路线打印
    cv2.line(img, (1038, 111), (1067, 379),(0, 255, 0),3)
    cv2.line(img,(1067, 379),(1201, 741), (0, 255, 0),3)
    cv2.line(img,(1201, 741),(1213, 767), (0, 255, 0),3)
    cv2.line(img,(1213, 767),(829, 754), (0, 255, 0),3)
    cv2.line(img,(829, 754),(503, 739), (0, 255, 0),3)
    cv2.line(img,(503, 739),(268, 390), (0, 255, 0),3)
      #  print(x,y)
'''
# (1084,744)
#img=cv2.resize(img,((1316,903)),interpolation=cv2.INTER_LINEAR) 
print(img.shape)
cv2.namedWindow("image")

cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
#route_print()
cv2.waitKey(0)
cv2.imwrite("./architecture.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  

#print(a)
#print(b)
print()
k={}
for i in range(len(a)):         #坐标字典
    k[i]=(a[i],b[i])


for i in k.keys():
    print(i,':',k[i])   

k={}
for i in range(len(a)):
    k[i]=(a[i],b[i])
print('k:',k)

c=[]
for i in range(len(a)):
    c.append(a[i]-a[i-1])
print(c)
d=[]
for i in range(len(a)):
    d.append(b[i]-b[i-1])
print(d)
for i in range(len(a)):
    print(math.sqrt(c[i]*c[i]+d[i]*d[i]))
