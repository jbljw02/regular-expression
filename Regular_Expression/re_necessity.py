# 1. 정규 표현식을 사용하지 않은 코드

text = "my email is jbljw02@naver.com"

# 공백을 기준으로 문자를 구분하여, @가 포함된 문자를 출력해주는 함수
def find_email(text):
    words = text.split()

    for word in words:
        if '@' in word:
            return word

# find_email 함수에서 출력된 문자를 email 변수에 저장
email = find_email(text)

# email 주소를 출력
if email:
    print("찾은 이메일 주소 : ", email)
else:
    print("이메일 주소 찾기 실패")


# 2. 정규 표현식을 사용한 코드

import re

text = "my email is jbljw02@naver.com"

# 이메일 주소의 패턴을 정규 표현식으로 작성
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# search() 메소드를 이용하여 text에서 이메일 주소를 찾음
match = re.search(pattern, text)

# email 주소를 출력
if match:
    email = match.group()
    print("찾은 이메일 주소 : ", email)
else:
    print("이메일 주소 찾기 실패")