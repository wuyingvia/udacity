
# coding: utf-8

# In[11]:


#read image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image=mpimg.imread('/home/wuying/A-udacity/lesson2/exit-ramp.jpg')
plt.imshow(image)


# In[12]:


#using opencv to transfer grayscale
import cv2
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray')


# In[38]:


kernel_size=5
blur_gray=cv2.GaussianBlur(gray,(kernel_size,kernel_size),0)
low_threshold=50
high_threshold=150
edges=cv2.Canny(blur_gray,low_threshold,high_threshold)
plt.imshow(edges,cmap='Greys_r')


# #define hough transform
# #params
# rho=1
# theta=np.pi/180
# threshold=1
# min_line_length = 10
# max_line_gap = 1
# line_image = np.copy(image)*0 #creating a blank to draw lines on
# 
# 

# In[47]:


#define hough transform
import numpy as np
#params 
rho=1 
theta=np.pi/180 
threshold=1 
min_line_length = 10 
max_line_gap = 1 
line_image = np.copy(image)*0 #creating a blank to draw lines on


#function
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on the blank
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)


# In[52]:


# Create a "color" binary image to combine with line image
#color_edges = np.dstack((edges, edges, edges)) 

# Draw the lines on the edge image
#combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
plt.imshow(combo)

