'''
# 1
print("Hello World")
# 2
print("Mary's cosmetics")
# 3
print('신씨가 소리질렀다. "도둑이야".')
# 4
print("C:\Windows")
# 5
print("안녕하세요.\n만나서\t\t반갑습니다.") # \n은 줄바굼, \t\t 한칸 띄어쓰기(총두칸)
# 6
print("오늘은", "일요일") # '오늘은' 띄우고 '일요일'
# 7
print('naver'+';'+'kakao'+';'+'sk'+';'+'samsung')
print("naver", "kakao", "sk", "samsung", sep=";") # sep 인자로 출력값 사이에 공백대신 ; 넣기
# 8
print("naver", "kakao", "sk", "samsung", sep="/")
# 9
print("first", end=""); print("second")
# 10
print(5/3)
# 11
삼성전자 = "50000"
총평가금액 = 삼성전자 * 10
print(총평가금액)
# 12
시가총액 = 29800000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
# 13
s = "hello"
t = "python"
print(s+"!", t)  # hello 뒤에 ! 붙이고 띄워쓰기 후 python 붙이기
# 14
print(2+2*3)
# 15
a = "132"
print(type(a))
# 16
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))   # int 는 정수형
# 17
num = 100
result = str(num)
print(result,type(result))  # str은 문자열
# 18
a = "15.79"
a = float(a)
print(a,type(a))
# 19
year = "2020"
num_int = int(year)
print(num_int-1,num_int,num_int+1)

year = "2020"
print(int(year)-3)
print(int(year)-2)
print(int(year)-1)
# 20
air = 48584 * 36
print(air)
# 21
letters = 'python'
print(letters[0],letters[2])
# 22
plate = "24가 2210"
print(plate[4:])
# 23
string = "홀짝홀짝홀짝"
print(f'{string[0]}{string[2]}{string[-2]}')

string = "홀짝홀짝홀짝"
print(string[::2])
# 24
string = "PYTHON"
print(string[::-1])
# 25
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")  # 변경하고 싶은 문자 .replace(변경하고싶은 문자, 변경할 문자)
print(phone_number1)
# 26
phone_number1 = phone_number.replace("-", "")
print(phone_number1)
# 27
url = "http://sharebook.kr"
print(url[-2:])

url_split = url.split(".")
print(url_split[-1])  # split (괄호 안) 기준으로 분리하는 걸 뜻함
# # 28
# lang = 'python'
# lang[0] = 'P'
# print(lang) #Python
# 29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)
# 30
string = 'abcd'
string.replace('b', 'B')
print(string)  # abcd
# 31
a = "3"
b = "4"
print(a + b)   #  7 이 아니고 a, b 문자 붙이기 >> 34
# 32
print("Hi" * 3) # HiHiHi
# 33
print("-" * 80)
# 34
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
# 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))  # % formatting 에서 %s 는 문자열을 %d 는 데이터 값을 출력
# 36
print("이름: {} 나이:{}" .format(name1, age1))
print("이름: {} 나이:{}" .format(name2, age2))  # 출력될 위치에 {} 넣어주고 .format해서 끌어올 데이터 체크
# 37
print(f"이름: {name1} 나이:{age1}")
print(f"이름: {name2} 나이:{age2}") # f-string는 문자열 앞에 f 붙은 형태
# 38
상장주식수 = "5,969,782,550"
상장주식수1 = 상장주식수.replace(",","")
상장주식수1 = int(상장주식수1)
print(상장주식수1,type(상장주식수1))
# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
# 40
data = "  삼성전자  "
data1 = data.strip()
print(data1)
# 41
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
# 42
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)
# 43
a = "hello"
a1 = a.capitalize()
print(a1)
# 44
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
# 45
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))
# 46
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
# 47
a = "hello world"
a.split()  # split()는 문자열의 공백 기준으로 분리
# 48
ticker = "btc_krw"
ticker.split("_")
# 49
date = "2020-05-01"
date.split("-")
# 50
date = "039490       "
data = date.rstrip()
print(data)
# 51
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
# 52
movie_rank.append("배트맨")
print(movie_rank)    # .append  리스트 안에 추가할 때 사용
# 53
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)   # 괄호 앞 자리에 리스트 추가
# 54
del movie_rank[3]
print(movie_rank)
# 55
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
# 57
nums = [1, 2, 3, 4, 5, 6, 7]
print("max:", max(nums))
print("min:", min(nums))
# 58
nums = [1, 2, 3, 4, 5]
print(sum(nums))
# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))  # len : 데이터 갯수 새기
# 60
nums = [1, 2, 3, 4, 5]
print(sum(nums)/5)

average = sum(nums) / len(nums)
print(average)
# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
# 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
# 65
interest = ['삼성전지', 'LG전자', 'Naver']
print(interest[0], interest[2])
# 66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest)) # 66 번 물어보기!!
# 67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
# 68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest)) # \n은 한줄 띄우기
# 69
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)
# 70
data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)
print(data2)  # sorted는 오름차순
# 71
my_variable = ()
print(type(my_variable))  # type는 잘 만들어졌는지 확인하겠다.
# 72
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
# 73
tuple = (1, )
print(type(tuple))
# 74
t = (1, 2, 3)
 # tuple은 원소(element) 값을 변경할 수 없다.
# 75
t = 1, 2, 3, 4
print(t)   # 정수
# 76
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t) # 튜플은 데이터 변경 불가, 새로 업데이트 시 기존 튜플 삭제
# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)

data = list(interest)
print(data)
# 78  # # 리스트를 튜플로 변경
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = ()
# data = tuple(interest)
print(type(interest))
# 79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)   # apple, banana, cake 나옴
# 80  # 튜플 range

# 81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores  #  뒤에 ,_,_는 총 10개 중 2개를 빼기
print(valid_score)
# 82
_, _, *valid_score = scores
print(valid_score)
# 83
a, *valid_score, b = scores
print(valid_score)
# 84
temp = {}  #  딕셔너리는 {} 로 함
print(temp)
# 85
ice = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(ice)
# 86
ice['죠스바'] = 1200
ice['월드콘'] = 1500
print(ice)
# 87
print("메로나 가격: ", ice["메로나"])
# 88
ice["메로나"] = 1300
print(ice)
# 89
del ice["메로나"]
print(ice)
# 90
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']   # 에러 : 딕셔너리에 없는 키 사용
# 91
inventory = {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
print(inventory)
# 92
print(inventory['메로나'][0], '원')
# 93
print(inventory['메로나'][1], '개')
# 94
inventory['월드콘'] = [500, 7]
print(inventory)
# 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream))

ice = list(icecream.keys())
print(ice)
# 96
ice = list(icecream.values())
print(ice)
# 97
price = sum(icecream.values())
print(price)
# 98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)  # 딕셔너리는 업데이트 해야한다.
# 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(data, close_price))
print(close_table)
# 101 # bool 타입
# 102
print(3 == 5)  # False
# 103
print(3 < 5)  # True
# 104
x = 4
print(1 < x < 5)  # True
# 105
print((3 == 3) and (4 != 3))  #True
# 106
print(3 >= 4) # => 가 아닌 >= 여야함 (지원하지 않는 연산자)
# 107
if 4 < 3:
    print("Hello World")  #  False
# 108
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")   #  Hi, there.
# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")   # 1, 2, 4
# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")   # 3, 5
# 111
user = input("입력:")
print(user * 2)
# 112
user = input("숫자를 입력하세요:")
print(10 + int(user))
# 113
a = input("")
if int(a) % 2 == 0:
    print("짝수")    # int() 는 실수 또는 정수를 집어넣는다 라는 표현
else:
    print("홀수")
# 114
user = input("입력값:")
i = 20 + int(user)
if i > 255:
    print(255)
else:
    print(i)
# 115
user = input("입력값:")
a = int(user) - 20
if a > 255:
    print(255)
elif a < 0:
    print(0)
else:
    print(a)
# 116   # 아무리 생각해도 모르겠다. 주의
time = input("현재시간:")
if time[-2:] == "00":   
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")
# 117
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("종목명: ")
if user in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가좋아하는계절은: ")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")  
# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가좋아하는과일은: ")
if user in fruit.values():   # values 는 : 뒤에 있는 딕셔너리 값. 
    print("정답입니다.") 
else:
    print("오답입니다.")
# 121
user = input("문자 입력")
if user.islower():
    print(user.upper())
else:
    print(user.lower())
# 122
user = int(input("score:"))
if user >= 81:
    print("grade is A")
elif user >= 61:
    print("grade is B")
elif user >= 41:
    print("grade is C")
elif user >= 21:
    print("grade is D")
else:
    print("grade is E")
# 123  # 몰라서 답 확인
환율 = {"달러" : 1167,
        "엔" : 1.096,
        "유로" : 1268,
        "위안" : 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")
# 124  # 답 확인
num1 = input("input number1:")
num2 = input("input number2:")
num3 = input("input number3:")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)
# 125  # 답확인
number = input("휴대전화 번호 입력:")
num = number.split("-")[0]  # .split("-") 는 - 를 중점으로 문자열 나눔
if num == "011":
    com = "SKT"
elif num == "016":
    com = "KT"
elif num == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")
--
number = input("휴대전화 번호 입력:")
if number[:3] == "011":
    com = "SKT"
elif number[:3] == "016":
    com = "KT"
elif number[:3] == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")  # 왜 틀린거?
# 126
우편번호 = input("우편번호:")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
# 127
주민등록번호 = input("주민등록번호: ")
주민등록번호 = 주민등록번호[7]
if 주민등록번호 == "1" or 주민등록번호 == "3":
    print("남자")
else:
    print("여자")
--
주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
else:
    print("여자")
# 128
ResNum = input("주민등록번호: ")
ResNum = ResNum.split("-")[1]
# print(type(ResNum[1:3]))
a = int(ResNum[1:3])
if a <= 8:
    print("서울 입니다.")
else:
    print("서울이 아닙니다.")
--
주민번호 = input("주민등록번호: ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")
# 129
num = input("주민등록번호: ")
first = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
second = 11 - (first % 11)
third = str(second)

if num[-1] == third[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])   # float 를 이용하여 숫자나 문자를 실수형으로 바꿀 수 있다
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
'''
# 131
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)   # 사과  \ 귤 \ 수박
# 132 # 주의
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")    # for문은 들여쓰기된 코드가 자료구조에 저장된 데이터 개수만큼 반복된다. 3개의 데이터가 있으니 ####를 세번 넣기
# 133
for 변수 in ["A", "B", "C"]:
  print(변수)

a = ["A", "B", "C"]
