#!/usr/bin/env python
# coding: utf-8

# In[11]:


#ร้านขายหนังสือร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อหนังสือมากกว่า 3 เล่ม ที่มีมูลค่ารวมเกิน 500 บาท คุณจะได้ส่วนลด 10% 
count = int(input("How many books: "))
money = int(input("How much: "))
if count > 3 and money > 500:
    s = money-money*0.1
else:
    s = money
print("You have to pay",int(s),"bath.")


# In[ ]:




