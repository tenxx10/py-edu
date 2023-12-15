

# 연습문제 1

su = 5
dan = 800
print('su 주소:', id(su))
print('dan 주소:',id(dan))

price = su * dan
print('금액=', price)


# 연습문제 2

x = 2
y = (2.5 * x**2 + 3.3 * x + 6)
print('2차 방정식 결과 = ', y)

#
# # 문제 3
#
#
# fat = int(input('지방의 그램을 입력하세요:'))   # 25
# car = int(input('탄수화물의 그램을 입력하세요: '))   #520
# pro = int(input('단백질의 그램을 입력하세요: '))    #45
#
# result = (fat*9 + car*4 + pro*4)
# print('총칼로리:',result,'cal')


# 문제 4

word1 = str(input('첫번째 단어: '))
word2 = str(input('두번째 단어: '))
word3 = str(input('세번째 단어: '))

print('='*15)
abbr = (word1[0]+ word2[0]+ word3[0])
print('약자:', abbr)







