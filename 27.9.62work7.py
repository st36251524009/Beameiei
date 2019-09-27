#!/usr/bin/env python
# coding: utf-8

# In[17]:


#เขียนฟังก์ชัน printdouble(s) ที่รับรายการ s ของจำนวนเต็ม จากนั้นให้พิจารณาข้อมูลในรายการทีละตัวตามลำดับ แล้วพิมพ์ค่าข้อมูลแต่ละตัวนั้นคูณด้วย 2
n = int(input("Enter N: "))
k = int(input("Enter K: "))
for x in range(1,n+1):
   if  x%k == 0:
      print(x)


# In[ ]:




