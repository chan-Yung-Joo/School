#!/usr/bin/env python
# coding: utf-8

# # 1. 변수의 개념

# In[227]:


# 변수 실습

# 숫자
a = 2020

print(a)


# In[228]:


# 텍스트
b = "삼성전자"


# In[229]:


print(b)


# In[230]:


type(b)


# In[231]:


# XML 형식 텍스트
c = "<note><to> Tove </to><from> Jani </from><heading> Reminder </heading><body> Don't forget me this weekend!</body></note>"


# In[232]:


type(c)


# In[233]:


import urllib
from PIL import Image


# In[234]:


urllib.request.urlretrieve("https://upload3.inven.co.kr/upload/2020/10/03/bbs/i13516850970.png","sample.png")


# In[235]:


img = Image.open("sample.png") # from ~ import 구문에 의해 PIL을 사용 불가
d = img


# In[236]:


import PIL


# In[237]:


img = PIL.Image.open("sample.png") # import 구문에 의해 PIL을 사용 가능
d = img


# In[238]:


type(d)


# In[239]:


d.show()


# ## 예약어 확인하기

# In[240]:


import keyword


# In[241]:


keyword.kwlist


# ## 변수의 연산

# In[242]:


a = 1


# In[243]:


b = 2


# In[244]:


a + b # 사칙연산이 가능하다!


# ### 변수는 개인의 고유 아이디를 갖음

# In[245]:


id(a)


# In[246]:


id(b)


# In[247]:


id(d) # 위에서 이미지 변수의 아이디 확인


# # 2. 수 다루기 (정수, 실수, 복소수)

# In[248]:


a = 23/7


# In[249]:


type(a)


# In[250]:


print(a)  # 소수점 15자리까지만 표현됨


# In[251]:


b = 2 + 3j  # a+bj -> a:실수부 , b: 허수부


# In[252]:


type(b)


# In[253]:


b.real # 실수부


# In[254]:


b.imag # 허수부


# ### 정수 연산

# In[255]:


a = 3
b = 2.5


# In[256]:


a*b


# In[257]:


a-b


# In[258]:


a+b


# In[259]:


# 나눗셈 연산
a/b


# In[260]:


# 몫 연산
a//b


# In[261]:


# 나머지 연산
a%b


# # 내장 수학 연산자 및 Math Module

# In[262]:


abs(-3) # 절댓값


# In[263]:


max(10,19,-1) # 최댓값


# In[264]:


min(10,19,-1) # 최솟값


# In[265]:


pow(2,4) # 지수 계산


# In[266]:


round(22.5) # 반올림 보단 버림에 가까운 개념


# In[267]:


round(22.54, 2) # 소숫점 2번째까지 표현하겠다는 의미


# ## 실습(1)

# In[268]:


a = list(range(0,101)) # 0부터 101전까지 수를 생성 후, 리스트로 저장


# In[269]:


print(a)


# In[270]:


max(a)


# In[271]:


min(a)


# ## 실습(2)

# In[272]:


a = 3/7 # a를 소숫점 2자리, 3자리까지 프린트 해봐라!


# In[273]:


round(a,2) # 소숫점 2자리까지


# In[274]:


round(a,3) # 소숫점 3자리까지


# ### 숫자값 print 하기 Tip!

# In[275]:


a = 31232/7
b = 3/8
c = 3/9


# In[276]:


print("a의 값은 ", round(a,2) , "이고 b의 값은 ", round(b,3), "이다.") # 흔히 사용하는 구문 -> 매우 불편


# In[277]:


# 편한 방법(1) -----> 이 방법이 더 많이 편함!
print("a의 값은 %.2f이고, b는 %.2f이고, c는 %.2f입니다."%(a,b,c))
# %.2f -> C언어에서 사용했던 Format 형식 지정 -> 소숫점 2자리까지 표현을 의미


# In[278]:


