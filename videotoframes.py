
# coding: utf-8

# In[1]:


import cv2 as c


# In[2]:


import cv2
vidcap = cv2.VideoCapture('SampleVideo_1280x720_1mb.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  count += 1

