#!/usr/bin/env python
# coding: utf-8

# In[2]:


#นาย ปรเมษฐ์  ไพโรจน์ 362515241009 EE36241N
user=input("Username :")
password=input("Password :")
if user=="beam" and password=="1010":
    print("Welcome to Icecream Shop.")
    print("----------Menu----------")
    print("Welcome to Icecream Shop")
    print("1. Strawberry 50 THB")
    print("2. Vanila        40 THB")
    print("3. Chocolate   30 THB")
    print("4. Lemon       20 THB")
    print("5. Milk           10 THB")
    s=80
    v=50
    c=40
    l=90
    m=10
    ice=int(input("What do you want?(1-5) : "))
    num=int(input("How many do you want? : "))
    if ice==1:
        print("You order ",num," of Strawberry ",s*num, " THB")
    elif ice==2:
        print("You order ",num," of Vanila ",v*num, " THB")
    elif ice==3:
        print("You order ",num," of Chocolate ",c*num, " THB")
    elif ice==4:
        print("You order ",num," of Lemon ",l*num, " THB")
    elif ice==5:
        print("You order ",num," of Milk ",m*num, " THB")
    
else :
    print("Error ,please try again.")