# 편한 방법(2)
print("a의 값은 {:.2f}이고, b는 {:.2f} 이고, c는 {:.3f} 입니다.".format(a,b,c))


# ## 실습(2)

# ### 아래의 변수들을 %.xf 키워드를 사용해서 한줄로 print 하시오!

# In[279]:


a1 = 3.14195 # 소숫점 5자리까지 표시
a2 = 3.14195 # 소숫점 3자리까지 표시
a3 = 3.14195 # 소숫점 2자리까지 표시
a4 = 3.14195 # 소숫점 1자리까지 표시
a5 = 3.14195 # 정수 표시


# In[280]:


print("a1: %.5f , a2: %.3f, a3: %.2f, a4: %.1f, a5: %d"%(a1,a2,a3,a4,a5))


# ### Math 모듈 다루기

# #### 모듈?
# #### 파이썬 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것.

# In[281]:


import math


# In[282]:


math.pi


# In[283]:


math.e


# ###  Math 모듈 계산 실습

# In[284]:


math.fabs(-5) # 절댓값


# In[285]:


math.ceil(-4.12) # 가까운 정수 올림


# In[286]:


math.floor(4.1) # 가까운 정수에서 버림


# In[287]:


math.exp(1) # e^1의 값


# In[288]:


math.sin(0) # sin(0)의 값


# In[289]:


math.cos(0) # cos(0)의 값


# In[290]:


math.tan(0) # tan(0)의 값


# In[291]:


math.sqrt(4) # 루트 4의 값


# In[292]:


math.log(4,2) # log(지수, 밑)


# In[293]:


math.factorial(1)


# In[294]:


math.factorial(5)


# In[295]:


math.factorial(10)


# In[296]:


math.factorial(100)


# # 4. 논리 연산자

# In[297]:


a = True
b = False


# In[298]:


a,b


# In[299]:


type(a)
type(b)


# In[300]:


a and b


# In[301]:


a or b


# In[302]:


not(a)


# In[303]:


not(b)


# # 5. 텍스트 다루기

# In[304]:


a = "Hello World"


# In[305]:


a[0]


# In[306]:


a[1]


# In[307]:


a[5] # 띄어쓰기도 하나의 문자로 생각함


# In[308]:


a[10]


# ##### a[11]의 경우는 범위 밖의 인덱스 이므로 에러 발생!

# ### 문자열 합치기도 가능

# In[309]:


a = "삼성" + "전자"


# In[310]:


a[0:3] # ----> Slicing(슬라이싱)


# In[311]:


a[:2] # 처음부터 인덱스 2까지


# In[312]:


a[2:] # 2부터 인덱스 끝까지


# ### 문자열이 있는지 확인하는 방법?

# In[313]:


"삼성" in a


# In[314]:


"성화" in a


# ### 문자열의 길이는 어떻게 확인할까?

# In[315]:


a = "hello world"


# In[316]:


len(a)


# ### 반복 출력도 가능하다!

# In[317]:


b = a*3


# In[318]:


len(b)


# ### 인덱싱의 추가 부분

# In[319]:


a = "삼성" + "전자"


# In[320]:


a[-1] # 마이너스는 뒤에서부터 인덱싱함!


# ### 문자열을 구분자를 사용해서 출력하기

# In[321]:


print("삼성","전자")


# In[322]:


print("삼성", "전자", sep=',') # sep의 default는 띄어쓰기임


# In[323]:


print("삼성", "전자", sep='>>>')


# ### 텍스트 입력(Input) 받아서 출력(Output)하기

# In[378]:


a = input("너의 이름은?")


# In[379]:


a


# In[380]:


type(a) # input 함수의 데이터 타입은 기본적으로 문자열임


# In[381]:


b = input("당신의 키는?")


# In[382]:


b


# In[383]:


type(b) # input 함수의 데이터 타입은 기본적으로 문자열임


# In[384]:


b = float(b) # 형변환도 가능함을 의미


# In[385]:


