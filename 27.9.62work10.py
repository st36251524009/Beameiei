#!/usr/bin/env python
# coding: utf-8

# In[21]:


#ให้เขียนรับตัวเลขฐาน 2 จากผู้ใช้ จากนั้นแปลงให้เป็นเลขฐานสิบ
x = input("Enter binary number: ")
d = len(x)-1
sum = 0
for y in x:
   if y == '1':
      sum = sum+2**d
   d = d-1
print(sum)


# In[ ]:




