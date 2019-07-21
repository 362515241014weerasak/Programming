#!/usr/bin/env python
# coding: utf-8

# In[2]:


#นาย วีระศักดิ์ วงษ์ภู่งาม 362515241014 EE36241N
print("--------Menu--------")
print("Welcome to Icecream Shop")
print("1. Strawberry  80 THB")
print("2. Vanila      50 THB")
print("3. Chocalate   40 THB")
print("4. Lemon       90 THB")
print("5. Milk        10 THB")
ch=int(input("What do you want?"))
if ch== 1:
    price=80
    print("Your order :", ch, "Strawberry ", price, "THB")
elif ch== 2:
    price=50
    print("Your order :", ch, "Vanila ", price, "THB")
elif ch== 3:
    price=40
    print("Your order :", ch, "Chocalate ", price, "THB")
elif ch==4:
    price=90
    print("Your order :", ch, "Lemon ", price, "THB")
elif ch==5:
    price=10
    print("Your order :", ch, "Milk ", price, "THB")
else:
    print("You not order:")


# In[ ]:




