# re 모듈관련 함수 import
from re import split, match, compile

# 텍스트 자료
multi_line= """http://www.naver.com
http://www.daum.net
www.hongkildong.com"""

# 1 구분자를 이용하여 문자열 분리
web_site = split ('\n', multi_line)
# spilt ('pattern', string)
print(web_site)               #['http://www.naver.com', 'http://www.daum.net', 'www.hongkildong.com'] 이렇게 뜸

# 패턴 객체 만들기
pat = compile("http://")

# 3 패턴 객체를 이용하여 정상 웹 주소 선택하기
sel_site = [ site for site in web_site if match(pat,site)]
print(sel_site)