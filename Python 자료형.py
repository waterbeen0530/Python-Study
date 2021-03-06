#!/usr/bin/env python
# coding: utf-8

# # 숫자형이란?
# 숫자형(number)이란 숫자 형태로 이루어진 자료형으로, 우리가 이미 잘 알고 있는 것이다.<br> 
# 우리가 흔히 사용하는 것을 생각해 보자.<br> 
# 123 같은 정수, 12.34 같은 실수, 드말게 사용하긴 하지만 8진수나 16진수 같은 것도 있다.
# > #### 파이썬 숫자 사용 예시<br>
# > - 정수 : 123, -123, 0<br>
# > - 실수 : 123.45, -1234.5, 3.4e10
# > - 8진수 : 0o34, 0o25
# > - 16진수 : 0x2A, 0xFF

# ## 숫자형은 어떻게 만들고 사용할까?
# 
# ### 정수형
# 정수형이란 말 그대로 정수를 뜻하는 자료형을 말한다.

# In[2]:


a = 123 # 양의 정수 대입
b = -178 #음의 정수 대입
c = 0 #0에 대입


# ### 실수형
# 파이썬에서 실수형은 소수점이 포함된 숫자를 말한다. 

# In[ ]:


# 일반적인 실수형 소숨점 표현 방식
a = 1.2
b = -3.45

#컴퓨터 지수 표현 방식
c = 4.24E10
d = 4.24e-10


# ### 8진수와 16진수
# - 8진수를 만들기 위해서는 숫자가 0o 또는 0O으로 시작하면 된다.<br>
# - 16진수를 만들기 위해서는 0x로 시작하면 된다.<br>
# - 8진수나 16진수는 파이썬에서 잘 사용하지 않는 형태의 숫자 자료형이다.

# In[ ]:


# 8진수
a = 0o177
# 16진수
b = 0x8ff
c = 0xABC


# ## 숫자형을 활용하기 위한 연산자
# 
# ### 사칙연산

# In[4]:


a = 3 
b = 4

num = a + b
print(num)

num = a - b
print(num)

num = a * b
print(num)

num = a / b
print(num)

#제곱을 나타내는 **연산자
num = a ** b
print(num)

# 나눗셈 후 나머지를 반환하는 % 연산자
num = a % b
print(num)

# 나눗셈 후 몫을 반환하는 // 연산자
num = a // b
print(num)


# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




