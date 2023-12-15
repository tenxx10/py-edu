
# 연습문제 1 - 1

zim = int(input('짐의 무게는 얼마입니까?', ))

if zim >= 10 :
    print('수수료는 ' + format(10000,'3,d')+ '원 입니다.')
else :
    print('수수료는 없습니다.')

# 연습문제 1-2
# 10의 배수단위로 증가 시켜야함 // 이든 % 사용해야함 ..^^

zim = int(input('짐의 무게는 얼마입니까?', ))
if zim >= 10 :
    price = (zim // 10) * 10000  # 참일 경우 가격을 계산하는 변수를 만듦
     # 15를 출력해도 몫은 1이 나와서 거기에 10000 곱하면 만원임
    #20 이면 몫 2가 나와서 2만원 !!!! 그래서 // 를 사용함 몫만 구할 거라서
    print('수수료는 '+ format(price, '3,d')+ '원 입니다')
else :
    print('수수료는 없습니다.')

    # 20이상으로 입력했을시 값이 두개가 뜸


# 연습문제 2

import random
print('>>숫자 맞추기 게임<<')
com = random.randint(1,10) #1~10 사이 난수 정수 발생

while True : #while문은 조건 달성하면 종료. while True는 무한루프 * 탈출조건 필수
    my = int (input('예상 숫자를 입력하시오 :')) # 숫자입력
    if my == com : #==같다면!
        print('~~성공~~')
        break #* 탈출조건
    elif my > com :
        print('더 작은 수 입력하삼')
        continue
    elif my < com :
        print('더 큰 수 입력하삼')
        continue
# 헐 이거 재밌다

# 연습문제 3
tot = 0
print('수열 =', end=' ') #한줄 출력하라는 조건

for i in range(1,101) :
    if i %3 == 0 and i %2 != 0 :
        print(i, end='')
        tot += i

print('\n누적합= %d' %tot) # tot가 2배수 제외한 3배수들의 누적합이어야함

#연습문제 3

tot = 0
print ('수열 = ', end= "")
for i in range(1,101) :
    if i % 3 == 0 and i% 2 != 0 :
        print(i, end='')
        tot += i

print('\n누적합: %d'%tot)



# # 연습문제 4
#
# multiline = """ 안녕하세요. 파이썬의 세계로 오신걸
# 환영합니다.
# 파이썬은 비단뱀처럼 매력적인 언어입니다."""
#
# sents= []
# words = []
#
# for sen in multiline.spilt(sep='\n') :
#     sents.append(sen)
# for word in sen.split():
#     words.append(word)
#
#     print(sents)
#     print('단어 개수: ', len(sents))
#     print(words)
#     print('단어 개수: ', len(words))
#

# 연습문제 4

multiline = """ 안녕하세요. 파이썬의 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

#공백 문자를 기준으로 단어수 카운터
cnt = 0
doc = [ ] # 빈 list : 줄 단위 출력
word = [] # 빈 list : 단어

for line in multiline.split('\n') : #줄바꾸기로도 나눠져있음 이걸로 3개 해둠
    doc.append(line)
    for w in line.split(""): #공백으로 , 요걸로 7개 구분됨
        word.append(w)
        print(w) # list는 한줄로 나와서 줄바꿈 사용하기 위해 print로 출력
        cnt += 1

# 결과 출력
print('단어수 :', cnt)
print(doc)
print(word)



















