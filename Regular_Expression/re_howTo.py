## 메타 문자

import re

# 1. '.'(dot) : 임의의 한 문자와 매치됩니다.
pattern = 'gr.y'
text = 'gray'
match = re.search(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 2. '*' : 바로 앞 문자가 0번 이상 반복되면 매치됩니다.
pattern = 'xy*z'
texts = ['xz', 'xyz', 'xyyyyyyyyz']
for text in texts:
    match = re.search(pattern, text)
    if match:
        print("매칭 성공")
    else:
        print("매칭 실패")

# 3. '+' : 바로 앞 문자가 1번 이상 반복되면 매치됩니다.
pattern = 'xy+z'
texts = ['xz', 'xyz', 'xyyyyyyyyz']
for text in texts:
    match = re.search(pattern, text)
    if match:
        print("매칭 성공")
    else:
        print("매칭 실패")

# 4. '?' : 바로 앞 문자가 0번 혹은 1번 나타나면 매치됩니다.
pattern = 'xy?z'
texts = ['xyz', 'xz', 'xyyz']
for text in texts:
    match = re.search(pattern, text)
    if match:
        print("매칭 성공")
    else:
        print("매칭 실패")

# 5. '[]' : 대괄호 안에 있는 문자 중 하나와 매치됩니다.
pattern = '[abcde]'
texts = ['apple', 'banana', 'fx']
for text in texts:
    match = re.search(pattern, text)
    if match:
        print("매칭 성공")
    else:
        print("매칭 실패")

# 6. '$' : 문자열의 끝 부분과 매칭됩니다.
pattern = 'Bomb$'
text = 'Water Bomb!'
match = re.search(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 7. '^' : 문자열의 시작 부분과 매칭됩니다.
pattern = '^Bomb'
text = 'Water Bomb!'
match = re.search(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 8. '\' : 특수 문자를 이스케이프 하거나, 특수한 의미를 가진 문자와 매칭됩니다.
pattern = '\$10'
text = 'Price is $10'
match = re.search(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 9. '|' : 둘 중 하나의 패턴과 매칭됩니다.
pattern = 'chrome|naver'
texts = ['chrome', 'naver', 'firefox']
for text in texts:
    match = re.search(pattern, text)
    if match:
        print("매칭 성공")
    else:
        print("매칭 실패")

# 10. '()' : 패턴을 그룹화합니다.
pattern = '(ab)+'
text = 'ababac'
match = re.search(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 11. '{}' : 패턴의 반복을 나타내는 용도로 사용됩니다.
pattern = 'a{2,4}'
text = 'aaa'
match = re.search(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")


## 메소드

# 1. search : pattern과 text에서 첫번째로 매칭되는 부분을 찾습니다. 매칭에 성공할 경우 re.Match 객체를 반환하고, 실패할 경우 None을 반환합니다.
pattern = 'Bomb'
text = 'Water Bomb!'
match = re.search(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 2. match : pattern과 text가 일치하는지 문자열의 시작부터 검사합니다. 매칭에 성공할 경우 re.Match 객체를 반환하고, 실패할 경우 None을 반환합니다.
pattern = 'Water'
text = 'Water Bomb!'
match = re.match(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 3. fullmatch : pattern과 text가 완전히 일치하는지 검사합니다. 매칭에 성공할 경우 re.Match 객체를 반환하고, 실패할 경우 None을 반환합니다.
pattern = 'Water Bomb!'
text = 'Water Bomb!'
match = re.fullmatch(pattern, text)
if match:
    print("매칭 성공")
else:
    print("매칭 실패")

# 4. findall : pattern과 text에서 매칭되는 모든 부분을 리스트로 반환합니다. 매칭된 부분이 없을 경우 빈 리스트를 반환합니다.
pattern = 'ab'
text = 'abcdefg'

match_list = re.findall(pattern, text)
print(match_list)

# 5. finditer : pattern과 string에서 매칭되는 모든 부분을 찾아서 이터레이터로 반환합니다. 매칭된 부분은 re.Match 객체로 나타나며 매칭된 부분이 없을 경우 빈 이터레이터를 반환합니다.
pattern = 'ab'
text = 'abcabcabc'
matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())

# 6. group : 그룹 인덱스를 지정하여 매칭된 부분을 반환합니다.
pattern = r'(\d+)/(\d+)/(\d+)'
text = '2000/09/17'
match = re.search(pattern, text)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2, 3))

# 7. start : 매칭된 부분의 시작 인덱스를 반환합니다.
pattern = 'Bomb'
text = 'Water Bomb!'
match = re.search(pattern, text)
if match:
    print(match.start())

# 8. end : 매칭된 부분의 끝의 다음 인덱스를 반환합니다.
pattern = 'Water'
text = 'Water Bomb!'
match = re.search(pattern, text)
if match:
    print(match.end())

# 9. span : 매칭된 부분의 시작 및 끝의 다음 인덱스를 튜플로 반환해줍니다.
pattern = 'Water'
text = 'Water Bomb'
match = re.search(pattern, text)
if match:
    print(match.span())