type(b)


# In[386]:


print("당신의 이름은 %s 이고, 당신의 키는 %.1f 입니다."%(a,float(b)))


# ## 실습(3)

# ### 자신의 이름과 소속, 핸드폰 번호를 입력 받아 출력합니다.

# ### 단, 핸드폰 번호는 모두 입력 받고, 앞 7자리만 출력하고 뒤의 4자리는 *로 표시

# In[387]:


name = input("너의 이름은?")


# In[388]:


depart = input("너의 소속은?")


# In[389]:


phone = input('너의 번호는?')


# In[392]:


print("당신의 이름은 %s 이고, %s 에 속하고, 당신의 번호는 %s-****입니다."%(name,depart,phone[:8]))


# # 6. 문자열 다루기

# In[393]:


a = "Hello world"


# ### 6.1 startswith( ) Method

# In[394]:


a.startswith("He")


# In[395]:


a.startswith("IO")


# ### 6.2 endswith( ) Method

# In[396]:


a.endswith("He")


# In[397]:


a.endswith("ld")


# In[398]:


b = "Hello world "


# In[399]:


b.endswith(' ')


# In[400]:


b.endswith('d')


# ### 6.3 find( ) Method

# In[401]:


a.find(' ') # 해당 문자 위치의 인덱스를 출력함


# In[402]:


a.find('+') # 해당 문자가 없으면 -1을 출력


# ### 6.4 rfind( ) Method

# In[403]:


a.rfind('H')


# In[404]:


a.rfind('w')


# ### 6.5 count( ) Method

# In[405]:


a.count(' ') # 해당 문자의 개수를 출력


# In[406]:


a.count('l') # 해당 문자의 개수를 출력


# ### 6.6 lstrip( ) Method

# In[407]:


c = "    LeftStrip!"


# In[408]:


c.lstrip()  # 왼쪽의 공백을 제거


# ### 6.7 rstrip( ) Method

# In[409]:


d = "Right Strip       "


# In[410]:


d.rstrip() # 오른쪽의 공백을 제거


# ### 6.8 strip( ) Method

# In[411]:


h = "      Strip       "


# In[412]:


h.strip() # 양쪽의 공백을 제거


# ### 6.9 isalpha( ) Method

# In[413]:


a = 'hello world'


# In[414]:


a.isalpha() # 공백도 인식하기 때문에 False가 출력


# ### 6.10 isnumeric( ) Method

# In[415]:


a = '12345678'


# In[416]:


a.isnumeric() # 숫자로만 이루어져 있는지를 확인


# ### 6.11 isalnum( ) Method

# In[417]:


a = '123456abcde'


# In[418]:


a.isalnum() # 숫자와 알파벳으로만 이루어져 있는지를 확인


# ### 6.12 replace( ) Method

# In[419]:


a = 'hello world'


# In[420]:


a.replace(' ', ',') # replace(a, b) -> a를 b로 변경한다!


# ### 6.13 split( ) Method

# In[421]:


a = 'hello world'


# In[422]:


a.split(' ') # 공백을 기준으로 나누겠다!


# In[423]:


a = 'hello Python World'


# In[424]:


b = a.split(' ') # 공백을 기준으로 나누겠다!


# In[425]:


type(b) # 기준으로 나눈 문자들은 List 형태로 저장이 됨을 알고 있을 것.


# ### 6.14 upper( ) Method

# In[426]:


a = 'lower case'


# In[427]:


a.upper() # 해당 문자열을 모두 대문자로 변경함


# ### 6.15 lower( ) Method

# In[428]:


a = 'UPPER CASE'


# In[429]:


a.lower() # 해당 문자열을 모두 소문자로 변경함


# ### 6.16 format( ) Method

# In[430]:


a = 'My name is {name}. I am {age} years old'


# In[431]:


a.format(name="주찬영", age=21) # print() 함수에서 format을 지정해주는것과 동일함

