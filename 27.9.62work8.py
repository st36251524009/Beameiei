#!/usr/bin/env python
# coding: utf-8

# In[18]:


#ให้เขียนโปรแกรมรับจำนวนเต็มระหว่าง 0 ถึง 9 จากนั้นแสดงแผนภาพฮิสโตแกรมที่แสดงความถี่ของข้อมูลแต่ละตัวที่ได้รับมา 
x = int(input())
n =[[],[],[],[],[],[],[],[],[],[]]
while x >=0 :
    if x == 0:
        n[0].append('*')
    elif x == 1:
        n[1].append('*')
    elif x == 2:
        n[2].append('*')
    elif x == 3:
        n[3].append('*')
    elif x == 4:
        n[4].append('*')
    elif x == 5:
        n[5].append('*')
    elif x == 6:
        n[6].append('*')
    elif x == 7:
        n[7].append('*')
    elif x == 8:
        n[8].append('*')
    elif x == 9:
        n[9].append('*')
    x = int(input())
for i in range(10):
    sum = ''
    for y in n[i]:
        sum = sum+y
    print(i,":",sum)


# In[ ]:




