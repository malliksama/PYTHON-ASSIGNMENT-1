
# coding: utf-8

# In[1]:


#task 1.1
a='arjun'
a


# In[2]:


#task 1.2
number_list=[]
for r  in range (2000,3201):
    if r%7==0 and r%5!=0:
        number_list.append(r)
print(*number_list, sep= ',')


# In[3]:


#task 1.3
name=input("Enter your name : ")
surname=input("Enter your surname:   ")
print(surname[::-1],"",name[::-1])


# In[4]:


#task 1.4
pi=3.14
#radius (r) is half of the diameter
r=6
v=(4/3)*pi*r**3
print( "the volume of a sphere", v)


# In[5]:


numbers = input("Input some comma seprated numbers : ")
list = numbers.split(",")
print('List : ',list)


# In[6]:


#task 2.2
r=5;
for i in range(r):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(r,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[7]:


#task 2.3
a=input('what is your name')
print(a[::-1])


# In[8]:



#task 2.4
word="WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST,\n\t\t SECULAR, DEMOCRATIC REPUBLIC\n\t\t\t and to secure to all its citizens"
print(word)

