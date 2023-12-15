# 문제 1

email = """ hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

from re import findall,match

for e in email.split(sep='\n') :
# findall
    result = findall('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]\\w{,2}',e)

    # 패턴과 일치하는 email
    if result:
        str_result = result   # string 반환
        print('findall :', str_result)

    # match
    result2 = match('^[a-z]\\w{3,}@[a-z]\\w{3,}.[a-z]\\w{,3}',e)

    if result2 :
        print('match: ', e)

#complie ver
#
# import re
#
# email = """ hong@12.com
# you2@naver.com
# 12kang@hanmail.net
# kimjs@gmail.com"""
#
# # 정규표현식 패턴을 미리 컴파일
# pat = re.compile(r'^[a-z]\w{3,}@[a-z]\w{2,}\.[a-z]\w{,2}')
#
# for e in email.split(sep='\n'):
#     # findall
#     result = pat.findall(e)
#
#     # 패턴과 일치하는 email
#     if result:
#         str_result = result[0]  # string 반환
#         print('findall :', str_result)
#
#     # match
#     result2 = pat.match(e)
#
#     if result2:
#         print('match: ', e)



# 문제 2

from re import findall
emp = ["2014홍길동220", "2002이순신300","2010유관순260"]

#함수정의
def name_pro(emp) :
    names = []

    for e in emp :
        name = findall('[가-힣]{3}', e)    #홍길동
        names.append(name)

    return names

# 함수호출
names = name_pro(emp)
print('names =', names)


#문제 3
from re import findall
from statistics import mean

emp = ["2014홍길동220", "2002이순신300","2010유관순260"]

#함수정의
def pay_pro (emp) :
    pays = []

    for e in emp :
        tmp = findall('[가-힣][0-9]{3}', e)
        pay = findall('[0-9]{3}',tmp[0])    #['220'] -> 220

        pays.append(int(pay[0]))    #['220'] -> 220

    print(pays)    # 220.300.260
    return mean(pays)

pays_mean = pay_pro(emp)
print('전체 사원의 급여 평균:', pays_mean)


# 문제 4
from re import findall
from statistics import mean

emp = ["2014홍길동220", "2002이순신300","2010유관순260"]

def pay_pro (x) :
    # from statistics import mean    # 평균함수 얘를 왜 여기 데려옴...????
    # import re
    tmp = [findall('[가-힣]{3}', user) for user in x]
    name = [user[0] for user in tmp]    #vector 저장


    pay = []
    tmp = [findall('[가-힣][0-9]{3}', user) for user in x]
    #이름 + 급여추출
    for user in tmp :
        str_user = user [0]
        pay.append(int(str_user[1:]))

    pay_avg = mean(pay)
    print('전체 급여 평균 : %d'%pay_avg)
    print('평균 이상 급여 수령자')
    for i in range(len(x)) :
        if pay[i] >= pay_avg :
            print(name[i], '=>', pay[i])


pay_pro(emp)



# 문제 5
from re import findall, sub

texts = ['AFAB54747, asabag?', 'abTTa $$;a12:2424', 'uysfsfA,A124&***$?']

def clean_text(text):
    texts_re = text.lower()
    texts_re2 = sub('[0-9]', '' , texts_re)
    texts_re3 = sub('[,.?!;:]', '' , texts_re2)
    texts_re4 = sub('[@#$%^&*()~]', '', texts_re3)
    texts_re5 = ''.join(texts_re4.split())
    return texts_re5


# 함수호출
texts_result = [clean_text(text) for text in texts]
print(texts_result)






