#!/usr/bin/env python
# coding: utf-8

# In[5]:


H = input('請輸入您的身高(公尺):')
W = input('請輸入您的體重(公斤):')
H = float(H)
W = float(W)
BMI = W / H**2
if BMI < 18.5:
    print('過瘦')
elif BMI >= 18 and BMI < 24:
    print('正常')
elif BMI >= 24 and BMI < 27:
    print('過重')
elif BMI >= 27 and BMI < 30:
    print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
    print('中度肥胖')
else: 
    print('重度肥胖')

