# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:09:37 2021

@author: hp
"""
import cv2
#import bellman_ford2
#bellman_ford2.singal_get_path()
def route_print(w,img): 
    '''
    print('请输入节点个数：')
   
    k=int(input())         
       #路线打印
    for i in range(int(k-1)):
        print('请输入')
        a=int(input())
        b=int(input())
        c=int(input())
        d=int(input())
    '''
    a=0
    
    #j=(513, 133)
    for i in range(len(w)):
        if a==len(w)-1:
            break
        #print("起点{}，终点{}".format(w[i],w[i+1]))
        a=a+1
        cv2.line(img, w[i],w[i+1],(0, 255, 0),15)
    '''
    cv2.line(img,(1778, 2446),(1908,2437), (0, 255, 0),3)
  #  cv2.line(img,(801, 322),(833, 377), (0, 255, 0),3)
  #  cv2.line(img,(833, 377),(863, 379), (0, 255, 0),3)
  #  cv2.line(img,(863, 379),(1030, 382), (0, 255, 0),3)
   # cv2.line(img,(503, 739),(1104, 165), (0, 255, 0),3)
   '''
if __name__=='__main__':
    img = cv2.imread('./bistu.jpg')      
   # img=cv2.resize(img,((1316,903)),interpolation=cv2.INTER_LINEAR)
    '''
    coordinate={ 
            0: (160, 151),
            1: (513, 133), 
            2: (746, 123), 
            3: (863, 121), 
            4: (1021, 117), 
            5: (1069, 382), 
            6: (1030, 382), 
            7: (863, 379), 
            8: (833, 377), 
            9: (801, 322), 
            10: (753, 291), 
            11: (564, 290), 
            12: (452, 405), 
            13: (389, 410), 
            14: (296, 413), 
            15: (456, 714), 
            16: (790, 749), 
            17: (1218, 768),
            18: (522, 168),
            19: (750, 155),
            20:(860, 151),
            21:(861, 280),
            22:(1011, 281),
            23:(508, 410),
            24:(836, 412),
            25:(840, 472),
            26:(826, 515),
            27:(507, 495),
            28:(513, 515),
            29:(551, 590),
            30:(802, 590),
            31:(976, 519),
            32:(975, 592),
            33:(560, 628),
            34:(561, 674),
            35:(792, 642),
            36:(791, 691),
            37:(390, 509),
            38:(482, 669),
            39:(977, 704),
            40:(1077, 519),
            41:(1152, 717),
            42:(385, 293),
            43:(550, 259),
            44:(505, 451)
    }
    #print(coordinate[1])
    m=[0,18,43,11,12,44]
    w=[]
    for i in range(len(m)):
        if m[i] in coordinate:
            w.append(coordinate[m[i]])
    print(w)    
    '''
    route_print(w,img)
    
    cv2.namedWindow("image")
    #cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.imwrite("./test.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  
      