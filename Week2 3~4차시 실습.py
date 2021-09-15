#!/usr/bin/env python
# coding: utf-8

# # 1. if 조건문

# ### 예제1)

# In[1]:


age = 19

if age < 20:
    print("청소년 할인")

print("입장을 환영합니다.")


# In[2]:


age = 40

if age < 20:
    print("청소년 할인")

print("입장을 환영합니다.")


# ### 예제2)

# In[3]:


a = 6
b = 5

if (a%2 == 0) and (b%2 == 0):   # a와 b 둘다 짝수인가?
    print("두 수가 모두 짝수!")
    
if (a%2 == 0) or (b%2 == 0):    # a와 b 중 하나만 짝수인가?
    print("두 수 중 하나 이상이 짝수!")


# ### 예제3) 시험 성적 판별

# In[7]:


score = int(input("점수를 입력하세요 : ")) 
# input 함수는 입력을 문자열로 받기 때문에 형변환!

if score >= 90:
    grade = 'A'

if score < 90 and score >= 80:
    grade = 'B'

if score < 80 and score >= 70:
    grade = 'C'
    
if score < 70 and score >= 60:
    grade = 'D'

if score < 60:
    grade = 'F'

print("당신의 등급은 : %s"%(grade))


# ### 예제4) 예제3의 개선 Version

# In[9]:


score = int(input("점수를 입력하세요 : "))

if score >= 90:
    grade = 'A'

else: # 위의 조건을 만족하지 않을 때!
    
    if score >= 80:
        grade = 'B'
    
    else:
    
        if score >= 70:
            grade = 'C'
    
        else:
        
            if score >= 60:
                grade = 'D'
        
            else:
                grade = 'F'

print("당신의 등급은 : %s"%(grade))


# ### 예제5) 예제4의 더 개선된 Version ---> 가독성이 더 좋은 것!

# In[10]:


score = int(input("점수를 입력하세요 : "))

if score >= 90:
    grade = 'A'

elif score >= 80:
    grade = 'B'

elif score >= 70:
    grade = 'C'

elif score >= 60:
    grade = 'D'

else:
    grade = 'F'

print("당신의 등급은 : %s"%(grade))


# # 2. for 반복문

# ### 예제1)

# In[11]:


for i in range(5):
    print("갤럭시 노트 40 출시!")


# #### range(a, b, c) ----> a: 시작값, b: 종료 값(반환X) , c: 간격 

# ### 예제2)

# In[12]:


for i in range(40, 51, 1):
    print("갤럭시 노트 {:d}출시!!".format(i))


# ### 예제3) 음수 값 간격은 어떻게?

# In[13]:


for i in range(-2, -10, -1):
    print("갤럭시 노트 {:d}출시!!".format(i))


# ### 실습하기!

# ### 팩토리얼(Fatorial) 계산하기 ------> 강의자료 Page 38

# In[ ]:





# ### 예제4) 중첩 For 문 --- 구구단

# In[19]:


for i in range(2, 10):   # i의 범위는 2부터 10전까지(9까지) 1간격으로!
    for j in range(1, 10): # j의 범위는 1부터 10 전까지(9까지) 1간격으로!
        
        print("{:d} * {:d} = {:d}".format(i, j, i*j))
        
    print() # 단이 바뀔 때, 한 칸 띄어 주기 위함! (가독성 높이기)


# ## for문과 리스트

# ### 예제5)

# In[20]:


for i in [0, 3, 10, 11]:
    print(i)


# In[21]:


for i in [0, 3, 10, 'a']:
    print(i)


# ### 예제6-1) 정수형 리스트의 객체 순회

# In[22]:


numbers = [11, 22, 33, 44, 55, 66]

for n in numbers:
    print(n, end = ' ')


# ### 예제 6-2) 실수형 리스트의 객체 순회

# In[24]:


f_numbers = [1.1, 2.5, 3.7, 5.6, 9.2, 11.3, 6.8]

for f in f_numbers:
    print(f, end = '/')


# ### 예제 6-3) 문자열 리스트의 객체 순회

# In[25]:


summer_fruits = ['수박', '참외', '체리', '포도']

for fruit in summer_fruits:
    print(fruit, end = ' ')


# In[ ]:




