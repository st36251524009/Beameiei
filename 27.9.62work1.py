#!/usr/bin/env python
# coding: utf-8

# In[4]:


#เขียนโปรแกรมรับจำนวนเต็มบวก 1 จำนวน จากนั้นให้แสดงผลลัพธ์เป็นจำนวนเต็มดังกล่าวที่เขียนอยู่ในรูปของตัวเลขฐาน สอง
x = int(input("Enter number: "))
x0 = x
sum = ''
d = 0
z = 0
while True:
   y = int(x%2)
   x = int(x/2)
   sum = str(y)+sum
   if y==1:
      z = z+2**d
   if z==x0:
      break
   d = d+1
z = int(sum)
print(z)

