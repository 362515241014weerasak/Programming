#!/usr/bin/env python
# coding: utf-8

# In[21]:


#นาย วีระศักดิ์ วงษ์ภู่งาม 362515241014 EE36241N
username = input("username")
password = input("password")
if username == "EE36241N" and password == "14":
    print("Welcome to xyz Shop")
    print("-----------Menu-----------")
    print("1. Lay 20 THB")
    print("2. Ichitan 20 THB")
    print("3. Sausage 10 THB")
    print("4. Pen 7 THB")
    print("5. Water 10 THB")
    print("--------------------------")
    ch= int(input("What do you want :"))
    if ch==1:
        price=20
        print("Your order :", "Lay", "20 THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==2:
        price=20
        print("Your order :", "Ichitan", "20THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==3:
        price=10
        print("Your order :", "Sausage", "10 THB") 
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==4:
        price=7
        print("Your order :", "Pen", "7 THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    elif ch==5:
        price=10
        print("Your order :", "Water", "10 THB")
        How=int(input("How many do you need :"))
        print( "Total :",How*price, "THB")
    else:
        print("You not order")    
else:
    print("You not member")
print("Thank you")


# In[ ]:





# In[ ]:




