# # 연습문제 1
#
# lst = [10, 1, 5, 2 ] # list 생성
# result=(lst * 2)
# print('단계 1: ', result)
# rst = result[0] * 2
# # print(rst)
# result.append(rst)
# print('단계2: ', result)
#
#
# result2 = result[1::2]
# print('단계3 : ', result2)
# result2 = []
# i = 0
# for n in result :
#     if (i % 2) != 0 :
#         result2.append(n)
#     i += 1
#
# print('단계3 : ', result2)
#
#
# 연습문제 1
#
lst = [10,1,5,2]
result = lst*2
print('단계 1:', result)

first = lst[0]*2
result.append(first)
print('단계2:', result)
#
# result2 = []
# i = 0
# for i in result :
#     if i %2 == 0 :
#         i += 1
# #
# result2 = result[1::2]
# # print('단계3 : ', result2)
#
#
# result2 = []
# i = 0
# for n in result :
#     if (i % 2) != 0 :
#         result2.append(n)
#     i += 1
#
# print('단계3 : ', result2)

















#
#
# # # 연습문제 2
# # size = int(input('vector 수: ' ))
# # list = []
# #
# # for i in range(size) :
# #     list.append(i)
# #
# # print('vector 크기:', len(list))
#
# # # 연습문제 2
# # size = int(input('vector 수 : '))
# # lst = []
# #
# # for i in range(size) :
# #     lst.append(int(input()))    #뭔말이지   ???
# #
# # print('vector 크기:', len(lst))
# #
# # #2-2
# # size1 = int(input('vector 크기 : '))
# # lst1 = []
# #
# # for i in range(size1) :
# #     lst1.append(int(input()))
# # if int(input()) in lst1 :      #찾을값 입력 (prompt없음) - 헷갈리네용
# #     print('yes')
# # else :
# #     print('no')
#
#
# # # 연습문제 3 내 ver
# # message = ['spam', 'ham', 'spam', 'ham', 'spam']
# # # dummy = [ 실행문 for msg in message ]
# # # dummy = [] 에 for in
# #
# # dummy = [ 1 if msg == 'spam' else 0 for msg in message]
# # # 실행문 if문 3항 사용 !! 한줄로 해서 편리
# #
# # print(dummy)
# #
# # #3-2
# #
# # # list for + if까지 쓰라네요...
# # spam_list = [ msg for msg in message]
# # for msg in spam_list :
# #     if spam_list[1] :
# # # 1만 출력하고 싶은데!!!! 어떻게 ???
# #         print(spam_list)
#
# #연습문제 3
#
# # dummy = [ 실행문 for msg in message ]
# message = ['spam', 'ham', 'spam', 'ham', 'spam']
# dummy = [ 1 if msg == 'spam' else 0 for msg in message]
# print(dummy)
#
#
# spam_list = [ msg for msg in message if msg == 'spam']
# # 3항 이용
# print(spam_list)
#
#
#
#
#
# # 연습문제 4
#
# position =  ['과장', '부장', '대리', '사장','대리','과장']
# uni_position = list(set(position))    # set 하면 중복제외 -> 원래 type인 list
# print('중복되지 않은 직위:', uni_position)
#
# position_cnt = {}
# for p in position :
#     position_cnt[p] = position_cnt.get(p, 0) + 1
# print('각 직위별 빈도수 : ', position_cnt)
#








