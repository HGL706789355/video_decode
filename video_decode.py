#time:2022/2/4  12:40
#author:
#
import cv2
import os
import pdb
#需要手动新建一个badapple的文件夹
cap = cv2.VideoCapture('badapple.mp4')
image_dir = 'badapple'#文件夹名称
fps = cap.get(cv2.CAP_PROP_FPS)#获取视频帧率
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))#获取视频宽，高大小
fourcc = cv2.VideoWriter_fourcc(*'XVID')#mp4编码打开
i= 0#生成图片名称从0开始

while (cap.isOpened()):
    ret, frame = cap.read()# 读取视频帧，返回retval, image
    str1 = str(i)
    str2 = str1.zfill(6)
    image_name = os.path.join(image_dir + '/' + str2 + '.jpg')# 将目录和文件名合成一个路径
    print(image_name)
    if ret == True:
        cv2.imwrite(image_name, frame)#将图片写到路径
    else:
        break
    i = i + 1
cap.release()# 释放视频流
